---
tags:
  - 功能实现
  - TensorRT
  - onnx
  - engine
  - 推理部署
  - GPU加速
  - YOLOv8
---

# TensorRT 部署：onnx 转 engine 并推理 · 功能实现 · N019

**时间:** 2026-10-21
**标签:** #功能实现 #TensorRT #onnx #engine #推理部署 #GPU加速 #YOLOv8
**关联:** [[N018 CUDA-cuDNN-TensorRT三层结构]]（概念）· [[N015 数据加载Dataset与DataLoader]]（前处理）· [[N017 ResNet-18架构与残差连接]]（训练出的模型）

## 实际情况

对应代码 `task2_onnx_ros2/trt_export_test.py`：把任务二训练的 `best.onnx`（YOLOv8n 装甲板检测，输入 `[1,3,640,640]` → 输出 `[1,8,8400]`）用 TensorRT 转成 engine 并加载推理，实测 **3.7ms/张**（onnxruntime-CPU 75ms，**加速 20 倍**）。产物 `best_fp16.engine`（15.3MB）+ 标注图 `results_trt/`。前后处理完全复用 `infer_onnx.py`（letterbox + 解码 + NMS），只把「推理引擎」从 onnxruntime 换成 TensorRT。

## 1. 整体两步

```
① 转 engine：onnx --(TensorRT builder)--> best_fp16.engine
② 推理：   engine --(TensorRT runtime)--> 检测结果
```

engine 是「针对当前 GPU 预编译好的执行计划」，构建一次、之后反复加载即可（连接 [[N018 CUDA-cuDNN-TensorRT三层结构]] 第 4 节）。

## 2. 转 engine：builder + parser + config

```python
builder = trt.Builder(logger)
network = builder.create_network()            # TensorRT 11 默认 explicit batch
parser  = trt.OnnxParser(network, logger)
with open(ONNX, "rb") as f:
    parser.parse(f.read())                    # 把 onnx 解析进 network

config = builder.create_builder_config()
config.set_memory_pool_limit(trt.MemoryPoolType.WORKSPACE, 1 << 30)  # 1GB 工作显存
serialized = bytes(builder.build_serialized_network(network, config)) # 编译成 engine 字节
with open(ENGINE, "wb") as f:
    f.write(serialized)
```

- `parse` 失败时用 `parser.get_error(i)` 逐条打印原因（比看异常好定位）
- `build_serialized_network` 返回 `IHostMemory`，要 `bytes()` 包一下才能 `len()`/写文件
- 本机构建一次 31.5s，engine 15.3MB

## 3. 推理：runtime + context + 显存指针

TensorRT 推理要自己管显存（不像 onnxruntime 那样 `sess.run` 一把梭）：

```python
runtime = trt.Runtime(logger)
engine  = runtime.deserialize_cuda_engine(open(ENGINE, "rb").read())
context = engine.create_execution_context()

inp = torch.from_numpy(blob).cuda()                       # 输入搬到 GPU
out = torch.empty((1, 8, 8400), dtype=torch.float32, device="cuda")

context.set_input_shape("images", tuple(inp.shape))       # 绑定形状
context.set_tensor_address("images", inp.data_ptr())       # 绑定输入指针
context.set_tensor_address("output0", out.data_ptr())      # 绑定输出指针
context.execute_async_v3(torch.cuda.current_stream().cuda_stream)
torch.cuda.synchronize()                                   # 等 GPU 算完
result = out.cpu().numpy()                                 # 结果搬回 CPU
```

- 输入/输出名（`images`/`output0`）用 `engine.get_tensor_name(i)` 动态读，别写死
- 显存缓冲用 torch 管理（`data_ptr()` 拿地址），省去手写 cudaMalloc/cudaMemcpy

## 4. 前后处理复用，不重写

letterbox（等比缩放 + 灰 114 补边）、BGR→RGB、/255、HWC→CHW、解码（前 4 框 + 后 4 类 argmax）、NMS——这些和 onnxruntime 版**完全一致**，直接照抄 `infer_onnx.py`。换推理引擎只换「第 2、3 节」这一段，前后处理不动。

## 5. 实测结果（4 张验证图）

| 图片 | TensorRT | onnxruntime-CPU | 加速 | 检测 |
| ---- | ---- | ---- | ---- | ---- |
| 1116.jpg | 3.67 ms | 79.58 ms | 21.7× | B1、B2 |
| 1161.jpg | 3.71 ms | 75.29 ms | 20.3× | R2 |
| 1182.jpg | 3.83 ms | 74.97 ms | 19.6× | B1 |
| 13892.jpg | 3.83 ms | 87.27 ms | 22.8× | R1 |

3.7ms ≈ 260 FPS，远高于实时（30 FPS）需求。这 3.7ms 里还含 Python 的数据搬运开销，纯 GPU 计算更快。

## 思考

（留白 —— 现在只是 Python 版验证。任务二最终要的是 C++ ROS2 节点里跑 TensorRT，`set_tensor_address` 这套在 C++ 里对应什么 API？）

## 总结

**本质：** TensorRT 部署分两步——builder 把 onnx 编译成 engine（parse + build_serialized_network），runtime 加载 engine 用 `context.set_tensor_address` + `execute_async_v3` 推理；前后处理与 onnxruntime 版完全复用，只换推理引擎；本机 YOLOv8n 从 75ms 加速到 3.7ms（20 倍，260 FPS）。
**标签:** #功能实现 #TensorRT #onnx #engine #推理部署 #GPU加速 #YOLOv8
