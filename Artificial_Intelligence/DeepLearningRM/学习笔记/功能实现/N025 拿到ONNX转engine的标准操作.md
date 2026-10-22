---
tags:
  - 功能实现
  - ONNX
  - TensorRT
  - Engine
  - trtexec
  - 推理部署Inference
  - 操作手册HowTo
---

# 拿到 ONNX 转 engine 的标准操作 · 功能实现 · N025

**时间:** 2026-10-22
**标签:** #功能实现 #ONNX #TensorRT #Engine #trtexec #推理部署Inference #操作手册HowTo #Workspace
**关联:** [[N024 ONNX编译成engine的原理]]（为什么这样做）· [[N022 ONNX与TensorRT Engine的区别]]（两者定位）· [[N019 TensorRT部署onnx转engine并推理]]（Python 实战）

## 一句话

拿到任何一份 ONNX，标准流程只有四步：**查输入输出 → 确认静态/动态 shape → `trtexec` build → 加载验证**。90% 的失败都能在前两步定位。

## 0. 前置检查（缺一不可）

```bash
# 1. TensorRT 可用
source ~/.bashrc
trtexec --version                 # TensorRT v110400 [b106]

# 2. Python 侧可用（可选）
python -c "import tensorrt as trt; print(trt.__version__)"   # 11.4.0.106

# 3. 确认当前机器就是目标 GPU
nvidia-smi                        # engine 不能跨 GPU 架构使用

# 4. 确认 ONNX 文件完整
ls -lh model.onnx
```

如果 `trtexec: command not found`：

```bash
export TENSORRT_ROOT=/home/akiha/opt/TensorRT-11.4.0.106
export PATH=$TENSORRT_ROOT/bin:$PATH
export LD_LIBRARY_PATH=$TENSORRT_ROOT/lib:$LD_LIBRARY_PATH
```

非交互 shell / IDE 不会读 `.bashrc`，要用全路径：

```bash
$TENSORRT_ROOT/bin/trtexec ...
```

## 1. 第一步：查 ONNX 的输入输出（最重要）

```python
import onnx
m = onnx.load("model.onnx")
onnx.checker.check_model(m)

for i in m.graph.input:
    print("input ", i.name, [d.dim_value or d.dim_param for d in i.type.tensor_type.shape.dim],
          onnx.TensorProto.DataType.Name(i.type.tensor_type.elem_type))
for o in m.graph.output:
    print("output", o.name, [d.dim_value or d.dim_param for d in o.type.tensor_type.shape.dim],
          onnx.TensorProto.DataType.Name(o.type.tensor_type.elem_type))
```

要确认四件事：

| 要确认 | 为什么 |
| ---- | ---- |
| 输入名字 | build 和推理时都要按名字绑定 |
| 输入 shape | 决定静态还是动态、决定 build 命令 |
| 输入 dtype | engine 输入必须是 FP32（或图里指定的类型） |
| 输出 shape | 决定后处理怎么写，必须提前知道 |

groundzero 的结果：

```
input  images  [1, 3, 640, 640] FLOAT
output output0 [1, 300, 30]     FLOAT
```

补充检查算子：

```python
import collections
print(collections.Counter(n.op_type for n in m.graph.node))
```

如果出现 TensorRT 不支持的算子，会在 build 的 Parse 阶段报错。

## 2. 第二步：区分静态 / 动态 shape

看第 1 步打印的维度：

| shape 长什么样 | 类型 | build 命令 |
| ---- | ---- | ---- |
| `[1, 3, 640, 640]` | **静态** | 直接 build，最简单 |
| `[-1, 3, 640, 640]` 或 `["batch", 3, 640, 640]` | **动态** | 必须给 min/opt/max profile |

**静态 shape 优先。** 导出 ONNX 时就固定 `dynamic=False`、`batch=1`，部署最省事。

## 3. 第三步：build

### 3.1 静态 shape（推荐）

```bash
trtexec \
  --onnx=/home/akiha/deep_learning/groundzero/runs/pose/train-4/weights/best.onnx \
  --saveEngine=/home/akiha/deep_learning/groundzero/runs/pose/train-4/weights/best.engine \
  --memPoolSize=workspace:2048M
```

参数含义：

| 参数 | 作用 | 建议 |
| ---- | ---- | ---- |
| `--onnx` | 输入 ONNX 路径 | 绝对路径最稳 |
| `--saveEngine` | 输出 engine 路径 | 放在 ONNX 同目录 |
| `--memPoolSize=workspace:2048M` | build 期临时显存 | 2 GB 起步；`M/G` 是合法后缀 |
| `--verbose` | 打印逐层信息 | 排查问题时加 |
| `--timingCacheFile=cache.bin` | 复用测速结果 | 反复 build 时加速 |
| `--profilingVerbosity=detailed` | engine 里保留层名 | 需要 profile 时加 |

**单位坑：** 只认 `B / K / M / G`，**不认 `MiB`**。写 `2048MiB` 会被解析成 2048 **字节**，日志里显示：

```
Memory Pools: workspace: 0.00195312 MiB
```

然后 tactic 全部因显存不足失败。

### 3.2 动态 shape

```bash
trtexec \
  --onnx=model_dynamic.onnx \
  --saveEngine=model.engine \
  --minShapes=images:1x3x640x640 \
  --optShapes=images:1x3x640x640 \
  --maxShapes=images:4x3x640x640 \
  --memPoolSize=workspace:2048M
```

