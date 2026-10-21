---
tags:
  - 概念原理
  - CUDA
  - cuDNN
  - TensorRT
  - GPU加速
  - 推理部署Inference
  - onnx
  - engine
---

# CUDA / cuDNN / TensorRT：GPU 加速的三层结构 · 概念原理 · N018

**时间:** 2026-10-21
**标签:** #概念原理 #CUDA #cuDNN #TensorRT #GPU加速 #推理部署Inference #onnx #engine
**关联:** [[N017 ResNet-18架构与残差连接]]（上一篇，训练出来的模型）· [[N019 TensorRT 部署：onnx 转 engine 并推理]]（实操）· [[N016 训练循环五步闭环]]（训练侧）

## 实际情况

2026-10-21 配齐 GPU 推理环境：CUDA toolkit 12.8 + cuDNN 9.27 + TensorRT 11.4(cu12)，并把任务二训练的 `best.onnx`（YOLOv8n 装甲板检测）用 TensorRT 转成 engine 跑通——推理 3.7ms/张，onnxruntime-CPU 要 75ms，**加速 20 倍**。本篇讲这三样东西分别是什么、为什么需要、怎么分工。

## 1. 从「训练好的模型要在 GPU 上快速跑」说起

训练用 PyTorch（连接 [[N016 训练循环五步闭环]]），在 dl_env 里跑通。但**训练完是要拿来用的**——任务二要把模型部署成 C++/ROS2 节点，实时检测装甲板。这时要的不是「灵活地训练」，而是「给定一张图，最快算出检测结果」。

把模型交给 GPU 高效执行，一路需要三样东西分工：**CUDA、cuDNN、TensorRT**。

## 2. CUDA toolkit —— 指挥 GPU 的「编译器和运行时」

GPU 是 NVIDIA 的硬件，CPU 的指令直接指挥不动它，必须走 NVIDIA 的软件栈。

- **CUDA** = NVIDIA 的 GPU 编程平台（Compute Unified Device Architecture）
- **toolkit** 提供三样关键东西：
  - `nvcc`：编译 CUDA 代码（`.cu`）的编译器
  - `libcudart`：CUDA 运行时库（程序运行时要链接的）
  - 数学库（cublas 矩阵、cufft 傅里叶等）

**类比：** CUDA 之于 GPU，就像 gcc + libc 之于 CPU——CPU 上用 gcc 编译 C 代码、靠 libc 跑；GPU 上用 nvcc 编译 CUDA 代码、靠 libcudart 跑。

本机装 CUDA **12.8**（nvcc 12.8.93，在 `/usr/local/cuda-12.8`）。

## 3. cuDNN —— 神经网络算子的「高度优化实现库」

神经网络最核心、最耗时的算子是**卷积**。你当然可以用 CUDA 直接在 GPU 上写卷积——能跑，但很慢；NVIDIA 的工程师把卷积、池化、归一化这些算子针对自家 GPU 优化到极致，打包成 **cuDNN**（CUDA Deep Neural Network library）。

**类比：** CUDA 是「通用语言」，cuDNN 是「已经替你写好的、极快的卷积函数库」——你直接调它，不用自己造轮子。

**注意：** PyTorch 训练时，底层其实也在调 cuDNN（装 torch 时自带了一份）。所以训练和推理都离不开它。本机装 cuDNN **9.27**。

## 4. TensorRT —— 推理专用的「执行计划编译器」

训练时要灵活（能改结构、能求梯度），推理时只要「固定结构，快速算输出」。TensorRT 抓住这个区别，在推理侧做三件优化：

1. **算子融合**：把相邻的几个小算子合成一个大算子（少几次显存读写）
2. **精度调优**：默认 TF32、可切 FP16/INT8，精度损失极小、速度快很多
3. **针对你这块 GPU 生成最优执行计划**（即 engine 文件）

流程：读入 onnx → 优化 → 输出 engine → 推理。本机 YOLOv8n 从 CPU 75ms 降到 GPU 3.7ms，**加速 20 倍**。本机装 TensorRT **11.4**。

## 5. 三者的层次关系

```
   你的程序（C++ 节点 / Python 推理脚本）
         │
   TensorRT  （推理引擎：融合算子 + 选精度 + 生成执行计划）
         │
    cuDNN    （卷积等算子的高效实现）
         │
   CUDA runtime / driver（把命令翻译给 GPU）
         │
    GPU 硬件（RTX 5060）
```

下层给上层当底座：TensorRT 调 cuDNN，cuDNN 调 CUDA，CUDA 指挥 GPU。

## 6. 训练 vs 推理：为什么用两套

| | 训练 | 推理 |
| ---- | ---- | ---- |
| 工具 | PyTorch | TensorRT（或 onnxruntime） |
| 追求 | 灵活、能求梯度 | 快、省显存 |
| 速度 | 一次几十分钟（无所谓） | 要几十 FPS（实时） |
| 结构 | 可变 | 固定 |

两者靠 **onnx** 格式衔接：PyTorch 训练完 export 成 onnx（模型结构的通用描述文件），TensorRT 读 onnx 生成 engine。

## 7. 版本为什么这样配

三者必须落在**同一个 CUDA 大版本**上，否则库之间对不上：

- CUDA **12.8**（和 torch 的 cu128 对齐）
- cuDNN **9.27**（对应 CUDA 12.x）
- TensorRT **11.4-cu12**（CUDA 12 只能用 pip 版；deb 版只有 CUDA 13）

## 思考

（留白 —— TensorRT 的 engine 是「针对当前这张 GPU 生成」的，换一台 GPU 就得重新生成。为什么 engine 不能像 onnx 那样到处跑？）

## 总结

**本质：** 在 GPU 上跑神经网络是三层分工——CUDA toolkit（nvcc + libcudart，指挥 GPU 的底座）、cuDNN（卷积等算子的极速实现库）、TensorRT（推理专用引擎，把 onnx 融合算子、选精度、编译成最优 engine）。训练用 PyTorch 图灵活、推理用 TensorRT 图快，中间靠 onnx 衔接；三者必须同 CUDA 大版本。本机 CUDA 12.8 + cuDNN 9.27 + TensorRT 11.4，YOLOv8n 推理从 75ms 加速到 3.7ms（20 倍）。
**标签:** #概念原理 #CUDA #cuDNN #TensorRT #GPU加速 #推理部署Inference #onnx #engine
