---
tags:
  - 功能实现
  - Ultralytics
  - YOLO
  - 训练参数TrainingArgs
  - 超参数Hyperparameters
  - 数据增强Augmentation
---

# Ultralytics 训练参数全解（显式 / 隐式）· 功能实现 · N021

**时间:** 2026-10-22
**版本:** ultralytics **8.4.183**（默认值以 `ultralytics/cfg/default.yaml` 为准）
**标签:** #功能实现 #Ultralytics #YOLO #训练参数TrainingArgs #超参数Hyperparameters #数据增强Augmentation #早停EarlyStopping #优化器Optimizer
**关联:** [[N020 NDJSON数据集与YOLO姿态估计pose训练]]（pose 实战）· [[N019 TensorRT部署onnx转engine并推理]]（导出）· [[YOLO Python 用法  Ultralytics 文档]]（官方原文）

## 一句话

`model.train()` 只写你想改的参数，**没写的全部从 `default.yaml` 继承**；真正的坑不在「默认值是多少」，而在**参数之间的耦合**——`optimizer=auto` 会忽略 `lr0`、`batch` 会触发梯度累积、pose 任务的 `fliplr` 会被自动关掉。这篇把显式参数、隐式默认值和常见坑一次讲清。

## 0. 默认值从哪来、怎么查

优先级大致是：

```
model.train(**kwargs)  >  cfg="xxx.yaml"  >  ultralytics/cfg/default.yaml  >  代码内部逻辑
```

三种查法：

```bash
# ① CLI：直接打印默认配置
yolo cfg

# ② 看源码
#   ultralytics/cfg/default.yaml

# ③ Python：读成字典
python -c "from ultralytics.cfg import DEFAULT_CFG_DICT as d; print(d['fliplr'])"
```

> 注意：`default.yaml` 是**全局默认**，部分参数会被代码二次改写。最典型的是 `optimizer=auto` 会**覆盖** `lr0`（见 §3.1）。

## 1. 你现在的脚本：显式 vs 隐式

### 1.1 装甲板检测 `task2_onnx_ros2/train_yolo.py`

```python
model = YOLO("yolov8n.pt")
model.train(
    data=DATA, epochs=100, imgsz=640, batch=16,
    device=0, project=PROJECT, name=NAME,
    patience=20, seed=42, workers=2, amp=False,
)
```

| 类别 | 参数 |
| ---- | ---- |
| **显式** | `data` `epochs` `imgsz` `batch` `device` `project` `name` `patience` `seed` `workers` `amp` |
| **隐式生效** | `optimizer=auto`（→ AdamW）、`lr0` 被 auto 覆盖、`pretrained=True`、`mosaic=1.0`、**`fliplr=0.5`**、`hsv_*`、`close_mosaic=10`、`val=True`、`plots=True`、`save=True`、`deterministic=True`…… |

### 1.2 交通标志姿态 `groundzero/new.py`

```python
model = YOLO("yolo26n-pose.pt")
results = model.train(data="traffic-signs.ndjson", epochs=100,
                      imgsz=640, workers=2, batch=8)
```

| 类别 | 参数 |
| ---- | ---- |
| **显式** | `data` `epochs` `imgsz` `workers` `batch` |
| **隐式生效** | 同上；但 **`fliplr` / `flipud` 被自动置 0**（数据集没写 `flip_idx`，见 §3.7） |

> ⚠️ 两处最容易误解：
> 1. 检测脚本**没有**设置 `fliplr`，所以用的是默认 **0.5**；
> 2. pose 脚本虽然名义默认 0.5，但 Ultralytics 检测到 pose 数据缺少 `flip_idx`，会**强制关闭并打 warning**。

## 2. 参数分组总表

### 2.1 任务与数据

