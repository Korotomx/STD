开发中遇到的问题与解决记录。每类一个 `##` 小节，按「现象 / 原因 / 解决 / 预防」记录；顶部是索引。

## 索引

| 编号 | 分类 | 问题 | 关键词 |
| ---- | ---- | ---- | ---- |
| [[#E001 matplotlib无显示环境Agg后端与中文字体\|E001]] | 运行时 | WSL 无显示环境画图 | Agg 后端、字体 fallback |
| [[#E002 TensorRT11的API变化\|E002]] | 构建 | TensorRT 11 API 与旧教程不兼容 | EXPLICIT_BATCH、BuilderFlag.FP16 |
| [[#E003 detect模型训练pose数据任务不匹配\|E003]] | 运行时 | 检测模型训姿态数据 | task 字段、pose 模型 |
| [[#E004 训练OOM内存不足dataloader workers太多\|E004]] | 运行时 | 训练被 OOM killer 杀掉 | RAM vs VRAM、workers |
| [[#E005 trtexec workspace单位写错导致build失败\|E005]] | 构建 | engine build 报找不到实现 | MiB 非法后缀、workspace |
| [[#E006 Ultralytics导出的engine带JSON头导致反序列化失败\|E006]] | 运行时 | engine 反序列化 magicTag 失败 | JSON 元数据头、ftrt |

分类含义：`构建` 编译/链接/安装/依赖；`运行时` 训练/推理/显存/数据；`环境` CUDA/GPU/环境变量；`API` 语法/API/版本差异。

## E001 matplotlib无显示环境Agg后端与中文字体

**现象**：跑 `03_dataset.py` 可视化时依次踩三个坑：`_tkinter.TclError: couldn't connect to display ":10"`；中文标题变豆腐块；换成 `Droid Sans Fallback` 后英文/数字（`T`、`=`）反而缺失。

**原因**：本机 GUI 走 xrdp 的 Xvnc `:10`，当前 shell 没连上 X，matplotlib 默认 `TkAgg` 要开窗口；`DejaVu Sans` 只含 Latin，没有 CJK 字形；`Droid Sans Fallback` 是 CJK fallback 字体，Latin 不全。

**解决**：

```python
import matplotlib
matplotlib.use("Agg")        # 无显示环境：只存图、不弹窗
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["DejaVu Sans", "Droid Sans Fallback"]
plt.rcParams["axes.unicode_minus"] = False
```

**预防**：无 GUI 环境画图一律用 `Agg` + `savefig`；必须用 `font.family` **列表**（`font.sans-serif` 列表在 matplotlib 3.11 不触发按字形 fallback），英文走 DejaVu、中文落到 Droid。

## E002 TensorRT11的API变化

**现象**：照 TensorRT 8/10 老教程写 `trt_export_test.py`，连踩四个 `AttributeError`：`NetworkDefinitionCreationFlag.EXPLICIT_BATCH` 不存在、`builder.platform_has_fast_fp16` 不存在、`BuilderFlag.FP16` 不存在、`build_serialized_network` 返回的 `IHostMemory` 没有 `len()`。

**原因**：TensorRT 11 大改 Python API：EXPLICIT_BATCH 成为默认且唯一模式，`create_network()` 不再传 flag；全局 `BuilderFlag.FP16/INT8` 被移除，精度改为 per-layer（`layer.precision`），默认走 TF32；`build_serialized_network` 返回 `IHostMemory` 对象而不是 bytes。

**解决**：

```python
network = builder.create_network()              # 不传 flag，默认 explicit batch
serialized = bytes(builder.build_serialized_network(network, config))
```

**预防**：写 TensorRT 代码前先 `dir(trt.BuilderFlag)` 确认 API 存在，别照搬老博客；`execute_async_v3` 传非默认 stream（如 `torch.cuda.current_stream().cuda_stream`），否则 TensorRT 每次自己同步、性能打折。

## E003 detect模型训练pose数据任务不匹配

**现象**：用 `YOLO("yolo26n.pt")` 训练 `traffic-signs.ndjson`（`task:"pose"`），在第一个 epoch 前就停住 / 报错，一直不真正开始训练。

**原因**：数据集第一行写了 `"task":"pose"`，标注是 8 个关键点（`kpt_shape:[8,3]`），而 `yolo26n.pt` 是检测模型，只有框、没有关键点预测头。模型任务和数据任务不匹配。

**解决**：

```python
model = YOLO("yolo26n-pose.pt")   # 不是 yolo26n.pt
```

**预防**：拿到数据集先看 `task` 字段（detect / pose / segment / obb），再选对应模型；命名规律 `yolo26n.pt`（detect）/ `yolo26n-pose.pt`（pose）/ `yolo26n-seg.pt`（segment），别只看 `yolo26n`。

## E004 训练OOM内存不足dataloader workers太多

**现象**：`model.train(...)` 跑到中途被内核 OOM killer 杀掉（退出码 137）。`workers=8` 死、`workers=4` 也死（死在 epoch 7），日志里没有 Python 报错，进程直接消失。

**原因**：OOM 的是**系统内存**不是显存。WSL2 总共 7.4G，VS Code Python 服务占约 2G，训练主进程（特征图 + pin memory）加上 dataloader 每个 worker 的子进程 + 共享内存（shmem）一起超了。`dmesg` 可见 `Out of memory: Killed process ... (python)`。

**解决**：

```python
model.train(..., workers=2, batch=8)   # 默认 workers=8, batch=16
```

**预防**：区分 VRAM 与 RAM——这次显存 8G 才用 3G，满的是 7.4G 系统内存；`workers` 是并行加载子进程数，每个都占一份内存，WSL2 别用默认 8。排查用 `free -h`、`dmesg | grep -i "out of memory"`。

## E005 trtexec workspace单位写错导致build失败

**现象**：

```bash
trtexec --onnx=best.onnx --saveEngine=best.engine --memPoolSize=workspace:2048MiB
```

build 33 秒后失败，报 `Skipping tactic 0 due to insufficient memory` / `Could not find any implementation for node ...` / `Created engine with size: 0 MiB`，但显卡还有 7 GB 空闲。

**原因**：`--memPoolSize` **只认 `B/K/M/G` 后缀，不认 `MiB`**。写 `2048MiB` 时解析器取走数字 2048、忽略非法后缀，workspace 只有 **2048 字节**。日志第一行 `Memory Pools: workspace: 0.00195312 MiB` 就是证据。workspace 太小 → 候选 kernel 无法试跑 → 报「找不到实现」而不是「显存不足」。

**解决**：

```bash
trtexec --onnx=best.onnx --saveEngine=best.engine --memPoolSize=workspace:2048M
```

成功日志：`workspace: 2048 MiB`、`Engine built in 39.9 sec`、`11.5644 MiB`、`629.27 qps`、`mean 1.59 ms`。

**预防**：合法后缀 `B`（字节）/`K`（KiB）/`M`（MiB）/`G`（GiB），不写后缀默认 MiB，别写 `2GiB`；遇到 `Could not find any implementation` 先看 `Memory Pools:` 那行确认 workspace 实际大小。工具名是 `trtexec`，没有 `tensorrt_rtx`；TensorRT 11 没有 `--fp16`，精度要预先写进 ONNX。

## E006 Ultralytics导出的engine带JSON头导致反序列化失败

**现象**：用 `model.export(format="engine", quantize=16, ...)` 产出 `best.engine`，自己的 `infer_engine.py` 加载报：

```
Serialization assertion header.magicTag == kEXPECTED_MAGIC_TAG failed.
Trying to load an engine created with incompatible serialization version
(1014 != 1953657958).
```

看起来像 TensorRT 版本不匹配，但导出和推理用的是同一个 `tensorrt 11.4.0.106`。

**原因**：Ultralytics 的 `.engine` 不是纯 engine 字节，而是 `[4 字节小端 JSON 长度][JSON 元数据][真正的 ftrt engine]`，groundzero 元数据长度是 **1014 字节**。报错里的 1014 正是这个长度，被 TensorRT 当成了 magic tag 的一部分。

```
best_fp32.engine（自己 trtexec）: 6674 7274 ...      ← "ftrt" 开头
best.engine（Ultralytics）:       f603 0000 7b22 ... ← 0x3f6 = 1014 + JSON
```

**解决**：读文件时解析 4 字节长度并跳过 JSON 头：

```python
raw = path.read_bytes()
n = int.from_bytes(raw[:4], "little")   # 前 4 字节 = JSON 长度
engine = raw[4 + n :]                  # 跳过长度和 JSON，后面才是 ftrt
```

或者直接用 `YOLO("best.engine")`，Ultralytics 的 backend 会自动处理头。

**预防**：扩展名相同不代表内部格式相同——自己 trtexec 出来是裸 engine，Ultralytics 导出的是「元数据头 + engine」；报错里的魔数 1014 是 JSON 头长度，不是 TensorRT 版本号。元数据头里有 task、类别名、输入 shape，Ultralytics 推理需要；自己写 runtime 可以丢掉，但要知道它存在。
