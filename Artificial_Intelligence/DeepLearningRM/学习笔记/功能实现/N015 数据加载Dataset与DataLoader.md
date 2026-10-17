---
tags:
  - 功能实现
  - 数据加载Dataset
  - DataLoader
  - transforms
  - 归一化Normalize
  - 批Batch
  - 可视化Visualization
---

# 数据加载 Dataset / DataLoader：把 MNIST 喂给网络 · 功能实现 · N015

**时间:** 2026-10-17 21:10
**标签:** #功能实现 #数据加载Dataset #DataLoader #transforms #归一化Normalize #批Batch #可视化Visualization
**关联:** [[N001 张量基础dtype-shape-device与GPU]]（batch 是第 0 维 N）· [[N009 LeNet-5架构与各层参数]]（batch 数据传输）· [[N012 过拟合与Dropout]]（验证集看泛化）· [[N013 数据增强图像增强与LRN]]（transform 里还能加增强）

## 实际情况

对应代码 `task1_resnet_mnist/03_dataset.py`，本机实测跑通。

### 1. 数据加载的「三层流水线」

```
磁盘(图片文件)  →  Dataset(取单个样本)  →  DataLoader(打包 batch)  →  网络
```

- **Dataset** 回答「第 i 个样本长啥样、一共多少个」
- **DataLoader** 回答「怎么一批批地喂」（batch / 打乱 / 多进程）

两者分工，正是考核任务一「数据加载规范」的评分点。

### 2. transforms：图片 → 张量 + 归一化

```python
transform = transforms.Compose([
    transforms.ToTensor(),                        # PIL 图 -> 张量：像素 [0,255]→[0,1]，HWC→CHW
    transforms.Normalize((0.1307,), (0.3081,)),   # (x-mean)/std，MNIST 全局均值/标准差
])
```

- `ToTensor` 做两件事：把 0~255 像素缩到 0~1，且把 `[H,W,C]` 转成 PyTorch 要的 `[C,H,W]`
- `Normalize` 让输入近似 N(0,1)，训练更稳、收敛更快
- **坑**：灰度图只有 1 通道，mean/std 要写**一元组** `(0.1307,)`，不是 `(0.1307)`

### 3. Dataset：数据的仓库

```python
train_full = torchvision.datasets.MNIST(root=DATA_DIR, train=True, download=True, transform=transform)
```

- 任何 Dataset 都有 `__len__`（总样本数）和 `__getitem__(i)`（取第 i 个）
- torchvision 已把 MNIST 做成现成 Dataset，`download=True` 首次自动下载
- `train_full[0]` 返回 `(图像张量, 标签)`

### 4. 切出验证集（对应过拟合 N012）

```python
train_set, val_set = random_split(train_full, [50000, 10000])
```

60000 张训练图切成 50000 训练 + 10000 验证：训练集「学」，验证集「看有没有过拟合」。

### 5. DataLoader：打包 batch + 打乱

```python
train_loader = DataLoader(train_set, batch_size=64, shuffle=True, num_workers=2)
```

- `batch_size=64`：一批 64 张，对应 N009 的 batch 维度
- `shuffle=True`：每 epoch 打乱顺序，防止网络「记住顺序」
- `num_workers=2`：2 个子进程并行读数据

### 6. batch 的形状 [N, C, H, W]

实测输出：
```
训练集样本数： 60000
训练集： 50000 张 | 验证集： 10000 张
train_loader 共 782 个 batch              # 50000 / 64
images.shape = torch.Size([64, 1, 28, 28])  # [batch, 通道, 高, 宽]
labels.shape = torch.Size([64])
```

这就是 N001 说的 4 维张量 `[N,C,H,W]`，也正是网络 `forward` 的输入形状。

### 7. 可视化：看一眼数据

前 16 张画成 4×4 网格，标题是标签（反归一化后画回原亮度）：

![[mnist_sample.png]]

## 思考

（留白 —— DataLoader 为什么比「自己 for 循环取样本」好？shuffle 到底在「打乱」哪一层的东西？）

## 总结

**本质：** 数据加载 = 三层流水线「磁盘 → Dataset(取单个) → DataLoader(打包 batch)」；transforms 负责图片→张量(ToTensor) + 归一化(Normalize)；Dataset 有 `__len__`/`__getitem__`；DataLoader 管 batch_size/shuffle/num_workers；一个 batch 的形状是 `[N,C,H,W]`。
**标签:** #功能实现 #数据加载Dataset #DataLoader #transforms #归一化Normalize #批Batch #可视化Visualization
