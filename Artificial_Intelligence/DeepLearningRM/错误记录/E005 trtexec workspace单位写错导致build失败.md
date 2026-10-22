# E005 · 构建 — trtexec workspace 单位写错导致 engine build 失败

**时间:** 2026-10-22
**分类:** #构建

## 问题

用 `trtexec` 把 groundzero 的 `best.onnx` 转 engine：

```bash
trtexec --onnx=best.onnx --saveEngine=best.engine --memPoolSize=workspace:2048MiB
```

build 了 33 秒后失败：

```
[W] UNSUPPORTED_STATE: Skipping tactic 0 due to insufficient memory
    on requested size of 10604536 detected for tactic 0x0000000000000000.
[E] Error[10]: IBuilder::buildSerializedNetworkToStream:
    Could not find any implementation for node {ForeignNode[/model.0/conv/Conv...]}
[I] Created engine with size: 0 MiB
```

看起来像模型不支持、显存不够，但实际上显卡还有 7 GB 空闲。

## 原因

`trtexec` 的 `--memPoolSize` **只认 `B / K / M / G` 后缀，不认 `MiB`**。

写 `2048MiB` 时，解析器取走数字 `2048`、忽略非法后缀，于是工作区只有 **2048 字节**。日志第一行就能看出来：

```
Memory Pools: workspace: 0.00195312 MiB   ← 2048 字节，不是 2048 MiB
```

workspace 太小 → 每层的候选 kernel 无法试跑 → TensorRT 报「找不到实现」，而不是直接说显存不足，所以很容易误判。

## 解决方案

改成合法后缀：

```bash
trtexec \
  --onnx=best.onnx \
  --saveEngine=best.engine \
  --memPoolSize=workspace:2048M
```

成功日志：

```
Memory Pools: workspace: 2048 MiB
Engine built in 39.9 sec
Created engine with size: 11.5644 MiB
Throughput: 629.27 qps
Latency: mean 1.59 ms
```

## 要点

- 合法后缀：`B`（字节）/ `K`（KiB）/ `M`（MiB）/ `G`（GiB）；**不写后缀时默认 MiB**
- 遇到 `Could not find any implementation`，先看 `Memory Pools:` 那一行确认 workspace 实际大小
- 同理别用 `--memPoolSize=workspace:2GiB`，要写 `2G`
- 工具名是 `trtexec`，没有 `tensorrt_rtx` 这个命令（那是另一个发行版 TensorRT-RTX 的命名）
- TensorRT 11 的 `trtexec` 没有 `--fp16`：strongly-typed 网络必须在 ONNX 图里预先转换精度
