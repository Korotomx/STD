# E004 · 运行时 — 训练 OOM：WSL2 内存不足、dataloader workers 开太多

**时间:** 2026-10-22
**分类:** #运行时

## 问题

`model.train(...)` 跑到中途被内核 OOM killer 杀掉（退出码 137）。`workers=8` 死、`workers=4` 也死（死在 epoch 7），日志里没有 Python 报错、进程直接消失。

## 原因

OOM 的是**系统内存**（不是显存）：WSL2 总共只有 7.4G，VS Code 的 Python 服务占约 2G，训练主进程（特征图 + pin memory）加上 dataloader 每个 worker 的子进程 + 共享内存（shmem）一起超了。`dmesg` 里能看到 `Out of memory: Killed process ... (python)`。

## 解决方案

降 dataloader workers + batch：

```python
model.train(..., workers=2, batch=8)   # 默认 workers=8, batch=16
```

要点：

- **区分显存(VRAM)与内存(RAM)**：这次显存 8G 才用 3G、根本没满，满的是 7.4G 系统内存——dmesg 说的 OOM 是「内存」不是「显存」
- `workers` 控制「并行加载数据的子进程数」，每个 worker 都占一份内存（含共享内存 shmem），WSL2 这种小内存环境别用默认 8
- 排查命令：`free -h` 看内存、`dmesg | grep -i "out of memory"` 看 OOM 记录
