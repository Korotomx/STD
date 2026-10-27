IoU = **交集面积 / 并集面积**，取值 $[0,1]$：0 完全不重叠，1 完全重合。检测里它是判断框质量的尺子，配合阈值 $\alpha$ 把预测分成 TP / FP；分割里它直接是逐像素主指标。核心计算只有一个技巧：**交集宽高分别取 max/min，再 clamp 到 0**。

> 原文：[[Intersection Over Union (IoU) in Object Detection &  Segmentation]]

## 定义

$$
\mathrm{IoU}=\frac{|A\cap B|}{|A\cup B|}
=\frac{\text{交集面积}}{\text{真值面积}+\text{预测面积}-\text{交集面积}}
$$

以鸟为例：模型 A 重叠多；模型 C 把树枝也框进去，交集可能更大，但并集也更大，IoU 反而可能低于 A。**IoU 奖励贴合，惩罚框大**。

## 检测：判定 TP/FP 的尺子

IoU 本身不是最终指标（最终看 mAP / Recall / Loss），它负责判定：

- $\mathrm{IoU}\ge\alpha$ → **TP**；
- $\mathrm{IoU}<\alpha$ → **FP**（背景或错位框被当成目标）。

同一个预测 IoU=0.96 时，阈值 0.5 判 TP，阈值 0.97 判 FP。把阈值降到 0，几乎任何框都能算 TP，所以阈值必须和指标一起报告，如 mAP@0.5、mAP@0.5:0.95。

NMS 也用它：把与高分框 IoU 超过阈值的重复框删掉。

## 分割：逐像素主指标

分割输出掩码，形状可以任意，没有“框”。逐像素比较预测与真值，算面积比；没有阈值 $\alpha$ 这一步，每个像素直接落入 TP / FP / FN。分割的 IoU 也叫 **Jaccard index**。

## 计算

两个框 $A=(ax_1,ay_1,ax_2,ay_2)$、$B=(bx_1,by_1,bx_2,by_2)$，坐标为左上 / 右下：

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

其中 $(\cdot)_+=\max(\cdot,0)$：不重叠时宽或高为负，clamp 到 0 后交集才为 0。忘了 max 0 会算出负面积。

```python
from torchvision.ops import box_iou

iou = box_iou(boxes_pred, boxes_gt)   # [N, M]，每对框的 IoU
```

## 一页总结

| 场景 | IoU 的角色 | 是否需要阈值 |
| --- | --- | --- |
| 目标检测 | 判定 TP/FP 的尺子（辅助指标，最终看 mAP） | 需要（$\alpha$，常 0.5） |
| 实例/语义分割 | 逐像素的主指标 | 不需要 |
| NMS | 去重的相似度度量 | 需要（NMS 阈值） |

## 坑与边界

- IoU 对**小目标**很苛刻：几个像素偏移就能让 IoU 从 0.8 掉到 0.3。评测小目标常用 mAP@0.5:0.95 分档，或配合 GIoU / DIoU / CIoU。
- 阈值必须与指标一起报告，否则 TP/FP 数量没有可比性；检测框坐标约定也要先统一。

分类指标到检测指标的延伸见 [[L1 深度学习基础]]；同属图像几何处理的插值见 [[双线性插值 从一维线性到二维图像]]。