---
tags:
  - 目标检测ObjectDetection
  - 语义分割Segmentation
  - 评价指标Metric
  - IoU交并比
  - NMS非极大值抑制
---

# IoU 交并比 · 检测与分割的评价指标

**时间:** 2026-10-23 整理
**来源:** [Intersection Over Union (IoU) in Object Detection & Segmentation](https://www.youtube.com/watch?v=RgQbweTwrkU)（YouTube，LearnOpenCV，2023-07-31）
**原文:** [[Intersection Over Union (IoU) in Object Detection &  Segmentation]]
**标签:** #目标检测ObjectDetection #语义分割Segmentation #评价指标Metric #IoU交并比 #NMS非极大值抑制
**关联:** [[L1 深度学习基础]]（分类指标 → 检测指标）· [[DeepLearningRM/主页|DeepLearningRM · 目标检测]]（ZLLC / groundzero 里的框与关键点评估）

## 一句话

IoU = **交集面积 / 并集面积**，取值 $[0,1]$：0 完全不重叠，1 完全重合。检测里它是「框质量」的尺子，配合阈值 $\alpha$ 把预测分成 TP / FP；分割里它直接是**主指标**（逐像素算，没有矩形也没有阈值）。核心计算只有一个技巧：**交集宽高分别取 max/min，再 clamp 到 0**。

## 实际情况

### 0. 为什么需要 IoU

目标检测输出一堆框，要评价「框得准不准」。只看「有没有重叠」不够——重叠面积相同的两个预测，**框得越大越吃亏**（分母里并集变大）。IoU 同时惩罚「漏框」和「画出多余的边」。

### 1. 定义与直觉

$$
\mathrm{IoU}=\frac{|A\cap B|}{|A\cup B|}
=\frac{\text{交集面积}}{\text{真值面积}+\text{预测面积}-\text{交集面积}}
$$

视频的例子（鸟）：

- 模型 A 重叠多 → 直觉上最好；
- 模型 C 甚至把**树枝**也框进去了 → 交集可能更大，但**并集也更大**，IoU 反而可能低于 A。

**结论：IoU 奖励「贴合」，惩罚「框大」**。这就是它比「只看交集」公平的地方。

### 2. 检测里：IoU 是「辅助指标」

IoU 本身不是最终指标（最终看 mAP / Recall / Loss），它扮演的是**判定的尺子**：

- 给定阈值 $\alpha$（常用 0.5），逐个预测框算 IoU 并与 $\alpha$ 比较：
  - $\mathrm{IoU}\ge\alpha$ → **TP**（真阳性）
  - $\mathrm{IoU}<\alpha$ → **FP**（把背景/错位框当成了目标）
- 同一个预测，$\mathrm{IoU}=0.96$ 时：阈值 0.5 → TP；阈值 0.97 → FP。
- 极端地，把阈值降到 0，几乎任何框都能算 TP——所以**阈值必须和指标一起报告**（如 mAP@0.5、mAP@0.5:0.95）。

> 实际训练/推理里还有另一个地方用到 IoU：**NMS 非极大值抑制**——把与高分框 IoU 超过阈值的重复框删掉（见 [[2026-10-23]] 的 non-maximum suppression）。

### 3. 分割里：IoU 是「主指标」

分割输出的是**掩码（mask）**，形状可以任意规则/不规则，没有「框」：

- 逐**像素**比较预测掩码与真值掩码，算面积比；
- 没有「阈值 $\alpha$」这一步：每个像素直接落入 TP / FP / FN；
- 因此分割的 IoU 也叫 **Jaccard index**（与 [[2026-10-23]] 词汇里的 Jaccard index 是同一个东西）。

### 4. 怎么算：一个公式搞定

两个框 $A=(ax_1,ay_1,ax_2,ay_2)$、$B=(bx_1,by_1,bx_2,by_2)$，坐标约定为左上 / 右下：

$$
\begin{aligned}
x_1&=\max(ax_1,bx_1), & x_2&=\min(ax_2,bx_2)\\
y_1&=\max(ay_1,by_1), & y_2&=\min(ay_2,by_2)
\end{aligned}
$$

$$
\text{交集}=(x_2-x_1)_+\cdot(y_2-y_1)_+,\qquad
\text{并集}=\text{area}(A)+\text{area}(B)-\text{交集}
$$

其中 $(\cdot)_+=\max(\cdot,0)$：**不重叠时宽或高为负，clamp 到 0 → 交集为 0**。这是实现里最容易漏的一步（忘了 max 0 会算出「负面积」的怪值）。

代码层面，PyTorch 有现成实现：

```python
from torchvision.ops import box_iou
iou = box_iou(boxes_pred, boxes_gt)   # [N, M]，每对框的 IoU
```

### 5. 一页总结

| 场景 | IoU 的角色 | 是否需要阈值 |
| ---- | ---- | ---- |
| 目标检测 | 判定 TP/FP 的尺子（辅助指标，最终看 mAP） | 需要（$\alpha$，常 0.5） |
| 实例/语义分割 | 直接的主指标（逐像素） | 不需要 |
| NMS | 去重的相似度度量 | 需要（NMS 阈值） |

> **注意：** IoU 对**小目标**很苛刻——几个像素的偏移就能让 IoU 从 0.8 掉到 0.3。所以评测小目标时常用 mAP@0.5:0.95 的分档，或配合 GIoU/DIoU/CIoU 这类改进（在无重叠时也能给出梯度）。

## 相关

- [[L1 深度学习基础]] — 准确率 / 损失这些「分类指标」；检测指标是它们的推广
- [[DeepLearningRM/主页|DeepLearningRM]] — ZLLC 检测 / groundzero pose 的 mAP 与 NMS 实践
- [[2026-10-23]] — 单词条 non-maximum suppression / Jaccard index（与 IoU 同源的两个概念：NMS 用 IoU 去重，分割 IoU 就是 Jaccard index）
