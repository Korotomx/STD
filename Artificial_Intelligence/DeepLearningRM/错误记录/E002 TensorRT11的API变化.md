# E002 · 构建 — TensorRT 11 的 API 变化（EXPLICIT_BATCH / FP16 被移除等）

**时间:** 2026-10-21 20:50
**分类:** #构建

## 问题

写 `trt_export_test.py` 时，照 TensorRT 8/10 的老教程写，连踩四个 `AttributeError`：

1. `trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH` 不存在
2. `builder.platform_has_fast_fp16` 不存在
3. `trt.BuilderFlag.FP16` 不存在（BuilderFlag 里只有 TF32，没有 FP16/INT8）
4. `build_serialized_network` 返回的 `IHostMemory` 没有 `len()`

## 原因

TensorRT 11 大幅改动 Python API，旧教程（8.x / 10.x 的写法）大量失效：

1. **EXPLICIT_BATCH 成为默认且唯一模式**，`create_network()` 不再需要传 flag
2. **精度控制 API 重构**：全局的 `BuilderFlag.FP16/INT8` 被移除，精度改为 per-layer 设置（`layer.precision`）；默认走 TF32
3. `build_serialized_network` 返回 `IHostMemory` 对象（不是 bytes），要 `bytes()` 包一层

## 解决方案

```python
network = builder.create_network()              # ① 不传 flag，默认 explicit batch
# ② 精度：先用默认 TF32（Blackwell 上已 20 倍加速），FP16 后续按 layer.precision 设
serialized = bytes(builder.build_serialized_network(network, config))  # ③ 包成 bytes
```

要点：

- **写 TensorRT 代码前，先 `dir(trt.BuilderFlag)` 之类确认 API 是否存在**，别照搬老教程（版本迭代快、老博客大量过期）
- 附加 warning：`execute_async_v3` 要传非默认 stream，否则 TensorRT 每次自己 `cudaStreamSynchronize`、性能打折。传 `torch.cuda.current_stream().cuda_stream` 可消除大部分；严格做法用独立 stream
