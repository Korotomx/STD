---
tags:
  - 功能实现
  - ONNX
  - TensorRT
  - Engine
  - 推理部署
  - FP16
  - JetsonOrin
---

# ONNX 与 TensorRT Engine 的区别 · 功能实现 · N022

**时间:** 2026-10-22
**标签:** #功能实现 #ONNX #TensorRT #Engine #推理部署 #FP16 #JetsonOrin
**关联:** [[N019 TensorRT部署onnx转engine并推理]]（builder / runtime 的 Python 实战）· [[N021 Ultralytics训练参数全解]]（导出参数）· [[N020 NDJSON数据集与YOLO姿态估计pose训练]]（groundzero 模型）

## 一句话

**ONNX 描述「要算什么」，Engine 是「针对某一块 GPU、某个 TensorRT 版本、某个输入尺寸和精度，编译好的最快算法方案」。** ONNX 可跨平台拷贝；Engine 不可移植，必须在目标设备上重新 build。

## 实际情况

groundzero 的交通标志 pose 模型最终要跑在 **NVIDIA Jetson Orin** 上，所以链路是：

```
groundzero: best.pt --export--> best.onnx        （通用，可拷贝）
Orin      : best.onnx --trtexec--> best_fp16.engine （目标机上编译）
```

`.engine` 不是「另一种模型格式」，而是 TensorRT 的**序列化推理计划（plan）**：只负责前向计算，不含预处理、NMS、后处理，也不能训练。

## 1. 两者的定位

| | ONNX | TensorRT Engine |
| ---- | ---- | ---- |
| 本质 | 通用计算图（算子 + 权重） | 针对特定 GPU / 版本编译后的推理计划 |
| 可移植性 | 跨框架、跨硬件 | **不可移植** |
| 谁执行 | onnxruntime / OpenCV DNN / TensorRT 等 | 只能由 TensorRT Runtime 加载 |
| 内容 | 原始算子、FP32 权重 | 融合后的层、选好的 kernel、FP16/INT8 权重、内存分配方案 |
| 能否训练 | 只推理 | 只推理 |
| 类比 | C 源码 / Java 字节码 | 针对某台机器编译出的可执行文件 |

## 2. Engine 里到底有什么

`trtexec --onnx=best.onnx --saveEngine=best_fp16.engine --fp16` 这一步，TensorRT 会做：

1. **解析 ONNX**，建内部网络；
2. **层融合**：Conv + BN + ReLU 合成一个 kernel，减少显存读写；
3. **精度选择**：允许的层用 FP16 kernel，敏感层自动回退 FP32；
4. **kernel autotuning**：同一算子有多种实现，实测选最快的；
5. **内存规划**：复用中间张量，减少显存占用；
6. **序列化**：把选好的方案写成 `.engine`。

所以 engine 不是「模型文件」，而是**已经做完图优化和硬件适配的成品**。运行时只做 `deserialize + execute`，不再解析 ONNX、不再经过 PyTorch。

## 3. 为什么它不能拷来拷去

Engine 和下面这些**绑定**：

- **GPU 架构**：Orin 是 Ampere（SM 8.7），RTX 5060 是 Blackwell，指令集不同；
- **TensorRT 版本**：TRT 10 的 engine 一般不能被 TRT 8 加载；
- **CUDA / JetPack 版本**；
- **输入 shape / batch**：静态 640×640、batch=1 的 engine 不能直接吃别的尺寸；
- **精度设置**：FP16 engine 和 FP32 engine 是两份不同的计划。

因此：

- 在开发机（RTX 5060）上 build 的 engine **不能**拷到 Orin 用；
- 换 JetPack、换 TensorRT、换输入尺寸、换 batch，都要**重新 build**；
- 正确做法是只把 **ONNX** 当跨设备产物。

## 4. Engine 不包含什么

它只包含**网络前向**。下面这些仍在自己的代码里：

