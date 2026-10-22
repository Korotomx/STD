## Quick Start Guide 快速入门指南

This guide walks you from a sample ONNX model to a running TensorRT-RTX engine on your RTX GPU using the `tensorrt_rtx` command-line tool in three steps: download a model, build a portable engine (**AOT**, ahead-of-time), and run inference (**JIT**, just-in-time). For how those phases fit together, refer to the [Architecture Overview](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/architecture/architecture-overview.html#architecture-overview).  
本指南将引导您使用 ONNX 示例模型，在您的 RTX GPU 上运行 TensorRT-RTX 引擎。 `tensorrt_rtx` 命令行工具三步走：下载模型，构建便携式引擎（ **AOT** （提前），并运行推理（ **准时制** （即准时制）。有关这些阶段如何衔接，请参阅…… [架构概述](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/architecture/architecture-overview.html#architecture-overview) 。

By the end you will have:  
到最后你将拥有：

- An ONNX model on disk 磁盘上的 ONNX 模型
- A serialized `resnet_engine.trt` engine file 连续的 `resnet_engine.trt` 引擎文件
- A successful inference run and a runtime cache for faster later launches  
	推理运行成功，并缓存运行时信息以加快后续启动速度。

> [!note] Note
> **GPU required only for Step 3.** Steps 1 and 2 run on a CPU-only machine (useful for build servers). Step 3 needs an installed RTX GPU and drivers that match [Prerequisites](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/installing-tensorrt-rtx/prerequisites.html#prerequisites).
> 
>   
> **仅步骤 3 需要 GPU。** 步骤 1 和 2 在仅使用 CPU 的机器上运行（适用于构建服务器）。步骤 3 需要已安装的 RTX GPU 和匹配的驱动程序。 [先决条件](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/installing-tensorrt-rtx/prerequisites.html#prerequisites) 。

## Prerequisites 先决条件

Before you begin:开始之前：

- Install TensorRT-RTX. Refer to [Installation Guide Overview](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/installing-tensorrt-rtx/installation-overview.html#installation-overview) and [Installing TensorRT-RTX](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/installing-tensorrt-rtx/installing.html#installing).  
	安装 TensorRT-RTX。请参阅 [安装指南概述](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/installing-tensorrt-rtx/installation-overview.html#installation-overview) 和 [安装 TensorRT-RTX](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/installing-tensorrt-rtx/installing.html#installing) 。
- Confirm your platform and GPU against [Prerequisites](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/installing-tensorrt-rtx/prerequisites.html#prerequisites) and the [Support Matrix](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/getting-started/support-matrix.html#support-matrix).  
	请确认您的平台和GPU是否与描述相符。 [先决条件](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/installing-tensorrt-rtx/prerequisites.html#prerequisites) 以及 [支持矩阵](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/getting-started/support-matrix.html#support-matrix) 。
- Confirm the CLI is on your `PATH`: `tensorrt_rtx --help` (Linux) or `tensorrt_rtx.exe --help` (Windows). If that fails, skip to below.

## Step 1: Download a Sample Model

This walkthrough uses a pre-trained ResNet-50 model from the [ONNX Model Zoo](https://github.com/onnx/models):

```bash
wget https://download.onnxruntime.ai/onnx/models/resnet50.tar.gz
tar xzf resnet50.tar.gz
```

```powershell
Invoke-WebRequest -Uri https://download.onnxruntime.ai/onnx/models/resnet50.tar.gz -OutFile resnet50.tar.gz
tar -xzf resnet50.tar.gz
```

Listing 1 Expected output (paths may vary) [#](#id2 "Link to this code")

```
resnet50/model.onnx
```

You should now have `resnet50/model.onnx`. To use your own model instead, export it to ONNX first; refer to the [ONNX Conversion Guide](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/installing-tensorrt-rtx/onnx-conversion.html#onnx-conversion).

## Step 2: Build the Engine (AOT)

Convert the ONNX model into a TensorRT-RTX engine. This step does **not** require a GPU and typically takes 20–30 seconds for most models.

```bash
tensorrt_rtx --onnx=resnet50/model.onnx --saveEngine=resnet_engine.trt
```

```powershell
tensorrt_rtx.exe --onnx=resnet50\model.onnx --saveEngine=resnet_engine.trt
```

```
Engine serialized to resnet_engine.trt
Engine size: ~25 MB (varies by model and precision)
```

You should see `resnet_engine.trt` in your working directory. This file is portable across supported RTX GPUs and operating systems.

## Step 3: Run Inference (JIT)

Load the engine and run inference on your RTX GPU. The first run JIT-compiles kernels for your device; `--runtimeCacheFile` saves that work for later launches.

```bash
tensorrt_rtx --loadEngine=resnet_engine.trt \
          --runtimeCacheFile=resnet.cache
```

```powershell
tensorrt_rtx.exe --loadEngine=resnet_engine.trt \`
          --runtimeCacheFile=resnet.cache
```

Listing 3 Expected output (representative; first run includes JIT compile time) [#](#id4 "Link to this code")

```
Inference latency: ~3 ms per iteration (GPU-dependent)
Runtime cache written to resnet.cache
```

If inference completes with latency output and a cache file is written, your TensorRT-RTX setup is working end to end.

## What You Just Did

You verified three things in three commands:

1. TensorRT-RTX can read an ONNX model and compile it to a portable engine (AOT).
2. The runtime can load that engine on your RTX GPU and run inference (JIT).
3. Runtime caching can persist JIT artifacts for faster subsequent runs.

This is the minimum viable deployment loop. [Build Your First Engine](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/getting-started/build-your-first-engine.html#build-your-first-engine) expands this walkthrough with production notes; the sections below point to deeper topics.

**Artifacts checklist** (you are ready for deployment topics when all are present):

- `resnet50/model.onnx` (or your own ONNX file)
- `resnet_engine.trt` from Step 2
- `resnet.cache` from Step 3 (after a successful JIT run)

## If a Command Fails

Confirm the CLI is installed and on your `PATH`:

```bash
tensorrt_rtx --help
```

```powershell
tensorrt_rtx.exe --help
```

If that fails, return to [Installing TensorRT-RTX](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/installing-tensorrt-rtx/installing.html#installing) and recheck `PATH` (Windows) or `PATH` / `LD_LIBRARY_PATH` (Linux) settings.

| Symptom | What to check |
| --- | --- |
| `--help` not found or unknown command | SDK/tarball `bin` on `PATH`; on Linux, `lib` on `LD_LIBRARY_PATH`. Re-run install steps in [Installing TensorRT-RTX](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/installing-tensorrt-rtx/installing.html#installing). |
| Step 1: archive missing or no `resnet50/model.onnx` | Re-download and extract; confirm your working directory matches the paths in Step 2. |
| Step 2: build errors or no `resnet_engine.trt` | No GPU is required. Check ONNX path, unsupported operators ([Operators](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/api/operators.html#operators)), and [Support Matrix](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/getting-started/support-matrix.html#support-matrix) precision limits. |
| Step 3: no GPU, driver, or CUDA errors | RTX GPU present, drivers installed, CUDA toolkit version matches prerequisites. The first JIT run can take several seconds; that is normal. |
| Step 3: inference runs but no cache file | Confirm `--runtimeCacheFile` is set and the process can write to the output directory. |

## Other Workflows

Most applications stay on the ONNX + `tensorrt_rtx` CLI path above. When you outgrow it:

- **Open-source demos**: End-to-end examples, including Flux, in the [TensorRT-RTX demos](https://github.com/NVIDIA/TensorRT-RTX/tree/main/demo) directory
- **Open-source samples**: Standalone runnable C++ and Python programs in the [TensorRT-RTX samples](https://github.com/NVIDIA/TensorRT-RTX/tree/main/samples) directory, and end-to-end samples with ONNX Runtime in [DIN Deploy](https://github.com/NVIDIA/din-deploy)
- **Your own ONNX models**: [ONNX Conversion Guide](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/installing-tensorrt-rtx/onnx-conversion.html#onnx-conversion)
- **C++ or Python integration**: [Using the Native Runtime API](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/inference-library/runtime-api.html#runtime-api)
- **PyTorch**: [Using TensorRT-RTX via PyTorch](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/inference-library/torch-trt-rtx.html#torch-tensorrt-rtx)
- **Port from TensorRT**: [Porting Guide for TensorRT Applications](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/inference-library/porting.html#porting)
- **Performance tuning**: [Best Practices](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/performance/best-practices.html#best-practices)

Run `tensorrt_rtx --help` for the full CLI flag reference.