| 参数 | 默认 | 意义 | 使用 / 注意 |
| ---- | ---- | ---- | ---- |
| `model` | `None` | 模型：`.pt`（权重）或 `.yaml`（结构） | 微调直接给 `.pt`；从零搭网络给 `.yaml` |
| `data` | `None` | 数据集配置：`.yaml` / `.ndjson` / 目录 | 路径建议**绝对路径**，避免相对路径解析到 `datasets_dir` |
| `task` | `detect` | 任务：`detect/segment/pose/classify/obb/...` | 通常由模型或数据自动推断；**模型任务必须和数据任务一致**（E003 的坑） |
| `mode` | `train` | 运行模式 | CLI 里由子命令决定，Python 里由调用方法决定 |
| `fraction` | `1.0` | 只用一部分训练集 | `0.1` 可快速跑通流程；实现上按**等间隔**抽 `fraction` 比例，不是随机打乱后取前 N 张 |
| `single_cls` | `False` | 把所有类别合并成 1 类 | 只做「有没有目标」时用；B1/B2/R1/R2 不要开 |
| `cls_remap` | `True` | 微调换数据集时，按**类名**重映射预训练分类头 | 类名能对上时保持 True；类别语义完全不同时注意检查 |
| `pretrained` | `True` | 是否加载预训练权重 | 当 `model` 已是 `.pt` 时权重已加载；主要对 `.yaml` 模型生效 |
| `resume` | `False` | 从 `last.pt` 续训 | 传 `model=.../last.pt, resume=True`；参数会尽量沿用原训练配置 |

### 2.2 训练长度与批次

| 参数 | 默认 | 意义 | 使用 / 注意 |
| ---- | ---- | ---- | ---- |
| `epochs` | `100` | 训练轮数 | 小数据集 + 预训练通常 100~300；配合早停 |
| `time` | `None` | 最长训练小时数 | 设置后**优先于 epochs** |
| `patience` | `100` | 验证指标连续 N 轮不提升就早停 | 你的检测脚本设 20，较激进；数据少时可 30~50 |
| `batch` | `16` | batch size | `-1` = AutoBatch；`0~1` 小数 = 按显存比例；显存不够优先降 batch 或 imgsz |
| `nbs` | `64` | 名义 batch，用于**梯度累积** | 实际按 `round(nbs / batch)` 累积；batch=8 时约等于每 8 步更新一次 |
| `imgsz` | `640` | 训练/验证输入尺寸 | 必须是 stride（通常 32）的倍数；predict/export 可用 `[h, w]` |
| `rect` | `False` | 矩形批处理（不强行正方形 padding） | 训练可省显存/加速，但 batch 内尺寸需一致；验证时 `mode=val` 也可开 |
| `multi_scale` | `0.0` | 多尺度训练范围（相对 imgsz 的比例） | `0.25` 表示在 ±25% 内随机；小数据集慎用，可能让训练更抖 |

### 2.3 优化器与学习率

| 参数 | 默认 | 意义 | 使用 / 注意 |
| ---- | ---- | ---- | ---- |
| `optimizer` | `auto` | 优化器：`SGD/MuSGD/Adam/AdamW/.../auto` | `auto` 会**忽略 lr0**：迭代数 >10000 用 MuSGD(lr=0.01)，否则 AdamW(按类别数拟合 lr) |
| `lr0` | `0.01` | 初始学习率 | 只有**显式指定 optimizer** 时才按这个值用；用 auto 时改它无效 |
| `lrf` | `0.01` | 最终学习率 = `lr0 × lrf` | 配合线性/余弦衰减；想保留更多学习能力可调大（如 0.05） |
| `momentum` | `0.937` | SGD 动量 / Adam 的 β1 | 一般不动 |
| `weight_decay` | `0.0005` | L2 正则 | 过拟合时略增；太小正则弱，太大欠拟合 |
| `warmup_epochs` | `3.0` | 预热轮数 | 小数据集可 1~3；太大浪费训练 |
| `warmup_momentum` | `0.8` | 预热初始动量 | 一般不动 |
| `warmup_bias_lr` | `0.1` | 预热期 bias 学习率 | auto 优化器会把它设为 0（Adam 不适合大 bias lr） |
| `cos_lr` | `False` | 余弦学习率调度 | 长训练可开；短训练收益有限 |
| `close_mosaic` | `10` | 最后 N 轮关闭 mosaic | `0` = 一直开；小数据集建议保留 10~15，让模型最后适应真实图像分布 |

**`optimizer=auto` 的实际选择逻辑（源码 `trainer.py`）：**

```python
if iterations > 10000:
    optimizer, lr, momentum = "MuSGD", 0.01, 0.9
else:
    optimizer, lr, momentum = "AdamW", round(0.002 * 5 / (4 + nc), 6), 0.9
```

- 你的 ZLLC 280 张、batch 16、100 epoch → 迭代数远小于 10000 → 实际是 **AdamW**。
- 所以「默认 lr0=0.01」在你的脚本里**并没有生效**，别再手动把 lr0 设成 0.01 后奇怪为什么没变化。

