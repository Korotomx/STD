训练用 PyTorch，部署要的是「给定一张图最快算出结果」，这中间靠 CUDA / cuDNN / TensorRT 三层分工。本机 CUDA 12.8 + cuDNN 9.27 + TensorRT 11.4(cu12)，YOLOv8n 推理从 CPU 75ms 降到 3.7ms（20 倍）。

## CUDA toolkit：指挥 GPU 的底座

GPU 是 NVIDIA 硬件，CPU 指令直接指挥不动，必须走 NVIDIA 软件栈。

- **CUDA** = NVIDIA 的 GPU 编程平台
- **toolkit** 提供：
  - `nvcc`：编译 `.cu` 的编译器
  - `libcudart`：CUDA 运行时库
  - 数学库（cublas 矩阵、cufft 傅里叶等）

类比：CUDA 之于 GPU，就像 gcc + libc 之于 CPU。本机 CUDA **12.8**（nvcc 12.8.93，`/usr/local/cuda-12.8`）。

## cuDNN：神经网络算子的优化实现库

卷积是 CNN 最核心、最耗时的算子。可以直接用 CUDA 写，但慢；NVIDIA 把卷积、池化、归一化针对自家 GPU 优化到极致，打包成 **cuDNN**。

类比：CUDA 是通用语言，cuDNN 是已经写好、极快的卷积函数库。PyTorch 训练时底层也在调 cuDNN（装 torch 时自带一份），所以训练和推理都离不开。本机 **9.27**。

## TensorRT：推理专用编译器

训练要灵活（能改结构、能求梯度），推理只要固定结构快速算输出。TensorRT 在推理侧做三件事：

1. **算子融合**：相邻小算子合成大算子，少几次显存读写
2. **精度调优**：默认 TF32，可切 FP16/INT8，精度损失小、速度快很多
3. **针对当前 GPU 生成最优执行计划**（engine 文件）

流程：读入 ONNX → 优化 → 输出 engine → 推理。本机 **11.4**。

## 三者的层次

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

## 训练 vs 推理

| | 训练 | 推理 |
| ---- | ---- | ---- |
| 工具 | PyTorch | TensorRT（或 onnxruntime） |
| 追求 | 灵活、能求梯度 | 快、省显存 |
| 速度 | 一次几十分钟无所谓 | 要几十 FPS |
| 结构 | 可变 | 固定 |

两者靠 **ONNX** 衔接：PyTorch 训练完 export 成 ONNX（模型结构的通用描述），TensorRT 读 ONNX 生成 engine。实操见 [[N019 TensorRT部署onnx转engine并推理]]。

## 版本匹配

三者必须落在**同一个 CUDA 大版本**上，否则库之间对不上：

- CUDA **12.8**（和 torch 的 cu128 对齐）
- cuDNN **9.27**（对应 CUDA 12.x）
- TensorRT **11.4-cu12**（CUDA 12 只能用 pip 版；deb 版只有 CUDA 13）

## 坑与边界

- engine 绑定当前 GPU 架构与 TensorRT 版本，换设备必须重新 build（见 [[N019 TensorRT部署onnx转engine并推理]]）。
- TensorRT 11 是 strongly-typed，没有全局 FP16 开关，精度要写进 ONNX 图。
- 只装 CUDA driver 不等于有 toolkit：`nvcc`、头文件、`trtexec` 都来自 toolkit/SDK。

## 总结

GPU 上跑神经网络是三层分工：CUDA toolkit（nvcc + libcudart，指挥 GPU）、cuDNN（卷积等算子的极速实现）、TensorRT（推理引擎，融合算子、选精度、编译 engine）。训练用 PyTorch 图灵活，推理用 TensorRT 图快，中间靠 ONNX 衔接；三者必须同 CUDA 大版本。