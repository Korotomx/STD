---
tags:
  - 功能实现
  - 虚拟环境venv
  - 环境配置
  - 包管理pip
---

# 虚拟环境 venv：隔离的 Python 世界 · 功能实现 · N003

**时间:** 2026-10-17
**标签:** #功能实现 #虚拟环境venv #环境配置 #包管理pip
**关联:** [[N001 张量基础dtype-shape-device与GPU]]（同为环境前置）

## 实际情况

本机实测：系统 Python 3.14（`/usr/bin/python3`）与虚拟环境 `dl_env`（`/home/akiha/dl_env/`）并存，互不干扰。

### 1. 什么是虚拟环境

虚拟环境 = 一个**独立的 Python 世界**，有自己的解释器 + 自己的第三方库目录，和系统 Python 完全隔离。

**C/C++ 类比**：相当于每个项目一套独立的「编译器 + include/lib 目录」，而不是全系统共用一套 `/usr/lib` 和一个 gcc 版本。C++ 里不同项目要不同版本库、靠 CMake 找库很痛苦；Python 的解法就是「每项目一个 venv，库各装各的」。

### 2. 为什么要用（三个理由）

1. **系统 Python 版本不对**：本机系统是 Python 3.14，太新，torch 没有对应 wheel（装不上）。`dl_env` 用 3.11 解决。
2. **项目间隔离**：任务一用 torch 2.11，将来别的项目可能要别的库/版本，互不污染。
3. **不污染系统**：装错东西直接删掉整个 venv 重建，系统 Python 不受影响。

### 3. 本机两个环境对比

| 环境 | 位置 | 解释器 | 有 torch? |
| ---- | ---- | ---- | ---- |
| 系统 Python | `/usr/bin/python3` | 3.14 | ❌（`import torch` 报 Traceback） |
| dl_env（venv） | `/home/akiha/dl_env/` | 3.11.15 | ✅ 2.11.0+cu128 |

实测：终端直接 `python3 -c "import torch"` 报错，而 `dl_env` 里 torch 全齐。

### 4. 关键操作

**创建**（已建好，不必重复）：
```bash
python3.11 -m venv /home/akiha/dl_env
```

**激活**（终端跑代码前）：
```bash
source /home/akiha/dl_env/bin/activate   # 提示符前出现 (dl_env)
python 02_autograd.py                     # 这时才是 3.11 + torch
deactivate                                # 用完退出
```
或不激活、直接用全路径：`/home/akiha/dl_env/bin/python 02_autograd.py`。

**VS Code 选解释器**（一次性）：`Ctrl+Shift+P` → `Python: Select Interpreter` → 选 dl_env；或在项目 `.vscode/settings.json` 里写 `python.defaultInterpreterPath` 固定（本项已配好）。

### 5. Anaconda vs venv

视频第三章用 Anaconda（conda）建虚拟环境，本机用标准库 `venv`——**同一个概念、不同工具**。conda 额外能管非 Python 依赖（某些 C 库），但纯 PyTorch 项目 venv 够用、更轻。

## 思考

（留白 —— `deactivate` 只是改 shell 的 PATH，为什么退出后「系统 Python 还在」？虚拟环境到底「虚拟」在哪一层？）

## 总结

**本质：** 虚拟环境 = 隔离的 Python（自己的解释器 + 库目录），C++ 类比是「每项目独立工具链」。本机 `dl_env`（3.11 + torch 2.11 cu128）已建好，与系统 3.14 隔离；终端用 `source activate` 激活、或全路径调用；VS Code 写 `python.defaultInterpreterPath` 固定。Anaconda/conda 与 venv 同概念、不同工具。
**标签:** #功能实现 #虚拟环境venv #环境配置 #包管理pip
