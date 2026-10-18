---
tags:
  - 概念原理
  - ResNet
  - 残差连接ResidualConnection
  - 恒等映射IdentityMapping
  - 梯度消失VanishingGradient
  - BasicBlock
  - 批归一化BatchNorm
---

# ResNet-18 架构与残差连接 · 概念原理 · N017

**时间:** 2026-10-18
**标签:** #概念原理 #ResNet #残差连接ResidualConnection #恒等映射IdentityMapping #梯度消失VanishingGradient #BasicBlock #批归一化BatchNorm
**关联:** [[N009 LeNet-5架构与各层参数]]（上一个架构，6 万参数）· [[N006 反向传播与梯度下降]]（梯度消失）· [[N007 卷积层运算步幅填充多卷积核]]（卷积层参数）· [[N012 过拟合与Dropout]]（训练时 val 走平）

## 实际情况

对应代码 `task1_resnet_mnist/resnet.py`，从零搭 ResNet-18（11,172,810 参数），MNIST 最佳验证准确率 99.14%。

### 1. 要解决的问题：退化 + 梯度消失

直觉以为「网络越深越好」，实验发现：单纯堆层，深了反而**在训练集上都变差**（不是过拟合，叫「退化」）。根源是**梯度消失**——反向传播时梯度从最后一层一层层传回，越传越弱，前面的层几乎学不动（连接 [[N006 反向传播与梯度下降]]）。

### 2. 解法：残差连接（skip connection）

让每块不去学完整映射 H(x)，而是学**残差** F(x)：

```
H(x) = F(x) + x        # x 是输入，原样抄过来加在结果上
```

两个妙处：
1. **深了不会变差**：若这几层没用，网络让 F(x)→0 即可，块退化成恒等 x，最坏「白加一层」
2. **梯度有高速公路**：反向时梯度沿 +x 这条短路直接传回、不衰减，缓解梯度消失

### 3. BasicBlock：残差的最小积木

```python
def forward(self, x):
    identity = x                       # 先抄一份
    out = self.relu(self.bn1(self.conv1(x)))
    out = self.bn2(self.conv2(out))
    out += self.shortcut(identity)     # F(x) + x
    out = self.relu(out)
    return out
```

- 两条 3×3 卷积 + BN + ReLU，`F(x) = conv2(bn(relu(conv1(x))))`
- 加完残差**再**过最后一个 ReLU
- `bias=False`：卷积后面紧跟 BatchNorm，偏置被 BN 吸收、可省

### 4. shortcut 的维度匹配（最易绕晕）

`F(x) + x` 要求两边形状一致，但 4 个 stage 里通道翻倍、尺寸减半，x 常常对不上：

| 情况 | shortcut 做什么 |
| ---- | ---- |
| stride=1 且通道不变 | 恒等（啥也不做，x 原样） |
| stride≠1 或通道变 | 1×1 卷积（改通道 + 改尺寸） |

例（layer2 第一个块）：输入 `[64,64,28,28]` → F(x) 路径 stride=2 变成 `[64,128,14,14]`，identity 还是 `[64,64,28,28]` → shortcut 用 1×1 卷积 stride=2 对齐成 `[64,128,14,14]` 再相加。

### 5. 四个 stage：通道翻倍、尺寸减半

| stage | 通道 | stride | 尺寸 | block 数 |
| ---- | ---- | ---- | ---- | ---- |
| stem(conv1) | 1→64 | 1 | 28×28 | — |
| layer1 | 64→64 | 1 | 28×28 | 2 |
| layer2 | 64→128 | 2 | 14×14 | 2 |
| layer3 | 128→256 | 2 | 7×7 | 2 |
| layer4 | 256→512 | 2 | 4×4 | 2 |

- 「18」= 1(stem) + 8 块×2 层卷积(16) + 1(fc) = 18 层
- **ResNet-34 = 每层 block 数 [2,2,2,2] 换成 [3,4,6,3]**，其它不动

### 6. MNIST 适配（与标准 ResNet 的区别）

标准 ResNet 给 ImageNet（3 通道 224×224）设计：stem 用 7×7 stride=2 + maxpool。MNIST 只有 1 通道 28×28，照原样会一下压没。改三点：
1. 输入通道 3 → **1**
2. stem 7×7 stride=2 → **3×3 stride=1**
3. 去掉 **maxpool**

### 7. 实测：轻微过拟合

train_acc 一路到 99.46%，val_acc 在 98.4~99.1 之间走平——1117 万参数去记 5 万张手写数字，容量严重过剩，轻微过拟合（连接 [[N012 过拟合与Dropout]]）。最佳验证准确率取的是「验证集最高」那轮（99.14%，第 9 轮），不是最后那轮。

## 思考

（留白 —— 残差连接解决了「深了退化」，那为什么 ResNet 还会轻微过拟合 MNIST？「退化」和「过拟合」是两码事，区别在哪？）

## 总结

**本质：** ResNet 用残差连接 `F(x)+x` 解决深层网络的退化与梯度消失——网络学残差、深了不退化、梯度有短路；BasicBlock = 两条 3×3 卷积 + shortcut（形状对不上时用 1×1 卷积对齐）；四个 stage 通道翻倍、尺寸减半；ResNet-18 = [2,2,2,2] 块，换成 [3,4,6,3] 即 ResNet-34。
**标签:** #概念原理 #ResNet #残差连接ResidualConnection #恒等映射IdentityMapping #梯度消失VanishingGradient #BasicBlock #批归一化BatchNorm