- `minShapes / optShapes / maxShapes` 必须**覆盖实际推理时用到的所有 shape**
- 推理前要调用 `context.set_input_shape("images", (1,3,640,640))`
- shape 越多，build 越慢，engine 越大；能用静态就用静态

### 3.3 Python build（可选）

不想依赖命令行时：

```python
import tensorrt as trt

logger  = trt.Logger(trt.Logger.INFO)
builder = trt.Builder(logger)
config  = builder.create_builder_config()
config.set_memory_pool_limit(trt.MemoryPoolType.WORKSPACE, 2 << 30)

network = builder.create_network()
parser  = trt.OnnxParser(network, logger)
if not parser.parse_from_file("best.onnx"):
    for i in range(parser.num_errors):
        print(parser.get_error(i))
    raise SystemExit("parse failed")

serialized = builder.build_serialized_network(network, config)
if serialized is None:
    raise SystemExit("build failed")
open("best.engine", "wb").write(bytes(serialized))
```

## 4. 第四步：验证 engine

### 4.1 命令行走一遍

```bash
trtexec --loadEngine=best.engine
```

能打印 `Throughput` / `Latency` 就说明 engine 可用。

### 4.2 Python 加载并推理（骨架）

```python
import tensorrt as trt
import torch

logger  = trt.Logger(trt.Logger.WARNING)
runtime = trt.Runtime(logger)
engine  = runtime.deserialize_cuda_engine(open("best.engine", "rb").read())
context = engine.create_execution_context()

# 输入输出按名字取，不按顺序
in_name  = engine.get_tensor_name(0)   # "images"
out_name = engine.get_tensor_name(1)   # "output0"

x = torch.from_numpy(blob).cuda()          # [1,3,640,640] float32
y = torch.empty(1, 300, 30, device="cuda") # 按第 1 步查到的输出 shape

context.set_tensor_address(in_name,  x.data_ptr())
context.set_tensor_address(out_name, y.data_ptr())
context.execute_async_v3(torch.cuda.current_stream().cuda_stream)
torch.cuda.synchronize()

out = y.cpu().numpy()   # [1, 300, 30]
```

如果 shape 是动态的，先 `context.set_input_shape(in_name, x.shape)`，再用 `context.get_tensor_shape(out_name)` 分配输出。

### 4.3 正确性验证（不要跳过）

拿同一张图，比较：

```
engine 结果  vs  原模型 (model.predict / onnxruntime) 结果
```

比较顺序：

1. 输出 shape 一致
2. 框的数量和分数接近
3. 坐标映射回原图后位置一致
4. 关键点 / 类别一致

直接看可视化图，容易把「前后处理错」误判成「engine 错」。

## 5. 精度：FP32 / FP16 怎么选

| 精度 | TRT 11 怎么做 | 说明 |
| ---- | ---- | ---- |
| FP32 | 默认 | ONNX 是 FP32 就直接 build |
| TF32 | 默认允许 | 比 FP32 快，精度略低，通常无感 |
| FP16 | 先把精度烤进 ONNX（ModelOpt AutoCast），再 build | TRT 11 没有 `--fp16` / `BuilderFlag.FP16` |
| INT8 | ONNX 里做 Q/DQ 量化 + 校准，再 build | 需要校准集 |

**建议：先 FP32 跑通、测速；确实不够快再考虑 FP16。** groundzero 模型 FP32 已经是 1.5 ms，没必要折腾。

## 6. 常见报错 → 原因

| 报错 | 原因 | 解决 |
| ---- | ---- | ---- |
| `trtexec: command not found` | PATH 没设 / 非交互 shell | 用全路径或 source `.bashrc` |
| `libnvonnxparser.so.11: cannot open` | 没有 `LD_LIBRARY_PATH` | 指向 `$TENSORRT_ROOT/lib` |
| `workspace: 0.00195312 MiB` | 单位写成 `2048MiB` | 改成 `2048M` |
| `Could not find any implementation for node` | workspace 太小，tactic 无法试跑 | 加大 workspace |
| Parse 阶段报 unsupported op | ONNX 有 TRT 不支持的算子 | 换 opset / 改导出 / 用 plugin |
| `serialize engine` / 反序列化失败 | engine 与 GPU / TRT 版本不匹配 | 在当前机器重新 build |
| 输出全是 0 / 结果错乱 | 绑错张量地址或 shape | 按名字绑定，核对输出 shape |
| 推理结果和原模型差很多 | 预处理不一致（RGB/BGR、归一化、letterbox） | 对照原模型预处理逐步比较 |

## 7. 产物管理

```
weights/
├── best.pt       训练产物（engine 阶段不需要）
├── best.onnx     通用图（可拷贝、可跨平台）
└── best.engine   当前 GPU 专用（不可移植）
```

建议命名带环境和精度，避免混淆：

```
best_fp32_sm120.engine
best_fp16_sm120.engine
```

## 8. 一页总结

```
查 ONNX 输入输出
      │  静态 shape？
      ├── 是 ──▶ trtexec --onnx --saveEngine --memPoolSize=workspace:2048M
      └── 否 ──▶ 加 --minShapes / --optShapes / --maxShapes
      │
      ▼
trtexec --loadEngine 验证
      │
      ▼
Python: Runtime → deserialize → Context → set_tensor_address → execute_async_v3 → synchronize
      │
      ▼
和原模型比结果 → 再谈性能
```

记住三条铁律：

1. **先查 shape，再 build**
2. **workspace 单位写 `M` / `G`，不写 `MiB`**
3. **engine 只在本机本版本可用，换环境重新 build**
