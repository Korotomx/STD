---
tags:
  - 功能实现
  - NDJSON
  - YOLO
  - pose姿态估计
  - 数据集
  - 关键点keypoint
---

# NDJSON 数据集与 YOLO 姿态估计（pose）训练 · 功能实现 · N020

**时间:** 2026-10-22
**标签:** #功能实现 #NDJSON #YOLO #pose姿态估计 #数据集 #关键点keypoint
**关联:** [[N015 数据加载Dataset与DataLoader]]（数据加载）· [[N016 训练循环五步闭环]]（训练流程）· [[YOLO Python 用法  Ultralytics 文档]]（官方文档原文）

## 实际情况

跟 ultralytics 官方文档学 NDJSON 数据集：`groundzero/traffic-signs.ndjson` 是「交通标志朝向」数据集（拍纸牌做的左/右/上/下箭头 + 停 + 限速标志），用 `yolo26n-pose.pt` 训练 100 epoch，最后**框 mAP50 99.3%、姿态 mAP50 99.3%**（产物 `runs/pose/train-4/weights/best.pt`，6.4MB）。

## 1. NDJSON 数据集格式

每行一个 JSON，两种 `type`：

```json
{"type":"dataset","task":"pose","class_names":{"0":"Left","1":"Right",...},"kpt_shape":[8,3]}
{"type":"image","file":"xx.jpg","url":"https://...","width":960,"height":1280,
 "split":"train","annotations":{"pose":[[classId, cx, cy, w, h, kp1x, kp1y, kp1v, ...]]}}
```

- `task` 决定任务类型：`detect`（框）/ `pose`（框+关键点）/ `segment`（分割）……
- 每张图 `pose` 里一行 = `[classId, cx, cy, w, h, 8×(x, y, 可见性)]`，**坐标全部归一化 [0,1]**，可见性 0=不可见 / 2=可见
- `kpt_shape:[8,3]` = 8 个关键点、每点 3 维（x, y, 可见性）
- 图片在 `url`（远端 CDN），首次训练自动下载到 `datasets/` 缓存

## 2. 训练（流程跟普通 YAML 数据集一样）

```python
from ultralytics import YOLO
model = YOLO("yolo26n-pose.pt")   # 关键：pose 任务必须用 pose 模型
model.train(data="traffic-signs.ndjson", epochs=100, imgsz=640, workers=2, batch=8)
```

ultralytics 读 NDJSON 后自动转成 YOLO 标签格式并生成 data.yaml，之后的训练循环和普通数据集完全一致（见 [[N016 训练循环五步闭环]]）。

## 3. 结果

| 指标 | epoch 100 |
| ---- | ---- |
| 框 mAP50 / mAP50-95 | 99.3% / 88.6% |
| 姿态 mAP50 / mAP50-95 | 99.3% / 97.4% |

## 思考

（留白 —— 这个数据集只有 480 训练 + 117 验证张图，为什么能训到 99%？是任务本身简单（纸牌朝向、特征明显）还是 YOLO26 预训练权重够强？换更难的姿态数据集会掉到多少？）

## 总结

**本质：** NDJSON 是新式数据集格式，`task` 字段标明任务类型（detect/pose/…）；训练时**模型任务必须和数据集 `task` 对上**（pose 数据用 `yolo26n-pose.pt`），其余流程与普通训练一致；关键点坐标归一化、每点 [x, y, 可见性] 三元组。
**标签:** #功能实现 #NDJSON #YOLO #pose姿态估计 #数据集 #关键点keypoint
