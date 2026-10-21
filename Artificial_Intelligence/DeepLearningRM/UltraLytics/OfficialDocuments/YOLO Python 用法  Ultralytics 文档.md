> 抓取自 Ultralytics 官方文档（web clip）。对应学习笔记：[[N020 NDJSON数据集与YOLO姿态估计pose训练]] · [[E003 detect模型训练pose数据任务不匹配]]

## Python 用法

欢迎阅读 Ultralytics YOLO Python 用法文档！本指南旨在帮助你将 Ultralytics YOLO 无缝集成到 Python 项目中，以执行 [目标检测](https://www.ultralytics.com/glossary/object-detection) 、 [实例分割](https://docs.ultralytics.com/zh/tasks/segment) 、 [语义分割](https://docs.ultralytics.com/zh/tasks/semantic) 、 [深度估计](https://docs.ultralytics.com/zh/tasks/depth) 和 [分类](https://docs.ultralytics.com/zh/tasks/classify) 。在这里，你将学习如何加载和使用预训练模型、训练新模型，以及对图像进行预测。易于使用的 Python 接口对所有希望在 Python 项目中集成 YOLO 的人来说都很有帮助，让你能够快速实现高级目标检测功能。让我们开始吧！

<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" src="https://player.bilibili.com/player.html?bvid=BV15z42117Cc&amp;autoplay=0" title="YouTube video player" frameborder="0"></iframe>  
**观看：** 精通 Ultralytics YOLO：Python

例如，用户只需几行代码，即可加载模型、训练模型、在验证集上评估模型性能，甚至 [将模型导出为 ONNX 格式](https://docs.ultralytics.com/zh/modes/export) 。

```
from ultralytics import YOLO

# 从头开始创建新的 YOLO 模型
model = YOLO("yolo26n.yaml")

# 加载预训练的 YOLO 模型（推荐用于训练）
model = YOLO("yolo26n.pt")

# 使用 'coco8.yaml' 数据集训练模型 3 个周期
results = model.train(data="coco8.yaml", epochs=3)

# 在验证集上评估模型性能
results = model.val()

# 使用模型对图像执行目标检测
results = model("https://ultralytics.com/images/bus.jpg")

# 将模型导出为 ONNX 格式
success = model.export(format="onnx")
```

## 训练

[训练模式](https://docs.ultralytics.com/zh/modes/train) 用于在自定义数据集上训练 YOLO 模型。在此模式下，模型会使用指定的数据集和超参数进行训练。训练过程会优化模型参数，使模型能够准确预测图像中对象的类别和位置。

训练

```
from ultralytics import YOLO

model = YOLO("yolo26n.pt")  # 传入任何模型类型
results = model.train(epochs=5)
```

[训练示例](https://docs.ultralytics.com/zh/modes/train)

## 验证

[验证模式](https://docs.ultralytics.com/zh/modes/val) 用于在 YOLO 模型训练完成后对其进行验证。在此模式下，模型会在验证集上进行评估，以衡量其 [准确率](https://www.ultralytics.com/glossary/accuracy) 和泛化性能。你可以使用此模式调整模型的超参数，以提升模型性能。

验证

```
from ultralytics import YOLO

# 加载 YOLO 模型
model = YOLO("yolo26n.yaml")

# 训练模型
model.train(data="coco8.yaml", epochs=5)

# 在训练数据集的验证划分上进行验证
model.val()
```

[验证示例](https://docs.ultralytics.com/zh/modes/val)

## 预测

[预测模式](https://docs.ultralytics.com/zh/modes/predict) 用于使用训练好的 YOLO 模型对新图像或视频进行预测。在此模式下，模型会从检查点文件加载，用户可以提供图像或视频来执行推理。模型会预测输入图像或视频中对象的类别和位置。

预测

```
import cv2
from PIL import Image

from ultralytics import YOLO

model = YOLO("model.pt")
# 接受所有格式 - image/dir/Path/URL/video/PIL/ndarray。0 表示网络摄像头
results = model.predict(source="0")
results = model.predict(source="folder", show=True)  # 显示预测结果。接受所有 YOLO predict 参数

# from PIL
im1 = Image.open("bus.jpg")
results = model.predict(source=im1, save=True)  # 保存绘制了结果的图像

# 来自 ndarray
im2 = cv2.imread("bus.jpg")
results = model.predict(source=im2, save=True, save_txt=True)  # 将预测结果保存为标签

# 来自 PIL/ndarray 列表
results = model.predict(source=[im1, im2])
```

[预测示例](https://docs.ultralytics.com/zh/modes/predict)

## 导出

[导出模式](https://docs.ultralytics.com/zh/modes/export) 用于将 YOLO 模型导出为可用于部署的格式。在此模式下，模型会转换为其他软件应用或硬件设备可用的格式。将模型部署到生产环境时，此模式非常有用。

导出

将官方 YOLO 模型导出为支持动态批量大小和图像大小的 [ONNX](https://www.ultralytics.com/glossary/onnx-open-neural-network-exchange) 格式。

```
from ultralytics import YOLO

model = YOLO("yolo26n.pt")
model.export(format="onnx", dynamic=True)
```

[导出示例](https://docs.ultralytics.com/zh/modes/export)

## 跟踪

[跟踪模式](https://docs.ultralytics.com/zh/modes/track) 用于使用 YOLO 模型实时跟踪对象。在此模式下，模型会从检查点文件加载，用户可以提供实时视频流来执行实时对象跟踪。此模式适用于监控系统或 [自动驾驶汽车](https://www.ultralytics.com/solutions/computer-vision-in-automotive) 等应用。

跟踪

```
from ultralytics import YOLO

# 加载模型
model = YOLO("yolo26n.pt")  # 加载官方检测模型
model = YOLO("yolo26n-seg.pt")  # 加载官方分割模型
model = YOLO("path/to/best.pt")  # 加载自定义模型

# 使用模型进行跟踪
results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True)
results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True, tracker="bytetrack.yaml")
```

[跟踪示例](https://docs.ultralytics.com/zh/modes/track)

## 基准测试

[基准测试模式](https://docs.ultralytics.com/zh/modes/benchmark) 用于分析 YOLO 各种导出格式的速度和准确率。基准测试会提供导出格式的大小、其 `mAP50-95` 指标（用于目标检测和分割）或 `accuracy_top1` 指标（用于分类），以及 ONNX、 [OpenVINO](https://docs.ultralytics.com/zh/integrations/openvino) 、TensorRT 等各种导出格式下每张图像的推理时间（毫秒）。用户可以根据对速度和准确率的要求，利用这些信息为特定用例选择最佳导出格式。

基准测试

对官方 YOLO 模型的所有导出格式进行基准测试。

```
from ultralytics.utils.benchmarks import benchmark

# Benchmark
benchmark(model="yolo26n.pt", data="coco8.yaml", imgsz=640, device=0)
```

[基准测试示例](https://docs.ultralytics.com/zh/modes/benchmark)

## 使用训练器

`YOLO` 模型类是 Trainer 类的高层封装。每个 YOLO 任务都有自己的训练器，并继承自 `BaseTrainer` 。这种架构让你能够更灵活地定制 [机器学习工作流](https://docs.ultralytics.com/zh/guides/model-training-tips) 。

检测训练器示例

```
from ultralytics.models.yolo.detect import DetectionPredictor, DetectionTrainer, DetectionValidator

overrides = {"model": "yolo26n.pt", "data": "coco8.yaml", "epochs": 3}

# Trainer
trainer = DetectionTrainer(overrides=overrides)
trainer.train()
trained_model = trainer.best  # best.pt 的路径

# Validator
validator = DetectionValidator(args={"data": "coco8.yaml"})
validator(model=trained_model)

# Predictor
predictor = DetectionPredictor(overrides={"model": trained_model})
predictor(source="https://ultralytics.com/images/bus.jpg")

# 从上次检查点恢复被中断的训练
trainer = DetectionTrainer(overrides={"resume": "path/to/last.pt"})
trainer.train()
```

你可以轻松定制训练器，以支持自定义任务或探索研发思路。Ultralytics YOLO 的模块化设计让你能够根据具体需求调整框架，无论是处理新的 [计算机视觉](https://www.ultralytics.com/glossary/computer-vision-cv) 任务，还是微调现有模型以获得更好的性能。

[自定义教程](https://docs.ultralytics.com/zh/usage/engine)

## 常见问题

- ### 如何将 YOLO 集成到我的 Python 项目中以进行目标检测？
	将 Ultralytics YOLO 集成到你的 Python 项目中很简单。你可以加载预训练模型，也可以从头开始训练新模型。以下是入门方法：
	```
	from ultralytics import YOLO
	# 加载预训练的 YOLO 模型
	model = YOLO("yolo26n.pt")
	# 对图像执行目标检测
	results = model("https://ultralytics.com/images/bus.jpg")
	# 可视化结果
	for result in results:
	    result.show()
	```
	更多详细示例请参阅 [预测模式](https://docs.ultralytics.com/zh/modes/predict) 部分。
- ### YOLO 提供哪些不同模式？
	Ultralytics YOLO 提供多种模式，以适应不同的 [机器学习](https://www.ultralytics.com/glossary/machine-learning-ml) 工作流，包括：
	- **[训练](https://docs.ultralytics.com/zh/modes/train)** ：使用自定义数据集训练模型。
	- **[验证](https://docs.ultralytics.com/zh/modes/val)** ：在验证集上评估模型性能。
	- **[预测](https://docs.ultralytics.com/zh/modes/predict)** ：对新图像或视频流进行预测。
	- **[导出](https://docs.ultralytics.com/zh/modes/export)** ：将模型导出为 ONNX 和 TensorRT 等多种格式。
	- **[跟踪](https://docs.ultralytics.com/zh/modes/track)** ：在视频流中实时跟踪对象。
	- **[基准测试](https://docs.ultralytics.com/zh/modes/benchmark)** ：对不同配置下的模型性能进行基准测试。
	每种模式都旨在为 [模型开发和部署](https://docs.ultralytics.com/zh/guides/model-deployment-options) 的不同阶段提供全面的功能。
- ### 如何使用我的数据集训练自定义 YOLO 模型？
	要训练自定义 YOLO 模型，你需要指定数据集和其他 [超参数](https://www.ultralytics.com/glossary/hyperparameter-tuning) 。下面是一个快速示例：
	```
	from ultralytics import YOLO
	# 加载 YOLO 模型
	model = YOLO("yolo26n.yaml")
	# 使用自定义数据集训练模型
	model.train(data="path/to/your/dataset.yaml", epochs=10)
	```
	有关训练的更多详情和示例用法链接，请访问我们的 [训练模式](https://docs.ultralytics.com/zh/modes/train) 页面。
- ### 如何导出 YOLO 模型以进行部署？
	使用 `export` 函数即可轻松将 YOLO 模型导出为适合部署的格式。例如，你可以将模型导出为 ONNX 格式：
	```
	from ultralytics import YOLO
	# 加载 YOLO 模型
	model = YOLO("yolo26n.pt")
	# 将模型导出为 ONNX 格式
	model.export(format="onnx")
	```
	有关各种导出选项，请参阅 [导出模式](https://docs.ultralytics.com/zh/modes/export) 文档。
- ### 我可以在不同的数据集上验证 YOLO 模型吗？
	可以。你可以在不同的数据集上验证 YOLO 模型。训练完成后，你可以使用验证模式评估模型性能：
	```
	from ultralytics import YOLO
	# 加载 YOLO 模型
	model = YOLO("yolo26n.yaml")
	# 训练模型
	model.train(data="coco8.yaml", epochs=5)
	# 在不同的数据集上验证模型
	model.val(data="path/to/separate/data.yaml")
	```
	请查看 [验证模式](https://docs.ultralytics.com/zh/modes/val) 页面，了解详细示例和用法。