### 2.4 精度、显存与速度

| 参数 | 默认 | 意义 | 使用 / 注意 |
| ---- | ---- | ---- | ---- |
| `device` | `None` | 设备：`0` / `[0,1]` / `cpu` / `mps` | WSL2 用 `device=0`；多卡传列表 |
| `workers` | `8` | DataLoader 进程数 | **WSL2 内存杀手**；OOM 时先降到 2~4（你的 E004） |
| `cache` | `False` | 缓存图像到 RAM/磁盘 | `True`/`'ram'` 快但吃内存；`'disk'` 折中 |
| `amp` | `True` | 自动混合精度（FP16） | 省显存、加速；`False` 更稳但更慢更吃显存。你的脚本关 AMP 是为了跳过 AMP 自检下载 |
| `compile` | `False` | `torch.compile` | 首次编译慢，环境不兼容时可能直接报错；教学/小数据不建议开 |
| `channels_last` | `None` | 内存格式优化 | 非 Windows CUDA 通常自动开，不用手设 |
| `profile` | `False` | 训练时顺带 profile ONNX/TensorRT 速度 | 只在做部署性能对比时开 |
| `seed` | `0` | 随机种子 | 复现实验要固定；但 GPU 算子仍可能有非确定性 |
| `deterministic` | `True` | 确定性算子 | 可复现但可能更慢；追求速度可设 False |
| `verbose` | `True` | 打印详细日志 | 批量跑实验可关 |

### 2.5 数据增强（重点）

| 参数 | 默认 | 意义 | 使用 / 注意 |
| ---- | ---- | ---- | ---- |
| `hsv_h` | `0.015` | 色相抖动（占色环比例） | ±1.5% ≈ ±5.4°；**红/蓝装甲板类别**慎调大，可能把 B 染成 R |
| `hsv_s` | `0.7` | 饱和度抖动 | 光照变化大时可保留 |
| `hsv_v` | `0.4` | 亮度抖动 | 室内/室外混合可保留 |
| `degrees` | `0.0` | 旋转角度 ± | 装甲板可加 5~10°；**方向类任务**（左/右/上/下）别开大，否则标签语义会错 |
| `translate` | `0.1` | 平移比例 ± | 目标可能出画时注意 |
| `scale` | `0.5` | 缩放增益 ± | 默认相当于 [0.5, 1.5]；小目标数据集慎用大 scale |
| `shear` | `0.0` | 剪切 ± 度 | 一般不动 |
| `perspective` | `0.0` | 透视变换 | 车载/斜视角可加 0.0005 左右 |
| `flipud` | `0.0` | 垂直翻转概率 | 交通标志「上/下」任务**必须 0**；普通检测也通常 0 |
| `fliplr` | **`0.5`** | **水平翻转概率** | 检测默认生效；pose 无 `flip_idx` 时自动禁用；方向类任务必须 0 |
| `bgr` | `0.0` | RGB↔BGR 通道交换概率 | 训练/推理通道顺序不一致时才考虑，正常不要开 |
| `mosaic` | `1.0` | 4 图拼接概率 | 小目标/小数据集可降到 0.5~0.8；最后 `close_mosaic` 轮关闭 |
| `mixup` | `0.0` | MixUp 概率 | 小数据集可试 0.1~0.2；分类/检测语义可能变糊 |
| `cutmix` | `0.0` | CutMix 概率 | 同上，默认关 |
| `copy_paste` | `0.0` | 复制粘贴增强 | **仅 segment/semantic/obb**；检测任务不适用 |
| `copy_paste_mode` | `flip` | copy-paste 策略 | 仅上述任务 |
| `auto_augment` | `randaugment` | 分类自动增广策略 | **仅 classify** |
| `erasing` | `0.4` | 随机擦除概率 | **仅 classify** |
| `augmentations` | `None` | 自定义 Albumentations 变换 | 需要更复杂增广时用；注意与内置增广叠加 |

> **一句话原则：** 增广要**保持标签语义不变**。方向、颜色类别、左右关系，是三个最容易翻车的地方。

### 2.6 损失权重

