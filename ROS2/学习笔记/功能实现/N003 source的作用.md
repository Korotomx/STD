---
tags:
  - 功能实现
  - 环境Environment
  - 工具
---

# source 的作用 · 功能实现 · N003

**时间:** 2026-10-03 首次记录 · 2026-10-05 13:13 深化
**标签:** #功能实现 #环境Environment #工具
**关联:** [[N004 工作空间vs包]]

## 疑惑点

`source setup.bash` 到底做了什么？为什么每次开新终端都要重新 source？

## 实际情况

1. `source xxx.bash` = **在当前终端进程里执行该文件**，把里面的环境变量、别名加载进来。
2. `source /opt/ros/lyrical/setup.bash` → 让终端能找到 `ros2` 命令和 ROS 的库。
3. `source ~/dev_ws/install/setup.bash` → 让你自己 build 的包能被 `ros2 run` 找到。
4. **环境变量是「进程级」的**：每个终端是独立进程，新终端不会继承上一个终端 source 的结果，所以每次都要重新加载。
5. **为什么必须 source 而不能直接 `./setup.bash`**：环境变量「进程私有 + 单向继承（父→子，子改不了父）」。直接执行会开子进程，`export` 只改子进程、退出即丢；source 在当前进程跑，变量才留得住。
6. **setup.bash 内部是「套娃」**：`setup.bash` → `. setup.sh` → `. local_setup.sh` → 各包的 `local_setup.bash`（`.` 就是 `source` 的简写）。
7. **真正改的是四个环境变量**：`PATH`（找命令）/ `LD_LIBRARY_PATH`（找 .so 库）/ `AMENT_PREFIX_PATH`（**ROS2 找包的核心**）/ `PYTHONPATH`（python 模块）。`ros2 pkg prefix <包名>`、`ros2 run` 都靠 `AMENT_PREFIX_PATH` 定位包。
8. **`.bashrc` 自动 source 的真相**：`.bashrc` 是 bash 每次开新终端自动执行的脚本；把 source 写进去（本机 `~/.bashrc:124`），开终端即自动加载——所以平时感觉「ros2 天生能用、不用手动 source」。

> **Note（连接 / 深化）：**
> - 连接：install/setup.bash 来自工作空间的构建产物，见 [[N004 工作空间vs包]]。
> - 深化：把 `source` 写进 `~/.bashrc` 可自动加载，避免每次手动执行（本机已配，见 `~/.bashrc:124`）。
> - 深化：`AMENT_PREFIX_PATH` 是 ROS2 定位包的核心变量，`ros2 pkg prefix` / `ros2 run` 都靠它。

## 思考

（留白 —— 试试 `echo $AMENT_PREFIX_PATH`，理解 ros2 靠它找包；再 `cat ~/.bashrc` 确认自动 source 了哪些）

## 总结

**本质：** `source` = 在**当前进程**里执行脚本、加载环境变量（而非开子进程，因为环境变量进程私有、单向继承）；因为环境变量不跨终端，所以每个新终端都要重新 source——除非写进 `.bashrc` 让它自动加载。
**标签:** #功能实现 #环境Environment #工具
