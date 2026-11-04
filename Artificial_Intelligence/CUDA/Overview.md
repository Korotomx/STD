> 材料：NVIDIA《CUDA Programming Guide》13.4.2（`Ref/cuda-programming-guide.pdf`）· [中文图解站](https://okazaki-yumemi.github.io/CUDA_PROGRAMMING_GUIDE_simplified-Chinese/)（基于 13.3，逐段译文 + PDF 图版）。目标：能写、能调 kernel，并落到 groundzero / TensorRT 推理链路，不通读 734 页。

## 环境现状

- **RTX 5060 Laptop 8GB（WSL2）**，Python `dl_env`（PyTorch 2.11.0+cu128）。
- CUDA toolkit **12.8.93** 为默认（`/usr/local/cuda`），另装 **13.1.115** 对照；`nvidia-smi`、`nvcc --version`、hello kernel 均通过。
- WSL2 只装 toolkit，**不要装 Linux 显卡驱动**；驱动在 Windows 侧。`/usr/local/cuda` 保持 12.8 与 torch cu128 对齐。
- 系统 **gcc 15** 超出 CUDA 12.8 支持范围 → 用 `g++-14`；**glibc 2.43** 的 C23 `cospi/sinpi/rsqrt` 与 CUDA 头文件冲突 → nvcc 加 `-U_GNU_SOURCE`。已封装 `~/.local/bin/nvcc` wrapper，自动加 `-ccbin g++-14 -U_GNU_SOURCE -arch=sm_120`，直接 `nvcc xxx.cu -o xxx` 即可。详见 [[C01 Introduction]]。
- 8GB 显存：练习规模控制在 1024³ float 以内。

## 学习路线（三阶段）

| 阶段 | 内容 | 状态 |
|---|---|---|
| 基础 | C01 GPU 吞吐模型 / 异构系统 / CC·PTX·cubin·fatbin；C02 索引 / warp·SIMT / 内存层次 / 六步流程 | ✅ 2026-10-24 |
| 进阶 | C03 平台、C04 CUDA C++、C06 SIMT kernel、C08 异步、C09 统一内存、C10 NVCC；项目：向量加法 → 矩阵乘 → 灰度化 → resize → shared-memory GEMM | 进行中 |
| 落地 | groundzero 预处理 kernel（letterbox + 归一化 + HWC→CHW）、TensorRT 部署 | ✅ 2026-11-05 预处理核已接入 `03_yolo`；TensorRT 端到端 01~03 完成 |

## 笔记

- [[C01 Introduction]] — GPU 为什么快、异构模型、平台（CC / PTX / cubin / fatbin）、第一个 kernel。
- [[C02 Programming Model]] — 索引、warp/SIMT、内存层次、显式/统一内存、异步、错误检查；向量加法实验。
- [[X01 Triton 与 TileLang]] — thread-level → tile-level：Triton 与 TileLang 的编程模型、matmul 写法与取舍。
- [[T00 编译与链接 TensorRT 程序]] — `-I/-L/-l`、rpath、`ldd` 里为什么没有 nvinfer。
- [[TensorRT 部署学习路径]] — runtime → YOLO 端到端 → CUDA 加速 → 工程化，四周路线与当前进度；含 `03_yolo` GPU 预处理核（`warp_affine` + 双线性 + HWC→CHW）。
- 索引：[[CUDA/STDY/STDY|STDY]]；原始剪藏三篇在 `Ref/`（[[Session 1.0 并行计算与并行编程]] · [[Session 1.1 CUDA Programming Model]] · [[Session 1.2 Triton-TileLang]]）。

## 章节地图

- **Part I–II**（C01–C04、C06、C08–C10）：主线精读；C05 Python、C07 Tile 选读。
- **Part III–V**（Advanced CUDA、CUDA Features、附录）：参考手册，用到再查；多 GPU / 集群暂不需要。

## 命题速查

一条命题一行，`→` 是推理方向，末尾是落点；复习只看这张纸，卡住再点进去。

- GPU 快在吞吐不在延迟：大量简单核心并行，换单线程速度。[[C01 Introduction]]
- 异构模型：host 管分配与搬运，device 跑 kernel，两者内存不互通。[[C01 Introduction]]
- 线程层次 grid → block → thread；全局下标 `blockIdx*blockDim+threadIdx`。[[C02 Programming Model]]
- warp 固定 32 线程同步执行 → 线程数取 32 的倍数，分支发散会浪费 lane。[[C02 Programming Model]]
- kernel launch 是异步的 → 不同步就读，拿到的是旧数据。[[C02 Programming Model]]
- 统一内存不等于免费：页没驻留显存时每次跨 PCIe，慢一个量级。[[C02 Programming Model]]
- 三处必查：launch 返回值、`cudaGetLastError()`、同步后的错误。[[C02 Programming Model]]
- 编译三时刻：编译时 `-I`、链接时 `-L/-l`、运行时 rpath 或 `LD_LIBRARY_PATH`。[[T00 编译与链接 TensorRT 程序]]
- `--as-needed` 会丢掉没用到的库 → 依赖以 `readelf -d` / `ldd` 为准。[[T00 编译与链接 TensorRT 程序]]
- 纯 host 用 `g++`，出现 `__global__` 或 `.cu` 才用 `nvcc`。[[T00 编译与链接 TensorRT 程序]]
- 预处理 kernel：一个线程算一个目标像素，逆仿射回源图再双线性采样；目标坐标 `+0.5` 移到像素中心、回采前 `-0.5`，四邻居越界就填 114；结果直接写 engine 输入 buffer，不再需要 CPU 预处理和 blob 的 H2D。[[TensorRT 部署学习路径]]
- `__constant__` 变量所有线程只读、同一次 launch 共用；宿主用 `cudaMemcpyToSymbol` 写入；pitch 传 `img.step`，别假设 `W*3`。[[TensorRT 部署学习路径]]
- tile 级编程：只写 load/compute/store，线程映射交给编译器。[[X01 Triton 与 TileLang]]
- Triton 编译器决定 shared memory 与流水线；TileLang 把这层控制权还回来。[[X01 Triton 与 TileLang]]
- 抽象越高越好写，越低越能压榨性能：原型 Triton、性能工程 TileLang、极端调优 CUDA。[[X01 Triton 与 TileLang]]