| 参数 | 默认 | 适用 | 意义 |
| ---- | ---- | ---- | ---- |
| `box` | `7.5` | detect/pose/segment | 框回归损失权重 |
| `cls` | `0.5` | 分类头 | 分类损失权重 |
| `dfl` | `1.5` | detect | Distribution Focal Loss 权重（YOLO26 的 DFL-free 头则退化为 L1） |
| `pose` | `12.0` | pose | 关键点损失权重 |
| `kobj` | `1.0` | pose | 关键点 objectness 权重 |
| `rle` | `1.0` | pose | RLE 损失权重 |
| `angle` | `1.0` | obb | 角度损失权重 |
| `dlog` / `dgrad` / `dlam` | `1.0` / `0.5` / `1.0` | depth | 深度损失相关 |
| `cls_pw` | `0.0` | 分类头 | 类别权重幂次，处理类别不平衡；0=关闭 |

> 损失权重是**最后才动**的参数。先调数据、增广、学习率；直接改 loss gain 很容易把训练搞崩。

### 2.7 验证、保存与日志

| 参数 | 默认 | 意义 | 使用 / 注意 |
| ---- | ---- | ---- | ---- |
| `val` | `True` | 训练中每轮验证 | 没有 val 集时设 False，否则会报错/指标无意义 |
| `split` | `val` | 验证用哪个 split | 可设 `test` / `train` |
| `conf` | `None` | 置信度阈值 | **val 默认 0.001，predict 默认 0.25**；不传就用各自默认 |
| `iou` | `0.7` | NMS 的 IoU 阈值 | 密集目标可调低，稀疏可调高 |
| `max_det` | `300` | 每图最多检测数 | 小目标密集场景可调大 |
| `save` | `True` | 保存 checkpoint 和预测结果 | 关掉可省磁盘，但没法 resume |
| `save_period` | `-1` | 每 N 轮存一次 | `-1` 只在最后/最佳保存；想留中间权重设 10 |
| `plots` | `True` | 保存训练曲线、混淆矩阵等 | 长时间实验可关，省时间/磁盘 |
| `save_json` | `False` | 保存 COCO JSON | 需要外部评估时开 |
| `exist_ok` | `False` | 允许覆盖同名 run | False 时会自动建 `train2/train3`；你的 `train-4` 就是这么来的 |
| `project` / `name` | `None` | 输出根目录 / 实验名 | 建议显式指定，方便找权重 |

### 2.8 导出 / 推理相关（顺带）

| 参数 | 默认 | 意义 | 注意 |
| ---- | ---- | ---- | ---- |
| `format` | `torchscript` | 导出格式 | 你用 `onnx` |
| `opset` | `None` | ONNX opset | 你用 17；TensorRT/OpenCV DNN 兼容性要试 |
| `simplify` | `True` | ONNX 图简化 | 一般保持 True |
| `dynamic` | `False` | 动态 shape | 需要变尺寸输入时开；会降低部分后端优化 |
| `quantize` | `None` | 量化精度（新参数，替代 `half/int8`） | `16/fp16`、`8/int8` 等 |
| `nms` | `None` | 是否把 NMS 嵌入导出模型 | `True` 嵌入；C++ 侧自己写 NMS 时保持默认 |
| `augment` | `False` | 推理时 TTA | 开=更准但更慢；实时 ROS2 节点不要开 |
| `agnostic_nms` | `False` | 类别无关 NMS | 多类别互相遮挡时可能有用 |
| `classes` | `None` | 只保留指定类别 | 部署时过滤用 |

## 3. 参数之间的耦合（真正的坑）

### 3.1 `optimizer=auto` × `lr0`

- `auto` 会打印：`'optimizer=auto' found, ignoring 'lr0=...'`。
- 迭代数 ≤10000 → **AdamW + 拟合 lr**；>10000 → **MuSGD + lr=0.01**。
- 想完全掌控学习率：显式写 `optimizer="SGD"` 或 `"AdamW"`，再配 `lr0`。

### 3.2 `batch` × `nbs` → 梯度累积

- 有效 batch ≈ `nbs=64`，不是你的 `batch=16`。
- `batch=8` 时累积 8 步才更新一次；这会影响**学习率与训练步数的关系**。
- 显存不够时，降 batch 是安全的；但训练动态会变，必要时同步调 `lr0`。

### 3.3 `imgsz` × stride

- 必须是 stride（通常 32）的倍数，否则内部会取整/报错。
- 训练用 `640`，导出/推理也要用同一尺寸（或支持 dynamic），否则精度/速度对不上。

### 3.4 `amp` × `batch` × 显存

