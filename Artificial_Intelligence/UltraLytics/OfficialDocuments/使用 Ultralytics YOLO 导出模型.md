![Ultralytics YOLO ecosystem and integrations](https://cdn.ul.run/i/f874ab850f33f361d01a01e9a8c98655.avif)

## 简介

训练模型的最终目标是将其部署到实际应用中。Ultralytics YOLO26 的导出模式提供多种灵活选项，可将训练好的模型导出为不同格式，以便部署到各种平台和设备。本指南将全面介绍模型导出的细节，说明如何实现最大的兼容性和性能。

查看 [尚未发布的 YOLO27 预览版](https://docs.ultralytics.com/zh/models/yolo27#supported-tasks-and-modes) ，了解计划支持的导出功能。

<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" src="https://player.bilibili.com/player.html?bvid=BV1qTAUzXEto&amp;autoplay=0" title="YouTube video player" frameborder="0"></iframe>  
**观看：** 如何将 Ultralytics YOLO26 导出为不同格式以供部署 | ONNX、TensorRT、CoreML 🚀

## 为什么选择 YOLO26 的导出模式？

- **灵活性：** 可导出为多种格式，包括 [ONNX](https://docs.ultralytics.com/zh/integrations/onnx) 、 [TensorRT](https://docs.ultralytics.com/zh/integrations/tensorrt) 、 [CoreML](https://docs.ultralytics.com/zh/integrations/coreml) 等。
- **性能：** 使用 TensorRT，GPU 速度最高可提升 5 倍；使用 ONNX 或 [OpenVINO](https://docs.ultralytics.com/zh/integrations/openvino) ，CPU 速度最高可提升 3 倍。
- **兼容性：** 让模型能够广泛部署到各种软硬件环境中。
- **易用性：** 通过简单的 CLI 和 Python API，快速轻松地导出模型。

## 使用示例

将 YOLO26n 模型导出为 ONNX 或 TensorRT 等其他格式。导出参数的完整列表请参见下方的“参数”部分。

示例

```
from ultralytics import YOLO

# 加载模型
model = YOLO("yolo26n.pt")  # 加载官方模型
model = YOLO("path/to/best.pt")  # 加载自定义训练的模型

# 导出模型
model.export(format="onnx")
```

## 参数

此表详细列出了将 YOLO 模型导出为不同格式时可用的配置和选项。这些设置对于优化导出模型在各种平台和环境中的性能、大小和兼容性至关重要。正确配置可确保模型以最佳效率满足目标应用的部署需求。

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `format` | `str` | `'torchscript'` | 导出模型的目标格式，例如 `'onnx'` 、 `'torchscript'` 、 `'engine'` （TensorRT）或其他格式。每种格式都支持不同的 [部署环境](https://docs.ultralytics.com/modes/export) 。 |
| `name` | `str` | `None` | 需要指定目标硬件的格式所用的硬件目标名称：Hailo 架构（ `'hailo8'` 、 `'hailo8l'` 、 `'hailo10h'` 、 `'hailo15h'` 、 `'hailo15l'` ；默认为 `'hailo8l'` ）、Rockchip RKNN 芯片（默认为 `'rk3588'` ）、Huawei Ascend SoC（CANN `--soc_version` ；默认为 `'Ascend310B4'` ）、Qualcomm QNN HTP 目标（默认为 `'73'` ），或 AMD Xilinx Versal AI Edge Series Gen 2 设备（默认为 `'ve2-xc2ve3858'` ，即 VEK385 评估套件）。这与其他模式使用的 `project` / `name` 运行命名组合不同。 |
| `imgsz` | `int` 或 `tuple` | `640` | 模型输入的目标图像尺寸。可以是表示正方形图像的整数（例如， `640` 表示 640×640），也可以是表示特定尺寸的元组 `(height, width)` 。如果未传入，导出时会沿用加载的检查点中记录的训练尺寸：官方 YOLO26 检查点记录的尺寸分别为：检测任务 `768` ，分类任务 `224` ，OBB 任务 `1024` ，其他任务 `640` ；微调模型则记录训练时使用的 `imgsz` 。根据 YAML 构建的模型没有记录训练尺寸，因此使用 `640` 。 |
| `optimize` | `bool` | `False` | 为 DEEPX 启用更高等级的编译器优化，以降低推理延迟，但会增加编译时间。 |
| `quantize` | `int` 或 `str` | `None` | 量化精度： `16` （FP16，可减小模型大小，并可能加快受支持硬件上的推理速度）或 `8` （INT8/PTQ，可进一步压缩模型，且 [准确率](https://www.ultralytics.com/glossary/accuracy) 损失极小，主要用于 [边缘设备](https://www.ultralytics.com/blog/understanding-the-real-world-applications-of-edge-ai) ；需要校准 `data` / `fraction` ）； `32` /未设置表示 FP32。使用 `quantize=8` 训练的检查点始终导出为 INT8： `onnx` 和 `engine` 会使用检查点自带的数值范围进行导出，无需校准；不接受其他格式或精度。 `'w8a8'` 和 `'w16a16'` 分别是 `8` 和 `16` 的别名；混合精度 `'w8a16'` （INT8 权重与 16 位激活值：CoreML、LiteRT、QNN）和 `'w8a32'` （动态 INT8：LiteRT）仅受这些格式支持。此参数替代已弃用的 `half` / `int8` 标志（ `half=True` → `16` ， `int8=True` → `8` ；仍可使用，但会显示弃用警告）。只能使用目标格式支持的精度（见下文）。 |
| `dynamic` | `bool` | `False` | 允许 TorchScript、ONNX、OpenVINO、TensorRT、CoreML 和 MNN 导出采用动态输入尺寸，提高处理不同图像尺寸时的灵活性。 |
| `simplify` | `bool` | `True` | 对于会构建 ONNX 中间图的导出，使用 `onnxslim` 简化该图（参见 [导出格式](https://docs.ultralytics.com/modes/export) ），可能提高性能并改善与推理引擎的兼容性。 |
| `opset` | `int` | `None` | 指定会构建 ONNX 图的导出所使用的 ONNX opset 版本（参见 [导出格式](https://docs.ultralytics.com/modes/export) ），以兼容不同的 [ONNX](https://docs.ultralytics.com/integrations/onnx) 解析器和运行时。如果未设置，则使用最新的受支持版本。 |
| `workspace` | `float` 或 `None` | `None` | 设置 [TensorRT](https://docs.ultralytics.com/integrations/tensorrt) 优化的最大工作区大小（单位为 GiB），以平衡内存使用量和性能。使用 `None` 可让 TensorRT 自动分配工作区，最大不超过设备上限。 |
| `nms` | `bool` ，可选 | `None` | `None` 导出原始一对多预测结果，以便外部执行 NMS； `True` 会在受支持时嵌入 NMS； `False` 会在可用时选择无 NMS 检测头。CoreML 嵌入式 NMS 支持静态形状的 detect、segment 和 pose。详情请参阅 [端到端检测指南](https://docs.ultralytics.com/zh/guides/end2end-detection) 。 |
| `conf` | `float` | `None` | 用于所有导出时生成 NMS 的置信度阈值： `nms=True` 导出、Hailo 的非端到端 detect 导出，以及 IMX 的 detect、pose 和 segment 导出；后者会在内部强制使用 `nms=True` 。未设置时默认为 `0.25` 。 |
| `iou` | `float` | `0.7` | 用于所有导出时生成 NMS 的 [IoU](https://www.ultralytics.com/glossary/intersection-over-union-iou) 阈值： `nms=True` 导出、Hailo 的非端到端 detect 导出，以及 IMX 的 detect、pose 和 segment 导出；后者会在内部强制使用 `nms=True` 。 |
| `max_det` | `int` | `300` | 导出模型输出中保留的最大检测数量。适用于所有格式的 `nms=True` 导出，但 CoreML 检测除外，其原生 NMS 流程没有检测数量上限；也适用于无 NMS 的端到端检测导出（YOLO26、YOLOv10，上限限制为可用锚点数量）以及 IMX 的 detect、pose 和 segment 导出。 |
| `agnostic_nms` | `bool` | `False` | 在通过标准 `nms=True` 流程生成导出时的 NMS（包括 CoreML 自带的 NMS 阶段）中启用类别无关 NMS，抑制不同类别之间得分较低且重叠的框，而不只是同一类别内的框。Hailo 或 IMX 自行生成的 NMS 配置不支持此选项，因此不会采用该设置，仍会按类别进行处理。此选项也会应用于无 NMS 的端到端导出（YOLO26、YOLOv10），但仅用于防止同一检测结果带有多个类别标签（IoU=1.0 的重复项），不会根据 IoU 阈值抑制不同的框。 |
| `batch` | `int` | `1` | 指定导出模型的批量推理大小，或导出模型在 `predict` 模式下并发处理的最大图像数量。导出参数中不包含 `batch` 的格式（Edge TPU、IMX500、DEEPX、Hailo、AMD Xilinx）会以批量大小 1 导出，并拒绝其他值。 |
| `device` | `str` | `None` | 指定导出设备：GPU（ `device=0` ）、CPU（ `device=cpu` ）、适用于 Apple silicon 的 MPS（ `device=mps` ）、Huawei Ascend NPU（ `device=npu` 或 `device=npu:0` ），或适用于 NVIDIA Jetson 的 DLA（ `device=dla:0` 或 `device=dla:1` ）。TensorRT 导出会自动使用 GPU，但 TensorRT 11 不支持 DLA。 |
| `verbose` | `bool` | `False` | 在 `format='engine'` 导出期间，将 TensorRT 构建器日志级别提高到 VERBOSE。其他导出格式会忽略此设置。 |
| `data` | `str` | `None` | [数据集](https://docs.ultralytics.com/datasets) YAML 文件的路径，是 INT8 量化校准所必需的；分类任务则使用数据集目录或内置数据集名称。如果启用 INT8 但未指定该路径，Ultralytics 会在需要时选择特定任务的校准数据集，或退回到该模型任务的默认数据集。使用 `quantize=8` 训练的检查点自带 INT8 数值范围，无需校准数据。 |
| `split` | `str` | `'val'` | 用于从 `data` 构建 INT8 量化校准数据加载器的数据集划分（ `'train'` 、 `'val'` 或 `'test'` ）。 |
| `fraction` | `float` 、 `int` 或 `list` | `1.0` | 用于 INT8 校准的数据集子集：比例、图像数量或 `[train, val, test]` 值。 `1` 表示完整数据划分，大于 `1` 的整数表示图像数量；只有可选的 test 条目接受 `0` / `0.0` 表示不使用任何数据。两项列表会保留完整的 `test` 。 |

调整这些参数可以根据具体需求自定义导出流程，例如部署环境、硬件限制和性能目标。选择合适的格式和设置，对于在模型大小、速度和 [准确率](https://www.ultralytics.com/glossary/accuracy) 之间实现最佳平衡至关重要。

## 导出格式

下表列出了 YOLO26 可用的导出格式。你可以使用 `format` 参数导出为任意格式，例如 `format='onnx'` 或 `format='engine'` 。导出模型后，你可以直接对其进行预测或验证，例如 `yolo predict model=yolo26n.onnx` 。导出完成后，系统会显示适用于你模型的用法示例。你也可以直接在浏览器中通过 [Ultralytics Platform](https://docs.ultralytics.com/zh/platform/train/models#export-model) 导出模型，无需进行任何本地设置。

| 格式 | `format` 参数 | 模型 | 元数据 | 参数 |
| --- | --- | --- | --- | --- |
| [PyTorch](https://pytorch.org/) | \- | `yolo26n.pt` | ✅ | \- |
| [TorchScript](https://docs.ultralytics.com/zh/integrations/torchscript) | `torchscript` | `yolo26n.torchscript` | ✅ | `imgsz`, `quantize`, `dynamic`, `nms`, `batch`, `device` |
| [ONNX](https://docs.ultralytics.com/zh/integrations/onnx) | `onnx` | `yolo26n.onnx` | ✅ | `imgsz`, `quantize`, `dynamic`, `simplify`, `opset`, `nms`, `batch`, `data`, `fraction`, `device` |
| [OpenVINO](https://docs.ultralytics.com/zh/integrations/openvino) | `openvino` | `yolo26n_openvino_model/` | ✅ | `imgsz`, `quantize`, `dynamic`, `nms`, `batch`, `data`, `fraction`, `device` |
| [TensorRT](https://docs.ultralytics.com/zh/integrations/tensorrt) | `engine` | `yolo26n.engine` | ✅ | `imgsz`, `quantize`, `dynamic`, `simplify`, `opset`, `workspace`, `nms`, `batch`, `data`, `fraction`, `device` |
| [CoreML](https://docs.ultralytics.com/zh/integrations/coreml) | `coreml` | `yolo26n.mlpackage` | ✅ | `imgsz`, `dynamic`, `quantize`, `nms`, `batch`, `device` |
| [Apple Core AI](https://docs.ultralytics.com/zh/integrations/coreai) | `coreai` | `yolo26n.aimodel` | ✅ | `imgsz`, `batch`, `quantize` |
| [TF SavedModel](https://docs.ultralytics.com/zh/integrations/tf-savedmodel) | `saved_model` | `yolo26n_saved_model/` | ✅ | `imgsz`, `quantize`, `opset`, `nms`, `batch`, `data`, `fraction`, `device` |
| [TF GraphDef](https://docs.ultralytics.com/zh/integrations/tf-graphdef) | `pb` | `yolo26n.pb` | ❌ | `imgsz`, `opset`, `batch`, `device` |
| [TF Edge TPU](https://docs.ultralytics.com/zh/integrations/edge-tpu) | `edgetpu` | `yolo26n_edgetpu.tflite` | ✅ | `imgsz`, `quantize`, `opset`, `data`, `fraction`, `device` |
| [LiteRT](https://docs.ultralytics.com/zh/integrations/litert) | `litert` | `yolo26n.tflite` | ✅ | `imgsz`, `quantize`, `batch`, `data`, `fraction`, `device` |
| [PaddlePaddle](https://docs.ultralytics.com/zh/integrations/paddlepaddle) | `paddle` | `yolo26n_paddle_model/` | ✅ | `imgsz`, `batch`, `device` |
| [MNN](https://docs.ultralytics.com/zh/integrations/mnn) | `mnn` | `yolo26n.mnn` | ✅ | `imgsz`, `batch`, `dynamic`, `quantize`, `simplify`, `opset`, `nms`, `device` |
| [NCNN](https://docs.ultralytics.com/zh/integrations/ncnn) | `ncnn` | `yolo26n_ncnn_model/` | ✅ | `imgsz`, `quantize`, `batch`, `device` |
| [IMX500](https://docs.ultralytics.com/zh/integrations/sony-imx500) | `imx` | `yolo11n_imx_model/` | ✅ | `imgsz`, `quantize`, `data`, `fraction`, `nms`, `device` |
| [RKNN](https://docs.ultralytics.com/zh/integrations/rockchip-rknn) | `rknn` | `yolo26n_rknn_model/` | ✅ | `imgsz`, `batch`, `name`, `quantize`, `simplify`, `opset`, `data`, `fraction`, `device` |
| [ExecuTorch](https://docs.ultralytics.com/zh/integrations/executorch) | `executorch` | `yolo26n_executorch_model/` | ✅ | `imgsz`, `batch`, `device` |
| [Axelera](https://docs.ultralytics.com/zh/integrations/axelera) | `axelera` | `yolo26n_axelera_model/` | ✅ | `imgsz`, `batch`, `quantize`, `data`, `fraction`, `device` |
| [DEEPX](https://docs.ultralytics.com/zh/integrations/deepx) | `deepx` | `yolo26n_deepx_model/` | ✅ | `imgsz`, `quantize`, `simplify`, `opset`, `data`, `optimize`, `device` |
| [Qualcomm QNN](https://docs.ultralytics.com/zh/integrations/qnn) | `qnn` | `yolo26n_qnn.onnx` | ✅ | `imgsz`, `batch`, `name`, `quantize`, `simplify`, `opset`, `data`, `fraction`, `device` |
| [Hailo](https://docs.ultralytics.com/zh/integrations/hailo) | `hailo` | `yolo26n_hailo_model/` | ✅ | `imgsz`, `name`, `quantize`, `data`, `fraction`, `simplify`, `conf`, `iou`, `device` |
| [Huawei Ascend](https://docs.ultralytics.com/zh/integrations/ascend) | `ascend` | `yolo26n_ascend_model/` | ✅ | `imgsz`, `batch`, `name`, `quantize`, `opset`, `simplify`, `nms`, `device` |
| [AMD Xilinx](https://docs.ultralytics.com/zh/integrations/xilinx) | `xilinx` | `yolo26n_xilinx_model/` | ✅ | `imgsz`, `name`, `quantize`, `data`, `fraction`, `opset`, `simplify`, `device` |

`nms=None` 默认输出原始结果，以供外部 NMS 使用。设置 `nms=False` 可选择可用的无 NMS 检测头；不支持的格式会回退到其原生输出路径。上方的 `nms` 条目表示可以通过 `nms=True` 嵌入 NMS 的格式。

自动安装导出依赖项

大多数格式都需要未随 `ultralytics` 一起安装的软件包。如果缺少某个软件包，导出时会在运行阶段通过 `uv` 或 `pip` 安装；在 Linux 上，还会通过 `apt` 安装 Java 等系统软件包（例如 IMX 所需的软件包）。Edge TPU 编译器会在不使用 `apt` 或 `sudo` 的情况下下载。若要保持环境不变（例如在容器镜像、CI 作业或生产服务中），请设置 `YOLO_AUTOINSTALL=False` 。此时，导出仍会检查缺少的软件包并报告，但不会更改环境；在安装这些软件包之前，导出会失败。

```
export YOLO_AUTOINSTALL=False
```

## 量化选项

使用 `quantize` 参数指定导出精度。字符串值不区分大小写，Ultralytics 会在导出前将可接受的别名规范化：

| 请求值 | 规范值 | 含义 |
| --- | --- | --- |
| `8`, `"8"`, `"int8"`, `"w8a8"` | `8` | INT8 权重和激活值 |
| `16`, `"16"`, `"fp16"`, `"w16a16"` | `16` | FP16 权重和激活值 |
| `32`, `"32"`, `"fp32"`, `"w32a32"` | `32` | 导出为 FP32；与未设置时相同，但 CoreML NMS ML Programs 默认使用 FP16 |
| `"w8a16"` | `"w8a16"` | INT8 权重搭配 16 位激活值（FP16；LiteRT 中为 INT16） |
| `"w8a32"` | `"w8a32"` | INT8 权重搭配 FP32 激活值（LiteRT 动态 INT8，无需校准） |

仍接受旧版 `half=True` 和 `int8=True` 标志，但会发出弃用警告，并转发到 `quantize=16` 和 `quantize=8` 。

并非每种导出格式都支持所有精度。显式请求 `quantize` 时，要么生成相应精度的模型，要么在导出前失败：

| 格式 | FP32（ `32` /未设置） | FP16（ `16` ） | INT8（ `8` ） | W8A16（ `"w8a16"` ） | 备注 |
| --- | --- | --- | --- | --- | --- |
| PyTorch | ✅ | 不适用 | 不适用 | 不适用 | 原生训练/检查点格式。 |
| TorchScript | ✅ | ✅ 仅限 GPU | ❌ | ❌ | 导出 FP16 TorchScript 需要 `device=0` ；CPU 导出为 FP32。 |
| ONNX | ✅ | ✅ | ✅ | ❌ | INT8 使用 ONNX Runtime 静态量化和校准数据。 |
| OpenVINO | ✅ | ✅ | ✅ | ❌ | INT8 使用 NNCF 训练后量化。 |
| TensorRT | ✅ | ✅ | ✅ | ❌ | INT8 需要有代表性的校准数据。 |
| CoreML | ✅¹ | ✅ | ✅ | ✅ | CoreML INT8 是权重量化；W8A16 使用 INT8 权重和 FP16 激活值。¹未设置时，NMS ML Programs 默认使用 FP16，分割/姿态 `nms=True` 导出始终使用 FP16。 |
| Core AI | ✅ | ✅ | ❌ | ❌ | 默认使用 FP32；也可以通过 `quantize=16` 指定 FP16 `.aimodel` 资产；不支持 INT8 路径。 |
| TF SavedModel | ✅ | ❌ | ✅ | ❌ | INT8 导出使用 TensorFlow 校准。 |
| TF GraphDef | ✅ | ❌ | ❌ | ❌ | 导出时不转换精度。 |
| Edge TPU | ❌ | ❌ | ✅ 自动 | ❌ | Edge TPU 必须使用 INT8；未设置时会自动启用。 |
| LiteRT | ✅ | ❌ | ✅ | ✅ | 静态 INT8（ `8` ）和 `"w8a16"` （int8 权重 + **int16** 激活值）使用校准数据；此外还支持 `"w8a32"` 动态 INT8（无需校准）。 `quantize=16` 并非单独的导出格式；FP32 模型会在运行时通过 GPU delegate 以 FP16 运行。 |
| PaddlePaddle | ✅ | ❌ | ❌ | ❌ | 导出时不转换精度。 |
| MNN | ✅ | ✅ | ✅ | ❌ | INT8 是通过 MNN 转换进行的权重量化。 |
| NCNN | ✅ | ✅ | ❌ | ❌ | 移动端/嵌入式运行时格式。 |
| IMX500 | ❌ | ❌ | ✅ 自动 | ❌ | IMX500 需要量化；未设置时会自动启用 INT8。 |
| RKNN | ❌ | ✅ 取决于芯片 | ✅ | ❌ | RK3588/RK3576/RK3566/RK3568/RK3562/RK2118/RV1126B 支持 FP16 或 INT8；RV1103/RV1106 系列仅支持 INT8。 |
| ExecuTorch | ✅ | ❌ | ❌ | ❌ | 导出时不转换精度。 |
| Axelera | ❌ | ❌ | ✅ 自动 | ❌ | Axelera 导出必须使用 INT8；未设置时会自动启用。 |
| DEEPX | ❌ | ❌ | ✅ 自动 | ❌ | DEEPX 导出必须使用 INT8；未设置时会自动启用。 |
| Qualcomm QNN | ❌ | ❌ | ❌ | ✅ 自动 | QNN HTP 导出固定使用 INT8 权重和 16 位激活值。 |
| Hailo | ❌ | ❌ | ✅ 自动 | ❌ | Hailo 导出必须使用 INT8；未设置时会自动启用。 |
| Huawei Ascend | ❌ | ✅ 自动 | ❌ | ❌ | Ascend AI Core 卷积仅接受 FP16/INT8 输入，因此 ATC 会编译为 FP16；未设置时会自动启用。 |
| AMD Xilinx | ❌ | ❌ | ✅ 自动 | ❌ | AMD Xilinx 导出需要 Vitis AI INT8（ `VINT8` ）；如果未设置，此选项会自动启用。 |

对于 INT8 和 W8A16 导出，请使用 `data` 提供有代表性的校准数据，例如 `data="coco8.yaml"` ，除非目标集成文档说明了默认行为或自动启用行为。LiteRT `"w8a32"` （动态 INT8）方案无需校准数据。

### 量化感知训练

上面的 INT8 导出采用训练后量化（PTQ）：通过对 `data` 进行一次校准来确定数值范围。量化感知训练（QAT）则通过在微调过程中加入伪量化，学习能够适应 INT8 的权重，从而恢复仅靠校准会损失的精度。将 `quantize=8` 传递给 `train` ，以微调预训练检查点，然后像往常一样导出：

示例

```
from ultralytics import YOLO

model = YOLO("yolo26n.pt")
model.train(
    data="coco.yaml",
    quantize=8,
    epochs=5,
    batch=64,
    optimizer="AdamW",
    lr0=0.00001,
    lrf=0.1,
    warmup_epochs=0.5,
    cos_lr=True,
    mosaic=0.0,
)
model.export(format="engine", quantize=8)  # 数值范围会随检查点保存，无需校准数据
```

微调预训练检查点时请使用较小的学习率。QAT 初期可能会降低精度，而它相较于训练后量化的优势取决于模型、数据集和训练预算。请将导出的模型与原始检查点和训练后量化导出模型都进行验证；训练期间的伪量化得分并不能证明模型在部署时的精度。

QAT 是否值得采用，取决于导出后端自身的校准对模型的处理效果。下方数值是在 COCO val2017 上测得的 mAP50-95，使用 TensorRT 10.16 引擎和 `imgsz=640` ，批次大小为 1；每个 QAT 检查点均使用 `epochs=20 patience=3` 训练：

| 模型 | FP32 引擎 | PTQ INT8 引擎 | QAT INT8 引擎 |
| --- | --- | --- | --- |
| `yolo26n` | 0.4032 | 0.3934 | 0.3935 |
| `yolo26s` | 0.4794 | 0.4412 | 0.4711 |
| `yolo26m` | 0.5269 | 0.4696 | 0.5137 |
| `yolo26l` | 0.5440 | 0.4889 | 0.5307 |
| `yolo26x` | 0.5701 | 0.5138 | 0.5527 |

在所有模型规模中，与 FP32 相比，QAT 会损失 0.008 到 0.017 mAP50-95；而训练后量化在 `yolo26n` 上损失 0.010，在较大模型上损失 0.038 到 0.057。因此，在校准效果本就很好的最小模型上，QAT 几乎没有收益；在其他模型上则能提升 0.030 到 0.044。换用其他数据集、导出格式或 TensorRT 版本时，结果可能不同，请自行测量。

QAT 模型需要 `compile=False` ；ModelOpt 的量化模块不支持 `torch.compile` 。

为减少 INT8 精度损失，检测头最后的输出卷积会特意保留为浮点运算；TensorRT 会为未量化层启用 FP16 混合精度。QAT 通过 [NVIDIA TensorRT Model Optimizer](https://github.com/NVIDIA/TensorRT-Model-Optimizer) 运行，该工具会在首次使用时自动安装，加载生成的检查点时也必须安装该工具。数值范围会随检查点保存， `onnx` 和 `engine` 导出会将其写入 Q/DQ 节点；其他格式则读取校准数据，并拒绝 QAT 检查点。

## 接下来做什么

查阅目标部署平台的集成指南，了解如何运行导出的模型—— [ONNX](https://docs.ultralytics.com/zh/integrations/onnx) 、 [TensorRT](https://docs.ultralytics.com/zh/integrations/tensorrt) 、 [CoreML](https://docs.ultralytics.com/zh/integrations/coreml) 等指南均列在 [完整集成列表](https://docs.ultralytics.com/zh/integrations) 中。

## 常见问题

- ### 如何将 YOLO26 模型导出为 ONNX 格式？
	使用 Ultralytics 将 YOLO26 模型导出为 ONNX 格式非常简单。你可以通过 Python 或 CLI 导出模型。
	示例
	```
	from ultralytics import YOLO
	# 加载模型
	model = YOLO("yolo26n.pt")  # 加载官方模型
	model = YOLO("path/to/best.pt")  # 加载自定义训练的模型
	# 导出模型
	model.export(format="onnx")
	```
	如需了解有关此流程的更多详情，包括处理不同输入尺寸等高级选项，请参阅 [ONNX 集成指南](https://docs.ultralytics.com/zh/integrations/onnx) 。
- ### 使用 TensorRT 导出模型有哪些优势？
	使用 TensorRT 导出模型可以显著提升性能。导出为 TensorRT 的 YOLO26 模型可实现最高 5 倍的 GPU 加速，因此非常适合实时推理应用。
	- **灵活性：** 针对特定硬件配置优化模型。
	- **速度：** 通过高级优化实现更快的推理。
	- **兼容性：** 与 NVIDIA 硬件无缝集成。
	如需详细了解如何集成 TensorRT，请参阅 [TensorRT 集成指南](https://docs.ultralytics.com/zh/integrations/tensorrt) 。
- ### 导出 YOLO26 模型时，如何启用 INT8 量化？
	INT8 量化是压缩模型并加快推理速度的好方法，尤其适用于边缘设备。启用 INT8 量化的方法如下：
	示例
	```
	from ultralytics import YOLO
	model = YOLO("yolo26n.pt")  # 加载模型
	model.export(format="onnx", quantize=8, data="coco8.yaml")
	```
	INT8 量化可应用于 [ONNX](https://docs.ultralytics.com/zh/integrations/onnx) 、 [TensorRT](https://docs.ultralytics.com/zh/integrations/tensorrt) 、 [OpenVINO](https://docs.ultralytics.com/zh/integrations/openvino) 、 [CoreML](https://docs.ultralytics.com/zh/integrations/coreml) 、 [Rockchip RKNN](https://docs.ultralytics.com/zh/integrations/rockchip-rknn) 和 [AMD Xilinx](https://docs.ultralytics.com/zh/integrations/xilinx) 等格式。为获得最佳量化效果，请使用 `data` 参数提供一个有代表性的 [数据集](https://docs.ultralytics.com/zh/datasets) 。有关可接受的 `quantize` 值和支持的格式，请参阅 [量化选项](#quantization-options) 。
- ### 导出模型时，为什么动态输入尺寸很重要？
	动态输入尺寸使导出的模型能够处理不同的图像尺寸，从而提升灵活性，并针对不同用例优化处理效率。导出为 [ONNX](https://docs.ultralytics.com/zh/integrations/onnx) 或 [TensorRT](https://docs.ultralytics.com/zh/integrations/tensorrt) 等格式时，启用动态输入尺寸可确保模型能够无缝适配不同的输入形状。
	导出时使用 `dynamic=True` 标志即可启用此功能：
	示例
	```
	from ultralytics import YOLO
	model = YOLO("yolo26n.pt")
	model.export(format="onnx", dynamic=True)
	```
	动态输入尺寸特别适用于输入尺寸可能变化的应用，例如视频处理，或处理来自不同来源的图像。
- ### 为什么导出模型在非正方形图像上的预测结果与 PyTorch 不同？
	PyTorch 模型和动态导出默认使用 [最小矩形填充](https://docs.ultralytics.com/zh/modes/predict#fixed-shape-vs-minimum-rectangle-rect) ，而静态导出会填充到完整的 `imgsz` ，因此置信度阈值附近的检测结果可能不同。若要匹配静态导出，请使用 `rect=False` 进行原生推理；也可以在支持的情况下使用 `dynamic=True` 导出。
- ### 优化模型性能时，需要重点考虑哪些导出参数？
	理解并配置导出参数对于优化模型性能至关重要：
	- **`format:`** 导出模型的目标格式（例如 `onnx` 、 `torchscript` 、 `saved_model` ）。
	- **`imgsz:`** 模型输入所需的图像尺寸（例如 `640` 或 `(height, width)` ）。
	- **`quantize:`** 量化精度，例如 `8` / `"int8"` 、 `16` / `"fp16"` 、 `32` / `"fp32"` ，或支持格式中的混合权重/激活值方案 `"w8a16"` 和 `"w8a32"` （LiteRT 动态 INT8）。请参阅 [量化选项](#quantization-options) 。
	- **`dynamic:`** 在支持动态形状的格式（如 ONNX、OpenVINO 和 TensorRT）中接受可变输入尺寸。
	- **`nms:`** 用于选择原始输出（外部 NMS， `None` ）、内嵌 NMS（ `True` ）或无 NMS 检测头（ `False` ）。
	- **`device:`** 导出期间用于追踪模型的设备，例如用于第一块 CUDA GPU 的 `cpu` 或 `0` ；FP16 TorchScript 需要 GPU。
	若要部署到特定硬件平台，可考虑使用专用导出格式，例如用于 NVIDIA GPU 的 [TensorRT](https://docs.ultralytics.com/zh/integrations/tensorrt) 、用于 Apple 设备的 [CoreML](https://docs.ultralytics.com/zh/integrations/coreml) ，或用于 Google Coral 设备的 [Edge TPU](https://docs.ultralytics.com/zh/integrations/edge-tpu) 。
- ### 导出后的 YOLO 模型中，输出张量代表什么？
	将 YOLO 模型导出为 ONNX 或 TensorRT 等格式时，输出张量结构取决于模型任务。了解这些输出对于实现自定义推理至关重要。
	对于使用 `nms=False` 导出的 **YOLO26 检测模型** （例如 `yolo26n.pt` ），受支持的格式会生成无 NMS 输出，其形状类似 `(batch_size, max_detections, 6)` ，包含 `[x1, y1, x2, y2, confidence, class_id]` 个值。使用默认的 `max_det=300` 时，这通常是 `(batch_size, 300, 6)` 。某些受限格式在不支持端到端算子时，会自动回退到传统输出布局。
	默认情况下（ `nms=None` ），包括 YOLO26 在内的检测模型会导出原始的一对多预测结果：输出通常是一个形状类似 `(batch_size, 4 + num_classes, num_predictions)` 的张量，其中通道表示边界框坐标和各类别的分数，而 `num_predictions` 取决于导出时的输入分辨率（也可以是动态的）。 [端到端检测指南](https://docs.ultralytics.com/zh/guides/end2end-detection) 介绍了哪些格式会保留端到端输出。
	对于 **分割模型** （例如 `yolo26n-seg.pt` ），通常会得到两个输出：第一个张量的形状类似 `(batch_size, 4 + num_classes + mask_dim, num_predictions)` （包含边界框、类别分数和掩码系数），第二个张量的形状类似 `(batch_size, mask_dim, proto_h, proto_w)` ，其中包含掩码原型，可与这些系数配合生成实例掩码。张量大小取决于导出时的输入分辨率（也可以是动态的）。
	对于 **姿态模型** （例如 `yolo26n-pose.pt` ），输出张量的形状通常类似 `(batch_size, 4 + num_classes + keypoint_dims, num_predictions)` ，其中 `keypoint_dims` 取决于姿态规范（例如关键点数量以及是否包含置信度），而 `num_predictions` 取决于导出时的输入分辨率（也可以是动态的）。
	[ONNX 推理示例](https://github.com/ultralytics/ultralytics/tree/main/examples) 展示了如何处理各类模型的这些输出。
- ### Ultralytics 是否提供官方的 C++ 推理 API？
	Ultralytics 目前不为 YOLO 模型提供专用的 C++ 推理 API。对于 C++ 部署，请将模型导出为 [ONNX](https://docs.ultralytics.com/zh/integrations/onnx) 、 [TensorRT](https://docs.ultralytics.com/zh/integrations/tensorrt) 、 [TorchScript](https://docs.ultralytics.com/zh/integrations/torchscript) 或 [MNN](https://docs.ultralytics.com/zh/integrations/mnn) 等运行时格式，然后使用相应运行时的原生 C++ API 加载导出的模型文件。
	例如，使用 `yolo export model=yolo26n.pt format=onnx` 导出检测模型，然后通过 ONNX Runtime C++ 运行 `.onnx` 文件；或者使用 `format=engine` 导出，再从 TensorRT C++ 应用运行 TensorRT 引擎。使用自定义 C++ 后处理时，请确保输出张量布局与你的任务和导出设置相匹配；默认的 YOLO26 检测导出会返回需要外部 NMS 处理的原始预测张量。使用 `nms=False` 导出无 NMS 检测结果，其形状为 `(batch, max_det, 6)` ；或者使用 `nms=True` 在受支持的格式中嵌入 NMS。
- ### 使用 nms=False 导出量化模型时，为什么 output0 是 FP32？
	使用 `quantize=16` （FP16）或 `quantize=8` （INT8）导出时，大多数张量都会转换为较低精度，以减小模型体积并提升性能。但是，启用 `nms=False` 时，后处理（包括类别索引）会直接嵌入导出的计算图中。
	`output0` 张量包含类别索引，这些索引在内部以浮点数表示。由于尾数精度有限，FP16 无法可靠地表示大于 2048 的整数值。为避免潜在的精度损失或类别 ID 错误， `output0` 会有意保留为 FP32。
	如果需要完整的 FP16 输出，请在 GPU 上使用 `nms=None` 导出，并在外部执行后处理。无论如何，CPU 上的 FP16 ONNX 导出都会保留 FP32 输入和输出，仅转换内部计算图。