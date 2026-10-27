Ultralytics 的 `model.train()` 只写想改的参数，其余全从 `default.yaml` 继承；真正的坑不在默认值，而在参数耦合（auto 优化器忽略 lr0、batch 触发梯度累积、pose 的翻转被自动关闭）。这篇先讲 NDJSON 数据集和 pose 训练，再把训练参数按组过一遍。

## NDJSON 数据集

`groundzero/traffic-signs.ndjson` 是「交通标志朝向」数据集（左/右/上/下箭头 + 停 + 限速），每行一个 JSON，两种 `type`：

```json
{"type":"dataset","task":"pose","class_names":{"0":"Left","1":"Right"},
 "kpt_shape":[8,3]}
{"type":"image","file":"xx.jpg","url":"https://...","width":960,"height":1280,
 "split":"train","annotations":{"pose":[[classId, cx, cy, w, h, kp1x, kp1y, kp1v, ...]]}}
```

- `task` 决定任务类型：`detect`（框）/ `pose`（框+关键点）/ `segment`（分割）
- 每行 `pose` = `[classId, cx, cy, w, h, 8×(x, y, 可见性)]`，**坐标全部归一化 [0,1]**，可见性 0=不可见 / 2=可见
- `kpt_shape:[8,3]` = 8 个关键点，每点 3 维
- 图片在 `url`，首次训练自动下载到 `datasets/` 缓存

### 最小训练

```python
from ultralytics import YOLO

model = YOLO("yolo26n-pose.pt")   # 关键：pose 任务必须用 pose 模型
model.train(data="traffic-signs.ndjson", epochs=100, imgsz=640, workers=2, batch=8)
```

ultralytics 读 NDJSON 后自动转成 YOLO 标签并生成 data.yaml，之后流程与普通数据集一致（训练循环见 [[N015 数据加载Dataset与DataLoader]]）。

### 结果

| 指标 | epoch 100 |
| ---- | ---- |
| 框 mAP50 / mAP50-95 | 99.3% / 88.6% |
| 姿态 mAP50 / mAP50-95 | 99.3% / 97.4% |

只有 480 训练 + 117 验证张图却能到 99%，主要是任务简单（纸牌朝向、特征明显）+ 预训练权重强。

## 训练参数

默认值优先级：

```
model.train(**kwargs) > cfg="xxx.yaml" > ultralytics/cfg/default.yaml > 代码内部逻辑
```

查法：`yolo cfg`、看 `ultralytics/cfg/default.yaml`、或 `from ultralytics.cfg import DEFAULT_CFG_DICT`。`default.yaml` 是全局默认，部分参数会被代码二次改写（最典型 `optimizer=auto` 覆盖 `lr0`）。

**最该记住的默认**：`epochs=100`、`batch=16`、`imgsz=640`、`workers=8`、`amp=True`、`mosaic=1.0`、`fliplr=0.5`、`close_mosaic=10`、`patience=100`、`optimizer=auto`。

### 任务与数据

| 参数 | 默认 | 意义 / 注意 |
| ---- | ---- | ---- |
| `model` | None | `.pt` 微调，`.yaml` 从零搭 |
| `data` | None | `.yaml` / `.ndjson` / 目录；建议绝对路径 |
| `task` | detect | detect/segment/pose/classify/obb；**模型任务必须和数据任务一致** |
| `fraction` | 1.0 | 只用一部分训练集，按等间隔抽，不是随机取前 N |
| `single_cls` | False | 合并成 1 类，只判「有没有目标」时用 |
| `cls_remap` | True | 换数据集时按类名重映射预训练分类头 |
| `pretrained` | True | `model` 已是 `.pt` 时权重已加载；主要对 `.yaml` 生效 |
| `resume` | False | 传 `last.pt, resume=True` 续训，尽量沿用原配置 |

### 训练长度与批次

| 参数 | 默认 | 意义 / 注意 |
| ---- | ---- | ---- |
| `epochs` | 100 | 小数据集 + 预训练通常 100~300 |
| `time` | None | 最长小时数，设置后优先于 epochs |
| `patience` | 100 | 验证指标连续 N 轮不升就早停；小数据 30~50 |
| `batch` | 16 | `-1`=AutoBatch，`0~1`=按显存比例 |
| `nbs` | 64 | 名义 batch，用于梯度累积 `round(nbs/batch)` |
| `imgsz` | 640 | 必须是 stride（通常 32）的倍数 |
| `rect` | False | 矩形批处理，省显存但 batch 内尺寸需一致 |
| `multi_scale` | 0.0 | 多尺度训练范围，小数据集慎用 |

### 优化器与学习率