- AMP 省显存，通常能开大一档 batch。
- 你的脚本 `amp=False` 是为了跳过 AMP 自检时的模型下载；小数据集 FP32 够用。
- WSL2 显存/内存都紧张时，优先顺序：**降 workers → 降 batch → 降 imgsz → 关 cache**。

### 3.5 `workers` × WSL2

- 默认 8，在 WSL2 上很容易把内存打满（E004）。
- 你现在用 2，是合理的；排查 dataloader 问题时可以临时 `workers=0`（主进程加载，慢但好调试）。

### 3.6 `mosaic` × `close_mosaic`

- `mosaic=1.0` 前 90 轮一直拼图，最后 `close_mosaic=10` 轮关掉，让模型适应真实分布。
- 小数据集如果 mosaic 太强，模型可能学到「拼图伪影」；可降到 0.5~0.8。
- `close_mosaic=0` = 不关；`epochs` 很短时注意别把 close 阶段挤没。

### 3.7 `fliplr` × `flip_idx`（pose 专属）

Ultralytics 源码逻辑：

```python
flip_idx = dataset.data.get("flip_idx", [])
if len(flip_idx) == 0 and (hyp.fliplr > 0.0 or hyp.flipud > 0.0):
    hyp.fliplr = hyp.flipud = 0.0
    LOGGER.warning("No 'flip_idx' array defined in data.yaml, disabling 'fliplr' and 'flipud' augmentations.")
```

- pose 数据必须提供长度为 `kpt_shape[0]` 的 `flip_idx`，告诉它「翻转后第 i 个关键点应该变成第几个」。
- 你的交通标志数据集 8 个关键点、类别含 **Left/Right**，没有 `flip_idx` → 自动禁用是正确行为。
- 如果强行加 `flip_idx` 但映射写错，关键点会错位，比不开更糟。

### 3.8 `pretrained` × 类别数

- 用 `.pt` 微调时，分类头会按新数据集的 `nc` 重建；主干权重保留。
- `cls_remap=True` 会尝试按**类名**匹配旧分类头；类名对不上时不要指望它。
- 类别数变化后，`model.model.names` 会更新；导出 ONNX 时输出维度也随之变化。

### 3.9 `freeze` × BatchNorm

- `freeze=N` 只把前 N 层的 `requires_grad` 设为 False。
- BN 层在 train 模式下 running stats **仍可能更新**；真要完全冻结，需要额外把 BN 设为 eval（Ultralytics 不自动做）。
- 小数据集微调时，`freeze=10` 可减少过拟合，但别冻到只剩分类头。

### 3.10 `patience` × `epochs`

- 早停看的是验证 fitness（通常是 mAP 之类），不是 train loss。
- `patience=20` + `epochs=100` 意味着最多 100 轮，但可能 20 轮不涨就停；小数据集波动大，太激进会错过后期提升。
- `patience=0` 通常表示关闭早停（跑满 epochs）。

### 3.11 `val` / `plots` / `save` × 磁盘与时间

- 默认三个都开；每个 run 会存权重、曲线、混淆矩阵、验证图。
- 快速扫参时可设 `plots=False, save=False`（但这样就没法 resume / 看 best.pt）。
- `save_period` 设正数会成倍增加磁盘占用。

### 3.12 `exist_ok` × run 目录

- 默认 False：同名 run 会自动变成 `train2`、`train3`……你的 `train-4` 就是多次重跑的结果。
- 想覆盖：`exist_ok=True`；但会**丢掉上一次的权重**，慎用。

## 4. 针对你两个任务的推荐配置

### 4.1 装甲板检测（ZLLC，280 张，4 类）

```python
model.train(
    data=DATA,
    epochs=150,
    imgsz=640,
    batch=16,
    device=0,
    workers=2,
    amp=False,
    patience=30,          # 比 20 稍宽松，小数据集波动大
    seed=42,
    optimizer="auto",     # 实际会选 AdamW；想固定就显式写
    fliplr=0.5,           # B1/B2/R1/R2 水平翻转通常安全；若类别含左右语义则改 0
    hsv_h=0.0,            # 红/蓝是类别核心特征，别把色相抖没了
    hsv_s=0.5,
    hsv_v=0.4,
    degrees=5.0,          # 小角度旋转，模拟安装/视角误差
    scale=0.3,            # 默认 0.5 对小目标偏强
    mosaic=0.8,
    close_mosaic=15,
    plots=True,
)
```

