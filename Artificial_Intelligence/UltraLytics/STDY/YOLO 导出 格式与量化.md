训练完的 `.pt` 不能直接上各种硬件，`model.export()` 把它转成 ONNX / TensorRT / CoreML 等目标格式。核心选择只有三个：**目标格式**、**输入尺寸/动态性**、**精度（FP32 / FP16 / INT8）**。

## 基本用法

```python
from ultralytics import YOLO

model = YOLO("yolo26n.pt")         # 官方模型
model = YOLO("path/to/best.pt")    # 自己训练的
model.export(format="onnx")        # 或 engine / openvino / coreml ...
```

CLI 同理：`yolo export model=yolo26n.pt format=onnx`。

## 常用导出参数

| 参数 | 默认 | 作用 |
| --- | --- | --- |
| `format` | `torchscript` | 目标格式 |
| `imgsz` | 640（官方 YOLO26 检测为 768） | 输入尺寸，可给 `(h, w)` |
| `quantize` | 未设置 = FP32 | `16` = FP16；`8` = INT8；`"w8a16"` / `"w8a32"` 混合精度 |
| `dynamic` | `False` | 允许动态输入尺寸（ONNX / TensorRT / OpenVINO 等） |
| `simplify` | `True` | 用 `onnxslim` 简化 ONNX 图 |
| `opset` | 最新支持版本 | ONNX opset |
| `workspace` | 自动 | TensorRT 最大工作区（GiB） |
| `nms` | `None` | `None` 输出原始预测由外部 NMS；`True` 嵌入 NMS；`False` 用无 NMS 头 |
| `conf` / `iou` | 0.25 / 0.7 | 导出时内嵌 NMS 的阈值 |
| `max_det` | 300 | 最多保留检测数 |
| `agnostic_nms` | `False` | 类别无关 NMS |
| `batch` | 1 | 批量大小 |
| `device` | 自动 | `0` / `cpu` / `mps` / `npu` / `dla:0` |
| `data` / `split` / `fraction` | - / `val` / 1.0 | INT8 校准数据 |

**旧参数**：`half=True` → `quantize=16`，`int8=True` → `quantize=8`，仍可用但会警告。

## 主要格式

| 格式 | `format` | 典型用途 | 精度支持 |
| --- | --- | --- | --- |
| ONNX | `onnx` | 跨框架交换、ORT 部署 | FP32 / FP16 / INT8 |
| TensorRT | `engine` | NVIDIA GPU 推理，最高约 5× 加速 | FP32 / FP16 / INT8 |
| OpenVINO | `openvino` | Intel CPU/GPU | FP32 / FP16 / INT8 |
| TorchScript | `torchscript` | PyTorch 内部部署 | FP32 / FP16（FP16 需 GPU） |
| CoreML | `coreml` | Apple 设备 | FP32 / FP16 / INT8 / W8A16 |
| TF SavedModel | `saved_model` | TF 生态 | FP32 / INT8 |
| LiteRT / TFLite | `litert` | Android / 边缘 | FP32 / INT8 / W8A16 / W8A32 |
| NCNN | `ncnn` | 移动端 / 嵌入式 | FP32 / FP16 |
| RKNN | `rknn` | Rockchip 芯片 | 按芯片 FP16 或 INT8 |
| Edge TPU / IMX500 / Hailo / DEEPX | 各自 | 专用加速器 | 强制 INT8 |

完整列表见原文档；Edge TPU、IMX500、Hailo、DEEPX、AMD Xilinx 等硬件**必须 INT8**，未指定时会自动启用。

## 量化

### 三种精度

| 值 | 含义 |
| --- | --- |
| `32` / 未设置 | FP32 |
| `16` / `"fp16"` | FP16 权重与激活 |
| `8` / `"int8"` / `"w8a8"` | INT8 权重与激活 |
| `"w8a16"` | INT8 权重 + 16 位激活（CoreML / LiteRT / QNN） |
| `"w8a32"` | INT8 权重 + FP32 激活（LiteRT 动态 INT8，无需校准） |

INT8 需要**有代表性的校准数据**：

```python
model.export(format="engine", quantize=8, data="coco8.yaml", fraction=0.5)
```

`fraction` 控制用多少数据校准（比例或图片数）。

### PTQ vs QAT

- **PTQ（训练后量化）**：校准一遍确定数值范围，最简单，但大模型掉点明显。
- **QAT（量化感知训练）**：微调时插入伪量化，让权重适应 INT8，再导出。

```python
model.train(data="coco.yaml", quantize=8, epochs=5, batch=64,
            optimizer="AdamW", lr0=1e-5, lrf=0.1,
            warmup_epochs=0.5, cos_lr=True, mosaic=0.0)
model.export(format="engine", quantize=8)   # 数值范围随 checkpoint 保存，无需再校准
```

COCO val2017、TensorRT 10.16、`imgsz=640` 的 mAP50-95：

| 模型 | FP32 | PTQ INT8 | QAT INT8 |
| --- | --- | --- | --- |
| yolo26n | 0.4032 | 0.3934 | 0.3935 |
| yolo26s | 0.4794 | 0.4412 | 0.4711 |
| yolo26m | 0.5269 | 0.4696 | 0.5137 |
| yolo26l | 0.5440 | 0.4889 | 0.5307 |
| yolo26x | 0.5701 | 0.5138 | 0.5527 |

结论：小模型（n）PTQ 已经很好，QAT 几乎没有收益；中大型模型 QAT 能追回 0.030~0.044 mAP，但仍有 0.008~0.017 的损失。换数据集/格式/TensorRT 版本要重新测。

QAT 相关注意：

- 需要 NVIDIA TensorRT Model Optimizer，首次使用自动安装；加载 QAT checkpoint 时也必须装。
- QAT 模型导出要用 `compile=False`（ModelOpt 不支持 `torch.compile`）。
- 检测头最后的输出卷积故意保留浮点，TensorRT 对未量化层启用 FP16 混合精度，减少掉点。

## 常见坑

- **自动装依赖**：导出缺包时会现场 `pip/uv/apt install`。容器/CI 里设 `YOLO_AUTOINSTALL=False`，否则环境会被改。
- **`nms` 三态**：`None` 不是“关闭 NMS”，而是“把原始输出交给你，外部自己做”；`True` 才是把 NMS 嵌进模型。
- **动态尺寸**：`dynamic=True` 更灵活，但某些后端会失去部分优化；固定尺寸性能更好。
- **INT8 必须校准**：没有 `data` 时 Ultralytics 会退回任务默认数据集，分布不匹配会掉点。
- **QAT 训练期分数不可信**：伪量化下的验证结果不等于部署精度，必须导出后再测。

## 总结

导出 = 选格式 + 定尺寸 + 定量化。ONNX 适合跨平台与 TensorRT 中间格式；`engine` 是 NVIDIA GPU 上最快；INT8 要先 PTQ 看掉点，大模型再考虑 QAT。参数里最常动的是 `format`、`imgsz`、`quantize`、`dynamic`、`nms`。