| 参数 | 默认 | 意义 / 注意 |
| ---- | ---- | ---- |
| `optimizer` | auto | **auto 会忽略 lr0**：迭代 >10000 用 MuSGD(lr=0.01)，否则 AdamW(拟合 lr) |
| `lr0` | 0.01 | 只有显式指定 optimizer 时才生效 |
| `lrf` | 0.01 | 最终 lr = `lr0 × lrf` |
| `momentum` | 0.937 | SGD 动量 / Adam β1 |
| `weight_decay` | 0.0005 | L2 正则 |
| `warmup_epochs` | 3.0 | 预热轮数，小数据 1~3 |
| `warmup_bias_lr` | 0.1 | auto 优化器会设为 0 |
| `cos_lr` | False | 余弦调度，长训练可开 |
| `close_mosaic` | 10 | 最后 N 轮关 mosaic；0=一直开 |

`optimizer=auto` 的实际逻辑（`trainer.py`）：

```python
if iterations > 10000:
    optimizer, lr, momentum = "MuSGD", 0.01, 0.9
else:
    optimizer, lr, momentum = "AdamW", round(0.002 * 5 / (4 + nc), 6), 0.9
```

ZLLC 280 张、batch 16、100 epoch → 迭代数远小于 10000 → 实际是 **AdamW**，默认 `lr0=0.01` 没生效。

### 精度、显存与速度

| 参数 | 默认 | 意义 / 注意 |
| ---- | ---- | ---- |
| `device` | None | `0` / `[0,1]` / `cpu`；WSL2 用 `device=0` |
| `workers` | 8 | **WSL2 内存杀手**，OOM 先降 2~4 |
| `cache` | False | `True`/`'ram'` 快但吃内存，`'disk'` 折中 |
| `amp` | True | 省显存加速；`False` 更稳但慢，且可跳过 AMP 自检下载 |
| `compile` | False | 首次编译慢，环境不兼容会直接报错 |
| `seed` | 0 | 复现要固定，但 GPU 算子仍可能不确定 |
| `deterministic` | True | 可复现但可能更慢 |

### 数据增强

| 参数 | 默认 | 意义 / 注意 |
| ---- | ---- | ---- |
| `hsv_h` | 0.015 | 色相抖动 ±1.5%；红/蓝是类别核心特征时改 0 |
| `hsv_s` / `hsv_v` | 0.7 / 0.4 | 饱和度 / 亮度抖动 |
| `degrees` | 0.0 | 旋转；方向类任务别开大，90° 会改语义 |
| `translate` / `scale` | 0.1 / 0.5 | 平移 / 缩放（默认约 [0.5,1.5]） |
| `shear` / `perspective` | 0.0 / 0.0 | 剪切 / 透视 |
| `flipud` | 0.0 | 垂直翻转；「上/下」任务必须 0 |
| `fliplr` | **0.5** | 水平翻转；pose 无 `flip_idx` 时自动禁用 |
| `bgr` | 0.0 | RGB↔BGR 交换，正常不要开 |
| `mosaic` | 1.0 | 4 图拼接；小目标/小数据可降 0.5~0.8 |
| `mixup` / `cutmix` | 0.0 / 0.0 | 小数据可试 0.1~0.2 |
| `copy_paste` | 0.0 | 仅 segment/semantic/obb |
| `auto_augment` / `erasing` | randaugment / 0.4 | 仅 classify |

原则：增广要**保持标签语义不变**。方向、颜色类别、左右关系是最容易翻车的三处。

### 损失权重

`box=7.5`（框）、`cls=0.5`（分类）、`dfl=1.5`（检测）、`pose=12.0`、`kobj=1.0`、`rle=1.0`（pose）、`angle=1.0`（obb）。损失权重是**最后才动**的参数，先调数据、增广、学习率。

### 验证、保存与日志

| 参数 | 默认 | 意义 / 注意 |
| ---- | ---- | ---- |
| `val` | True | 每轮验证；没有 val 集设 False |
| `split` | val | 用哪个 split 验证 |
| `conf` / `iou` | None / 0.7 | val 的 conf 默认 0.001，predict 默认 0.25 |
| `max_det` | 300 | 每图最多检测数 |
| `save` | True | 存 checkpoint 和预测；关了没法 resume |
| `save_period` | -1 | 每 N 轮存一次 |
| `plots` | True | 曲线、混淆矩阵等 |
| `exist_ok` | False | 同名 run 自动变 `train2/train3`（`train-4` 就是这么来的） |
| `project` / `name` | None | 输出根目录 / 实验名，建议显式指定 |

### 导出 / 推理相关

`format=torchscript`（导出格式）、`opset=None`、`simplify=True`、`dynamic=False`、`quantize=None`（16/8）、`nms=None`、`augment=False`、`agnostic_nms=False`、`classes=None`。新版本用 `quantize=16`，`half=True` 已过时。

