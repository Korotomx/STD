---
tags:
  - 功能实现
  - TensorRT
  - Engine
  - 推理Inference
  - 预处理Preprocess
  - Letterbox
  - 后处理Postprocess
  - 关键点Keypoint
---

# TensorRT engine 推理全流程：预处理 / 绑地址 / 解码 / 验证 · 功能实现 · N026

**时间:** 2026-10-22
**标签:** #功能实现 #TensorRT #Engine #推理Inference #预处理Preprocess #Letterbox #后处理Postprocess #关键点Keypoint #性能Profiling
**关联:** [[N025 拿到ONNX转engine的标准操作]]（engine 怎么来）· [[N024 ONNX编译成engine的原理]]（编译原理）· [[N027 数值精度与量化 FP32-FP16-BF16-TF32-INT8]]（FP32/FP16/INT8）· [[N028 图像坐标与Letterbox仿射变换]]（坐标原点 / 单位 / 正逆变换推导）· [[N023 模型全流程总览 从数据到Orin部署]]（全流程位置）· [[N020 NDJSON数据集与YOLO姿态估计pose训练]]（模型来源）

## 一句话

engine 只负责「`[1,3,640,640]` 进、`[1,300,30]` 出」；**预处理、绑定显存、解码、逆映射、画图全都要自己写**。推理链路可以拆成 5 个动作 + 2 次坐标变换。

## 实际情况

groundzero 交通标志 pose 模型：

```
原图 4096×3072 (BGR)
  → letterbox → 640×640，r=0.15625，pad(left,top)=(80,0)
  → RGB /255 / HWC→CHW → [1,3,640,640] float32
  → best.engine → [1,300,30]
  → 置信度过滤 → 逆映射 → 原图坐标的框 + 8 关键点
```

实测单张图耗时（RTX 5060）：

| 阶段 | FP32 | FP16 |
| ---- | ---- | ---- |
| 预处理（letterbox + RGB + CHW） | 1.16 ms | 1.05 ms |
| engine 推理（含 H2D/D2H + synchronize） | 3.79 ms | 3.44 ms |
| 后处理（解码 + 逆映射） | 0.14 ms | 0.15 ms |
| **端到端** | **5.10 ms（196 FPS）** | **4.35 ms（230 FPS）** |

> 纯 GPU kernel 是 FP32 1.385 ms vs FP16 0.690 ms（约 2×）；脚本内的固定拷贝/分配开销把端到端差距压缩到约 15%。

## 0. 全景数据流

```
原图 BGR H×W×3
   │ ① letterbox：等比缩放 + 灰边
   ▼
640×640 BGR        ── 记住 r 和 pad，逆映射要用
   │ ② BGR→RGB → /255 → HWC→CHW → 加 batch
   ▼
[1,3,640,640] float32
   │ ③ 绑地址 + execute_async_v3 + synchronize
   ▼
[1,300,30] float32（仍是 640 坐标系）
   │ ④ 置信度过滤 + 解码
   ▼
框 + 8×(x,y,conf)
   │ ⑤ 逆 letterbox：(x-pad)/r
   ▼
原图坐标 → 画图 / 发布
```

```mermaid
flowchart LR
    A[原图 BGR] -->|letterbox + RGB + CHW| B["[1,3,640,640]"]
    B -->|engine 前向| C["[1,300,30]"]
    C -->|conf 过滤 + 解码| D[框 + 关键点<br/>640 坐标]
    D -->|减 pad 除以 r| E[原图坐标]
    E --> F[画图 / ROS2 发布]
```

## 1. 预处理：letterbox

模型输入固定 640×640。直接 `cv2.resize(img, (640,640))` 会把长宽比压扁，框和关键点全都偏，所以必须**等比缩放 + 补灰边**。

```python
r = min(640 / h, 640 / w)                  # 用长边算比例
new_w, new_h = round(w * r), round(h * r)
resized = cv2.resize(img, (new_w, new_h))
dw, dh = (640 - new_w) / 2, (640 - new_h) / 2
left, right = round(dw - 0.1), round(dw + 0.1)
top, bottom = round(dh - 0.1), round(dh + 0.1)
padded = cv2.copyMakeBorder(resized, top, bottom, left, right,
                            cv2.BORDER_CONSTANT, value=(114, 114, 114))
```

