> 抓取自 Ultralytics 官方文档（web clip）。对应学习笔记：[[N020 NDJSON数据集与YOLO姿态估计pose训练]]

## 安装 Ultralytics

使用 pip、conda 或 Docker 安装 `ultralytics` 包，也可以从源代码安装；随后使用预训练的 [YOLO26](https://docs.ultralytics.com/zh/models/yolo26) 模型运行首次预测。每种安装方式都会安装 [pyproject.toml](https://github.com/ultralytics/ultralytics/blob/main/pyproject.toml) 中列出的所有必需依赖项。

安装

在 Python>=3.8 且 PyTorch>=1.8 的环境中安装或更新 [ultralytics](https://pypi.org/project/ultralytics/) 包：

```
pip install -U ultralytics
```

如需安装最新开发版本，请直接从 [Ultralytics GitHub 仓库](https://github.com/ultralytics/ultralytics) 安装：

```
pip install git+https://github.com/ultralytics/ultralytics.git@main
```

提示

[PyTorch](https://www.ultralytics.com/glossary/pytorch) 的安装要求因操作系统和 CUDA 版本而异。若要使用特定构建版本，请先按照 [PyTorch 安装说明](https://pytorch.org/get-started/locally/) 安装 PyTorch，然后安装 `ultralytics` 。对于 Linux 上的 AMD GPU，请按照 [AMD 集成指南](https://docs.ultralytics.com/zh/integrations/amd#installation) 中的说明安装 ROCm 版 PyTorch。

## 通过 CLI 使用 Ultralytics

在终端中使用 `yolo` 命令运行你的第一次预测：

```
yolo predict model=yolo26n.pt
```

预训练的 `yolo26n.pt` 权重会自动下载，模型会在两个随附的示例图像上运行，命令会显示标注结果的保存位置；首次运行时，该位置为 `runs/detect/predict` 。将 `source` 指向你自己的图像、视频、目录、URL 或流，也可以使用 `source=0` 指向网络摄像头：

```
yolo predict model=yolo26n.pt source=0 show=True
```

`predict` 是 **模式** ，用于指定如何使用模型： `train` 、 `val` 、 `predict` 、 `export` 、 `track` 或 `benchmark` 。 **任务** （ `detect` 、 `segment` 、 `semantic` 、 `depth` 、 `classify` 、 `pose` 或 `obb` ）会从模型文件中读取，因此 `yolo TASK MODE ARGS` 语法通常只需要模式以及 `arg=value` 键值对，例如 `imgsz=640` 。有关所有模式，请参阅 [CLI 指南](https://docs.ultralytics.com/zh/usage/cli) ；有关所有参数，请参阅 [配置](https://docs.ultralytics.com/zh/usage/cfg) 页面。

## 通过 Python 使用 Ultralytics

在 Python 中执行相同的预测：

```
from ultralytics import YOLO

model = YOLO("yolo26n.pt")  # 加载预训练的 YOLO26n 检测模型
results = model("https://ultralytics.com/images/bus.jpg", save=True)  # 进行预测并保存标注后的图像
```

`results` 是一个 [Results](https://docs.ultralytics.com/zh/modes/predict#working-with-results) 对象列表，每张图像对应一个对象；对象包含边界框、掩码、关键点或类别概率，具体取决于任务。 [Python 指南](https://docs.ultralytics.com/zh/usage/python) 介绍了如何使用相同的 `YOLO` 类进行训练、验证、导出和跟踪。

<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" src="https://player.bilibili.com/player.html?bvid=BV1Xm411z7am&amp;autoplay=0" title="YouTube video player" frameborder="0"></iframe>  
**观看：** Ultralytics YOLO 快速入门指南

## Ultralytics 设置

数据集、权重和运行结果目录等持久化设置、 [Ultralytics Platform](https://platform.ultralytics.com/) API 密钥以及实验记录器开关，都存储在由 `yolo settings` 管理的 JSON 文件中。有关如何查看、更改或重置这些设置，请参阅 [设置](https://docs.ultralytics.com/zh/usage/settings) 页面。

## 接下来做什么

浏览 YOLO 运行所用的 [模式](https://docs.ultralytics.com/zh/modes) 和 [YOLO26](https://docs.ultralytics.com/zh/models/yolo26) 模型尺寸，然后按照 [数据集指南](https://docs.ultralytics.com/zh/datasets) 整理数据，并 [使用自己的数据进行训练](https://docs.ultralytics.com/zh/modes/train) 。

想了解未来规划，可以查看 [YOLO27（即将推出）](https://docs.ultralytics.com/zh/models/yolo27) 。其模型目前尚未开放；以上示例使用的是已发布的 YOLO26 系列。

## 常见问题

- ### 如何使用 pip 安装 Ultralytics？
	使用 pip 安装 Ultralytics：
	```
	pip install -U ultralytics
	```
	这会从 [PyPI](https://pypi.org/project/ultralytics/) 安装最新稳定版 `ultralytics` 包。若要直接从 GitHub 安装开发版本：
	```
	pip install git+https://github.com/ultralytics/ultralytics.git
	```
	确保系统已安装 Git 命令行工具。
- ### 我可以使用 conda 安装 Ultralytics YOLO 吗？
	可以，在一条命令中创建包含 Python 和 Ultralytics YOLO 的 conda 环境，然后激活它：
	```
	conda create --name ultralytics-env -c conda-forge python=3.11 ultralytics torchvision -y
	conda activate ultralytics-env
	```
	这种方法是 pip 的绝佳替代方案，可确保与其他软件包兼容。对于 CUDA 环境，在同一条命令中添加 `pytorch-gpu` 元包，这样 conda 就会选择支持 CUDA 的 PyTorch 构建版本：
	```
	conda create --name ultralytics-env -c conda-forge python=3.11 ultralytics torchvision pytorch-gpu -y
	conda activate ultralytics-env
	```
	更多说明请参阅 [Conda 快速入门指南](https://docs.ultralytics.com/zh/guides/conda-quickstart) 。
- ### 使用 Docker 运行 Ultralytics YOLO 有哪些优势？
	Docker 为 Ultralytics YOLO 提供隔离且一致的环境，确保其在不同系统上流畅运行，并避免本地安装的复杂性。你可以在 [Docker Hub](https://hub.docker.com/r/ultralytics/ultralytics) 获取官方 Docker 镜像，其中包含适用于 GPU、CPU、ARM64、 [NVIDIA Jetson](https://docs.ultralytics.com/zh/guides/nvidia-jetson) 和 Conda 的变体。拉取并运行最新镜像：
	```
	# Pull the latest ultralytics image from Docker Hub
	sudo docker pull ultralytics/ultralytics:latest
	# Run the ultralytics image in a container with GPU support
	sudo docker run -it --ipc=host --device nvidia.com/gpu=all ultralytics/ultralytics:latest
	```
	在 Linux 上，CDI 设备请求需要 Docker >= 28.2.0 和 NVIDIA Container Toolkit >= 1.18。有关 Docker 的详细说明，请参阅 [Docker 快速入门指南](https://docs.ultralytics.com/zh/guides/docker-quickstart) 。
- ### 如何克隆 Ultralytics 仓库进行开发？
	克隆 Ultralytics 仓库并设置开发环境：
	```
	# Clone the ultralytics repository
	git clone https://github.com/ultralytics/ultralytics
	# Navigate to the cloned directory
	cd ultralytics
	# Install the package in editable mode for development
	pip install -e .
	```
	这样你就可以为项目做贡献，也可以试用最新的源代码。有关派生仓库和固定到自定义分支的信息，请参阅 [开发环境安装](https://docs.ultralytics.com/zh/help/contributing#development-installation) 。
- ### 为什么应该使用 Ultralytics YOLO CLI？
	Ultralytics YOLO CLI 无需编写 Python 代码，即可简化目标检测任务的运行，让你直接在终端中通过单行命令完成训练、验证和预测。基本语法如下：
	```
	yolo TASK MODE ARGS
	```
	例如，训练检测模型：
	```
	yolo train data=coco8.yaml model=yolo26n.pt epochs=10
	```
	在完整的 [CLI 指南](https://docs.ultralytics.com/zh/usage/cli) 中查看更多命令和用法示例。