## 参数耦合（真正的坑）

- **`optimizer=auto` × `lr0`**：auto 打印 `ignoring 'lr0=...'`；要完全掌控就显式 `optimizer="AdamW"` 再配 `lr0`。
- **`batch` × `nbs`**：有效 batch ≈ 64，不是 16；`batch=8` 时累积 8 步更新一次，训练动态会变。
- **`imgsz` × stride**：必须是 32 的倍数；训练/导出/推理尺寸要一致。
- **`amp` × 显存**：WSL2 紧张时优先顺序 **降 workers → 降 batch → 降 imgsz → 关 cache**。
- **`mosaic` × `close_mosaic`**：最后 10 轮关掉让模型适应真实分布；太强可能学到拼图伪影。
- **`fliplr` × `flip_idx`（pose）**：

```python
flip_idx = dataset.data.get("flip_idx", [])
if len(flip_idx) == 0 and (hyp.fliplr > 0.0 or hyp.flipud > 0.0):
    hyp.fliplr = hyp.flipud = 0.0
    LOGGER.warning("No 'flip_idx' array defined ... disabling ...")
```

pose 数据要提供长度 `kpt_shape[0]` 的 `flip_idx`，告诉程序翻转后第 i 个点变成第几个；映射写错比不开更糟。

- **`pretrained` × 类别数**：换数据集时分类头按 `nc` 重建，主干保留；`cls_remap` 按类名匹配，对不上时别指望。
- **`freeze` × BatchNorm**：`freeze=N` 只关前 N 层 `requires_grad`，BN 的 running stats 仍可能更新。
- **`patience` × `epochs`**：早停看验证 fitness，不看 train loss；小数据波动大，20 轮可能过早停。
- **`val`/`plots`/`save`**：默认全开，扫参时可关 `plots/save`（但没法 resume）。
- **`exist_ok=False`**：产生一堆 `train2/train3`，找 best.pt 时别拿错目录。

## 两个任务的推荐配置

装甲板检测（ZLLC，280 张，4 类）：

```python
model.train(
    data=DATA, epochs=150, imgsz=640, batch=16, device=0,
    workers=2, amp=False, patience=30, seed=42,
    fliplr=0.5,          # 类别无左右语义时安全
    hsv_h=0.0,           # 红/蓝是类别核心特征
    hsv_s=0.5, hsv_v=0.4,
    degrees=5.0, scale=0.3, mosaic=0.8, close_mosaic=15,
    plots=True,
)
```

交通标志姿态（6 类含方向，8 关键点）：

```python
model.train(
    data="traffic-signs.ndjson", epochs=100, imgsz=640, batch=8,
    workers=2, amp=False, patience=30, seed=42,
    fliplr=0.0,          # Left/Right 会翻反
    flipud=0.0,          # Up/Down 会翻反
    degrees=10.0,        # 90° 会把 Left 转成 Up
    scale=0.3, mosaic=0.5, close_mosaic=10,
)
```

方向类任务的增广不能破坏语义；要开翻转必须先定义正确的 `flip_idx`，并确认类别映射是否也要互换（Ultralytics 不会自动改类别标签）。

## 坑与边界

1. auto 优化器下改 `lr0` 无效，看日志确认实际优化器和 lr。
2. pose 的 `fliplr` 被静默关闭——不是没生效，是缺 `flip_idx`。
3. 方向/颜色类任务开大翻转、旋转、色相抖动，mAP 看着还行但方向/颜色全错。
4. WSL2 OOM 先降 `workers`，再 batch/imgsz；`cache=True` 最吃内存。
5. `amp=False` 可跳过 AMP 自检的模型下载。
6. `patience` 太小会错过后期提升。
7. 模型任务与数据任务不一致会直接报错（见 [[错误记录#E003 detect模型训练pose数据任务不匹配|E003]]）。
8. `val=False` 但没有 val 集，指标/早停失效。
9. 数据 yaml 用相对路径，可能相对 `datasets_dir` 而不是脚本目录。

复盘看 `runs/<task>/<name>/args.yaml`，它记录最终生效值（包括 auto 优化器改写后的 lr0）。

## 总结

NDJSON 用 `task` 字段标明 detect/pose/segment，pose 标注是 `[classid, cx, cy, w, h, 8×(x,y,vis)]` 全归一化；模型任务必须和数据一致。`model.train()` 只写想改的参数，默认全从 `default.yaml` 继承。三个高频坑：auto 优化器忽略 lr0、pose 缺 `flip_idx` 自动关翻转、方向/颜色类任务的增广破坏语义。调参顺序：数据与标签 → 增广语义 → 显存/速度（workers/batch/imgsz/amp）→ 学习率/轮数 → 最后才动 loss 权重。