三件事必须记住：

1. **缩放比例 `r`**
2. **左上补边 `(left, top)`**
3. 补边值 114（YOLO 默认灰）

groundzero 的例子：`4096×3072`（高×宽），`r=0.15625`，缩放后 `640×480`，左右各补 80。

> 坐标系为什么以左上为原点、单位为什么是连续像素、正逆变换的偏置怎么推，见 [[N028 图像坐标与Letterbox仿射变换]]。

### 1.1 转成张量

```python
rgb = cv2.cvtColor(padded, cv2.COLOR_BGR2RGB)  # OpenCV 是 BGR，训练是 RGB
x = rgb.astype(np.float32) / 255.0             # 归一化
x = np.transpose(x, (2, 0, 1))[None]           # HWC -> CHW，再加 batch
x = np.ascontiguousarray(x)                    # TensorRT 要求内存连续
```

## 2. 加载 engine：5 个动作

```python
logger  = trt.Logger(trt.Logger.WARNING)
runtime = trt.Runtime(logger)
engine_bytes = read_engine_bytes(engine_path)   # 跳过 Ultralytics 的 JSON 元数据头
engine  = runtime.deserialize_cuda_engine(engine_bytes)
context = engine.create_execution_context()

in_name  = engine.get_tensor_name(0)   # "images"
out_name = engine.get_tensor_name(1)   # "output0"

x = torch.from_numpy(blob).cuda()
y = torch.empty(tuple(engine.get_tensor_shape(out_name)),
                dtype=torch.float32, device="cuda")

context.set_tensor_address(in_name,  x.data_ptr())
context.set_tensor_address(out_name, y.data_ptr())
context.execute_async_v3(torch.cuda.current_stream().cuda_stream)
torch.cuda.synchronize()
out = y.cpu().numpy()
```

要点：

- **logger / runtime 要一直存活**，否则 engine 可能失效
- 绑定按**张量名字**，不按顺序
- 显存地址传 `data_ptr()`，TensorRT 不会帮你分配
- 异步执行后必须 `synchronize()`，否则读到的是未完成结果
- 第一次推理会初始化 CUDA kernel，计时前要先 warmup
- **Ultralytics 导出的 engine 不是纯 engine 字节**：文件开头是 4 字节小端 JSON 长度 + JSON 元数据（groundzero 是 1014 字节），后面才是 `ftrt`。直接 `read_bytes()` 去 deserialize 会报 `header.magicTag == kEXPECTED_MAGIC_TAG failed`，要先按长度跳过

## 3. 输出解码：[1,300,30]

这版模型是 **end2end**，输出已经做过 NMS，每行 30 列：

| 列 | 含义 |
| ---- | ---- |
| 0~3 | `x1, y1, x2, y2`（**xyxy**，640 坐标系） |
| 4 | 置信度 `score` |
| 5 | 类别索引 |
| 6~29 | 8 个关键点 × `(x, y, conf)` |

```python
for row in out[0]:
    x1, y1, x2, y2, score, cls = row[:6]
    if score < 0.25:
        continue
    kpts = row[6:].reshape(8, 3)
```

300 行里大部分是低分填充：groundzero 这张图只有 1 行 `score>0.25`。

> 普通 YOLOv8 检测模型输出是 `[1, 84, 8400]`，需要自己解码 + NMS；这版是 `[1, 300, 30]`，**不要再写 NMS**。

## 4. 逆映射：框和关键点都要做

```python
box = [(x1 - left) / r, (y1 - top) / r,
       (x2 - left) / r, (y2 - top) / r]

kpts[:, 0] = (kpts[:, 0] - left) / r
kpts[:, 1] = (kpts[:, 1] - top) / r
# 第三列 conf 不参与变换
```

