TensorRT-RTX 是面向 RTX GPU 的推理运行时。最小闭环三步：**下载 ONNX → AOT 建 engine → JIT 推理**。

## 三步

```bash
# 1. 下载示例模型
wget https://download.onnxruntime.ai/onnx/models/resnet50.tar.gz
tar xzf resnet50.tar.gz              # 得到 resnet50/model.onnx

# 2. 构建 engine（AOT，不需要 GPU，约 20~30 秒）
tensorrt_rtx --onnx=resnet50/model.onnx --saveEngine=resnet_engine.trt

# 3. 推理（JIT，需要 RTX GPU）
tensorrt_rtx --loadEngine=resnet_engine.trt \
             --runtimeCacheFile=resnet.cache
```

预期输出：第 2 步打印 `Engine serialized to resnet_engine.trt`；第 3 步打印延迟（如 `~3 ms per iteration`）并写出 `resnet.cache`。

## AOT 与 JIT

| 阶段 | 做什么 | 需要 GPU |
| --- | --- | --- |
| **AOT**（ahead-of-time） | ONNX → 序列化 engine，跨支持的 RTX GPU / 操作系统可移植 | 否 |
| **JIT**（just-in-time） | 加载 engine，为当前设备编译 kernel，首次运行较慢 | 是 |

`--runtimeCacheFile` 把 JIT 产物存下来，后续启动直接复用，避免每次重新编译。

构建服务器可以只跑第 1、2 步（纯 CPU），把 `.trt` 分发到有 GPU 的机器执行第 3 步。

## 产物清单

- `resnet50/model.onnx`
- `resnet_engine.trt`（约 25 MB，随模型和精度变化）
- `resnet.cache`（首次成功 JIT 后生成）

## 排错

| 现象 | 检查 |
| --- | --- |
| `--help` 找不到命令 | SDK 的 `bin` 是否在 `PATH`；Linux 还要看 `LD_LIBRARY_PATH` 是否含 `lib` |
| 第 1 步没有 `model.onnx` | 重新下载解压，确认工作目录与第 2 步路径一致 |
| 第 2 步构建失败 | 不需要 GPU；查 ONNX 路径、不支持的算子、支持矩阵里的精度限制 |
| 第 3 步 GPU / 驱动 / CUDA 报错 | RTX GPU 在位、驱动已装、CUDA 版本匹配；首次 JIT 几秒属正常 |
| 推理成功但没有 cache | `--runtimeCacheFile` 是否设置、输出目录是否可写 |

## 什么时候超出 CLI

CLI 适合 ONNX + 单模型快速验证。需要自定义预处理/后处理、集成到 C++/Python 应用、PyTorch 原生接口或性能调优时，转去：

- 官方 demo / samples（C++、Python、Flux 等端到端例子）；
- Runtime API（C++/Python 集成）；
- PyTorch 接口；
- 从 TensorRT 迁移的 porting guide；
- Best Practices。

## 易错点

- engine 可跨 RTX GPU 移植，但 JIT 仍会针对具体设备编译；换机器后首次运行会慢。
- 第 2 步不需要 GPU，别把构建失败误判成“没显卡”。
- 没有 runtime cache 不代表失败，只是下次还要重新 JIT。
- CLI 只覆盖 ONNX + 快速验证；自定义前后处理、应用集成要转 Runtime API / samples。