- letterbox / resize / BGR→RGB / `/255`；
- NMS、置信度过滤；
- 框和关键点从 640 空间映射回原图；
- ROS2 消息封装与发布。

groundzero 的 pose 模型，engine 输出仍然是「框 + 8 个关键点」的原始张量，后处理要自己写；不能直接套 detect 的 `[1,8,8400]` 解码。

## 5. 实际使用

### Python

```python
import tensorrt as trt

logger = trt.Logger(trt.Logger.WARNING)
runtime = trt.Runtime(logger)
with open("best_fp16.engine", "rb") as f:
    engine = runtime.deserialize_cuda_engine(f.read())
context = engine.create_execution_context()
# 然后 set_tensor_address + execute_async_v3
```

完整 builder / runtime / 显存绑定的代码见 [[N019 TensorRT部署onnx转engine并推理]]。

### 命令行冒烟测试

```bash
trtexec --loadEngine=best_fp16.engine --iterations=200
```

### C++

链接 `nvinfer` / `nvinfer_plugin`，用 `IRuntime::deserializeCudaEngine`。**OpenCV DNN 和 onnxruntime 都不能加载 `.engine`。**

## 6. groundzero 的落地流程

### ① 开发机：导出 FP32 ONNX

```python
from ultralytics import YOLO

m = YOLO("runs/pose/train-4/weights/best.pt")
onnx_path = m.export(
    format="onnx",
    imgsz=640,
    opset=17,
    quantize=None,   # FP32，不量化
    simplify=True,
    dynamic=False,
    batch=1,
    nms=False,
)
print(onnx_path)
```

导出后确认输出结构：

```python
import onnx

m = onnx.load(onnx_path)
for o in m.graph.output:
    print(o.name, [d.dim_value for d in o.type.tensor_type.shape.dim])
```

### ② Orin：build FP16 Engine

```bash
/usr/src/tensorrt/bin/trtexec \
  --onnx=best.onnx \
  --saveEngine=best_fp16.engine \
  --fp16 \
  --memPoolSize=workspace:4096MiB \
  --verbose
```

- `--fp16` 允许 FP16 kernel，输入/输出通常仍是 FP32；
- 静态 640 不需要 shape profile；
- 先 `sudo nvpmodel -m 0` + `sudo jetson_clocks`，否则 FPS 受功耗限制。

### ③ 验证

```python
from ultralytics import YOLO

m = YOLO("best_fp16.engine", task="pose")
r = m.val(data="traffic-signs.ndjson", imgsz=640)
print("box mAP50:", r.box.map50, "pose mAP50-95:", r.pose.map)
```

姿态任务对 FP16 比纯检测敏感，重点看 **pose mAP50-95**。

## 7. 常见误区

| 误区 | 实际 |
| ---- | ---- |
| 「engine 是更小的模型文件」 | 它是硬件专用执行计划，可能比 ONNX 大，也可能小 |
| 「开发机 build 好拷过去就行」 | GPU 架构 / TensorRT 版本不同，load 会失败 |
| 「engine 里包含 NMS」 | 默认不包含；`nms=True` 才会嵌入，且输出结构会变 |
| 「FP16 会明显掉精度」 | 通常只掉零点几个点，但姿态关键点要实测 |
| 「engine 能继续训练」 | 不能，只能推理 |
| 「onnxruntime 也能跑 engine」 | 不能，只能用 TensorRT Runtime |

## 总结

**本质：** ONNX 是通用计算图，负责「模型长什么样」；Engine 是按 Orin 的 GPU 架构、TensorRT 版本、输入尺寸和 FP16 精度**现场编译出来的机器码**。因此 engine 必须在目标设备上 build，换设备 / 换 JetPack / 换 shape 都要重编；它只加速前向，不替代预处理、NMS 和后处理。

**标签:** #功能实现 #ONNX #TensorRT #Engine #推理部署 #FP16 #JetsonOrin