漏掉关键点的逆映射，是这类任务最常见的 bug：框看起来对、点却飘在左上角。

## 5. 验证：先比数值，再看图

groundzero 第一张验证图：

```
预测框 [660.6, 2437.5, 1165.9, 3743.3]
标注框 [632.2, 2416.9, 1157.4, 3736.6]
中心偏差 18.5 / 13.7 px（原图 4096 宽，约 0.4%）
预测类别 Down，置信度 0.9136，标注类别 Down
```

按这个顺序验证：

1. 输出 shape 是否为 `[1,300,30]`
2. 高置信度行的 `cls` 是否等于标注类别
3. 框的数值是否接近标注（先不画图）
4. 画图看关键点是否落在物体角点上
5. 最后才看整体视觉效果

## 6. 性能：三个数字的区别

| 数字 | 含义 | groundzero 实测 |
| ---- | ---- | ---- |
| trtexec latency | **纯 GPU kernel**，预分配 buffer、无拷贝 | 1.59 ms |
| 脚本内 engine 段 | kernel + 每次 H2D/D2H + 显存分配 + synchronize | 3.79 ms |
| 端到端 | 预处理 + engine + 后处理 | 5.10 ms（196 FPS） |

**部署指标看端到端。** 优化顺序：

1. 预分配输入输出 tensor，循环里 `copy_`，避免反复分配
2. 预处理尽量用 GPU（避免 CPU resize 成为瓶颈）
3. 多流 / 批处理
4. 最后才考虑 FP16

## 7. 常见坑

| 现象 | 原因 |
| ---- | ---- |
| 框位置整体偏移 | 忘了减 `left/top`，或除以了错误的 `r` |
| 框对、关键点全错 | 只逆映射了框，没处理关键点 |
| 颜色异常 / 精度下降 | BGR 没转 RGB，或忘了 `/255` |
| `set_tensor_address` 报错 | 输入 shape 不对，或没用连续内存 |
| 结果是上一帧的 | 忘了 `torch.cuda.synchronize()` |
| 第一次特别慢 | CUDA kernel 初始化，计时前要 warmup |
| 画出第 8 个点但位置是 (0,0) | 关键点 `conf=0` 表示未标注，应跳过 |
| 自己写 NMS 后结果变少 | end2end 输出已 NMS，重复做会过度抑制 |
| `Serialization assertion header.magicTag == kEXPECTED_MAGIC_TAG failed` | Ultralytics 导出的 engine 前面多了 JSON 元数据头，按 4 字节长度跳过后再反序列化 |

## 8. 在全流程里的位置

前四步（数据 → 训练 → 导出 → build）见 [[N023 模型全流程总览 从数据到Orin部署]]；本篇是最后一步：

```bash
cd ~/deep_learning/groundzero

# ① 训练（已跑完，产物 runs/pose/train-4/weights/best.pt）
python new.py

# ② 导出 ONNX（产物 best.onnx）
python export_onnx.py

# ③ build FP32 engine（产物 best.engine）
trtexec --onnx=runs/pose/train-4/weights/best.onnx \
        --saveEngine=runs/pose/train-4/weights/best.engine \
        --memPoolSize=workspace:2048M

# ③' 或者一步导出 FP16 engine（TRT 11 走 ModelOpt AutoCast）
python export_engine.py

# ④ 推理验证（本篇）
python infer_engine.py
```

四步的产物、shape、耗时对照见 N023 的「一次真正跑通的链路」一节。

## 总结

engine 推理不是「加载模型就完事」，而是**一条自己负责前后处理的数据管线**：

1. 预处理：letterbox（记 `r` 和 `pad`）→ RGB → 归一化 → CHW → batch
2. 绑定：Runtime → deserialize → Context → `set_tensor_address`
3. 执行：`execute_async_v3` + `synchronize`
4. 解码：`[1,300,30]` 按列拆成框 / 分数 / 类别 / 关键点
5. 逆映射：框和关键点用同一组 `r`、`pad` 还原
6. 验证：先比数值，再看图；性能看端到端，不看单一 kernel
