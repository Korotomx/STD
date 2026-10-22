# E006 · 运行时 — Ultralytics 导出的 engine 带 JSON 头，直接反序列化失败

**时间:** 2026-10-22
**分类:** #运行时

## 问题

用 Ultralytics 导出 FP16 engine：

```python
model.export(format="engine", quantize=16, ...)
```

产出 `best.engine`，但用自己的 `infer_engine.py` 加载时报错：

```
[TRT] [E] IRuntime::deserializeCudaEngine: Error Code 1: Serialization
(Serialization assertion header.magicTag == kEXPECTED_MAGIC_TAG failed.
Trying to load an engine created with incompatible serialization version
(1014 != 1953657958). ...)
AssertionError: engine 反序列化失败（GPU 或 TRT 版本不匹配？）
```

错误信息看起来像「TensorRT 版本不匹配」，但导出和推理用的是同一个 `tensorrt 11.4.0.106`。

## 原因

Ultralytics 的 `.engine` 文件**不是纯 engine 字节**，而是：

```
[4 字节小端 JSON 长度][JSON 元数据][真正的 ftrt engine]
```

groundzero 的元数据长度是 **1014 字节**。报错里的 `1014` 正是这个长度，被 TensorRT 当成了 magic tag 的一部分。

对比文件头：

```
best_fp32.engine（自己 trtexec 构建）:
00000000: 6674 7274 ...        ← "ftrt" 开头

best.engine（Ultralytics 导出）:
00000000: f603 0000 7b22 ...  ← 0x3f6 = 1014，后面是 {"description": "Ultralytics...
```

## 解决方案

读文件时先解析 4 字节长度，跳过 JSON 头：

```python
import json

def read_engine_bytes(path):
    raw = path.read_bytes()
    n = int.from_bytes(raw[:4], "little")
    if 0 < n <= len(raw) - 4:
        try:
            json.loads(raw[4 : 4 + n])      # 能解析成 JSON 才认为是元数据头
            return raw[4 + n :]
        except (ValueError, UnicodeDecodeError):
            pass
    return raw
```

然后：

```python
engine = runtime.deserialize_cuda_engine(read_engine_bytes(engine_path))
```

另一种做法是直接用 Ultralytics 的 backend 加载，它会自动处理头：

```python
from ultralytics import YOLO
model = YOLO("best.engine")
```

## 教训

- **文件扩展名相同，内部格式不一定相同**：自己 `trtexec` 出来的是裸 engine，Ultralytics 导出的是「元数据头 + engine」。
- 报错里的魔数 `1014` 就是 JSON 头长度，不是 TensorRT 版本号。
- 元数据头里带着 task、类别名、输入 shape 等信息，Ultralytics 推理需要它；自己写 runtime 时可以丢掉，但要知道它存在。
