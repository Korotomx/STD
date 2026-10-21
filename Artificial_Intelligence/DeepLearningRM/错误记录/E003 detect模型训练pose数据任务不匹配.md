# E003 · 运行时 — detect 模型训练 pose 数据：任务不匹配

**时间:** 2026-10-22
**分类:** #运行时

## 问题

用 `YOLO("yolo26n.pt")`（检测模型）训练 `traffic-signs.ndjson`（`task:"pose"` 的交通标志朝向数据集），训练在第一个 epoch 前就停住 / 报错，一直不真正开始训练。

## 原因

数据集第一行就写了 `"task":"pose"`，标注是 **8 个关键点**（`kpt_shape:[8,3]`），而 `yolo26n.pt` 是**检测模型**——只有框、没有关键点预测头。检测模型去训姿态数据 = 任务不匹配，模型和数据对不上。

## 解决方案

换同系列的 **pose 模型**：

```python
model = YOLO("yolo26n-pose.pt")   # 不是 yolo26n.pt
```

要点：

- **拿到数据集先看它的 `task` 字段**（detect / pose / segment / obb / …），再选对应模型
- 模型命名规律：`yolo26n.pt`（detect）/ `yolo26n-pose.pt`（pose）/ `yolo26n-seg.pt`（分割），别只看「yolo26n」就选