**为什么：**
- 数据少 → 增广是主要正则，但**不能破坏类别语义**（颜色、左右）。
- 小目标 → 别用太猛的 scale/mosaic。
- `close_mosaic` 留够轮数，让模型最后见到真实单图分布。

### 4.2 交通标志姿态（6 类含方向，8 关键点）

```python
model.train(
    data="traffic-signs.ndjson",
    epochs=100,
    imgsz=640,
    batch=8,
    workers=2,
    amp=False,
    patience=30,
    seed=42,
    fliplr=0.0,           # 必须关：Left/Right 会翻反
    flipud=0.0,           # 必须关：Up/Down 会翻反
    degrees=10.0,         # 只做小角度；90° 会把 Left 转成 Up
    scale=0.3,
    mosaic=0.5,
    close_mosaic=10,
)
```

**为什么：**
- 类别本身就是**方向语义**，水平/垂直翻转等于改标签。
- 旋转同理：小角度是视角扰动，大角度会改变「左/右/上/下」的含义。
- 如果要开翻转，必须先定义正确的 `flip_idx`，并确认类别映射也一致（例如 Left↔Right 是否要互换标签——Ultralytics 不会自动改类别）。

## 5. 常见坑清单

1. **`optimizer=auto` 下改 `lr0` 无效**——看日志确认实际优化器和 lr。
2. **pose 的 `fliplr` 被静默关闭**——不是没生效，是缺少 `flip_idx`。
3. **方向类任务开翻转/大旋转**——标签语义被破坏，mAP 看着还行但方向全错。
4. **红/蓝类别开大 `hsv_h`**——颜色是类别特征，色相抖动可能制造错标。
5. **WSL2 OOM**——先降 `workers`，再降 `batch`，再降 `imgsz`；`cache=True` 最吃内存。
6. **AMP 自检下载模型**——离线/网络差时 `amp=False` 可跳过（你的做法）。
7. **`patience` 太小**——小数据集 val 曲线抖，20 轮可能过早停。
8. **`exist_ok=False` 产生一堆 `train2/train3`**——找 best.pt 时别拿错目录。
9. **`imgsz` 不是 32 的倍数**——内部取整，导出/推理尺寸对不上。
10. **模型任务与数据任务不一致**——detect 模型训 pose 数据会直接报错（E003）。
11. **`freeze` 以为 BN 也冻了**——BN running stats 仍可能更新。
12. **`single_cls=True` 误开**——4 类变 1 类，指标全变。
13. **`val=False` 但没有 val 集**——训练能跑，指标/早停失效。
14. **`augment=True` 用在实时推理**——TTA 让 FPS 掉一大截。
15. **`half=True` 已过时**——新版本用 `quantize=16`。
16. **数据 yaml 用相对路径**——可能相对 `datasets_dir` 而不是脚本目录，找不到图。

## 6. 最小改动示例

**命令行：**

```bash
yolo train model=yolov8n.pt data=data.yaml epochs=100 imgsz=640 batch=16 \
  workers=2 amp=False fliplr=0.0 mosaic=0.8
```

**Python（推荐，和你现有脚本一致）：**

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(
    data="data.yaml",
    epochs=100,
    imgsz=640,
    batch=16,
    workers=2,
    amp=False,
    fliplr=0.0,      # 按任务决定
)
metrics = model.val()          # 单独验证
model.export(format="onnx", imgsz=640, opset=17)
```

**查当前 run 用了哪些参数：**

```python
print(model.trainer.args)      # 训练后
# 或直接看 runs/.../args.yaml
```

> `runs/<task>/<name>/args.yaml` 是**最可靠的复盘依据**：它记录的是最终生效值（包括 auto 优化器改写后的 lr0）。

## 7. 一页总结

- **默认值**：以 `ultralytics/cfg/default.yaml` 为准；`yolo cfg` 可打印。
- **最该记住的默认**：`epochs=100`、`batch=16`、`imgsz=640`、`workers=8`、`amp=True`、`mosaic=1.0`、`fliplr=0.5`、`close_mosaic=10`、`patience=100`、`optimizer=auto`。
- **三个高频坑**：auto 优化器忽略 lr0；pose 无 flip_idx 自动关翻转；方向/颜色类任务的增广破坏语义。
- **调参顺序**：数据与标签 → 增广语义 → 显存/速度（workers/batch/imgsz/amp）→ 学习率/轮数 → 最后才动 loss 权重。
