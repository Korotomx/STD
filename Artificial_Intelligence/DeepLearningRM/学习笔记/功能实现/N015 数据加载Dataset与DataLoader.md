数据从磁盘到网络要过三层：Dataset 取单个样本、DataLoader 打包 batch、训练循环五步更新权重。这篇把 MNIST 的数据加载、最小训练循环和常用语法串成一条可运行链路。

## 数据加载：三层流水线

```
磁盘(图片文件) → Dataset(取单个样本) → DataLoader(打包 batch) → 网络
```

- **Dataset** 回答「第 i 个样本长啥样、一共多少个」（`__len__` / `__getitem__`）
- **DataLoader** 回答「怎么一批批地喂」（batch / 打乱 / 多进程）

### transforms：图片 → 张量 + 归一化

```python
transform = transforms.Compose([
    transforms.ToTensor(),                        # PIL 图 -> 张量：[0,255]→[0,1]，HWC→CHW
    transforms.Normalize((0.1307,), (0.3081,)),   # (x-mean)/std，MNIST 全局均值/标准差
])
```

`Normalize` 让输入近似 N(0,1)，训练更稳、收敛更快。灰度图只有 1 通道，mean/std 要写**一元组** `(0.1307,)`，不是 `(0.1307)`。

### Dataset 与切分验证集

```python
train_full = torchvision.datasets.MNIST(root=DATA_DIR, train=True, download=True, transform=transform)
train_set, val_set = random_split(train_full, [50000, 10000])
```

torchvision 已把 MNIST 做成现成 Dataset，`download=True` 首次自动下载，`train_full[0]` 返回 `(图像张量, 标签)`。60000 张切成 50000 训练 + 10000 验证：训练集「学」，验证集「看有没有过拟合」。

### DataLoader 与 batch 形状

```python
train_loader = DataLoader(train_set, batch_size=64, shuffle=True, num_workers=2)
```

- `batch_size=64`：一批 64 张
- `shuffle=True`：每 epoch 打乱顺序，防止网络记住顺序
- `num_workers=2`：2 个子进程并行读数据（WSL2 内存小，别用默认 8）

实测输出：

```
训练集样本数： 60000
训练集： 50000 张 | 验证集： 10000 张
train_loader 共 782 个 batch              # 50000 / 64
images.shape = torch.Size([64, 1, 28, 28])  # [batch, 通道, 高, 宽]
labels.shape = torch.Size([64])
```

`[N, C, H, W]` 就是网络 `forward` 的输入形状。

### 可视化

前 16 张画成 4×4 网格，标题是标签（反归一化后画回原亮度）：

![[mnist_sample.png]]

## 训练循环：五步闭环

```python
for images, labels in loader:
    images, labels = images.to(DEVICE), labels.to(DEVICE)
    optimizer.zero_grad()               # ① 清空上一步残留梯度
    outputs = model(images)             # ② 前向：算出预测
    loss = criterion(outputs, labels)   # ③ 算损失：错得有多离谱
    loss.backward()                     # ④ 反向：自动求每个权重的梯度
    optimizer.step()                    # ⑤ 更新：按梯度挪一步
```

顺序不能乱：不清零梯度会累加；先 forward 才有 loss 可 backward；backward 算出梯度后 step 才更新。

### 损失函数 CrossEntropyLoss

- 输入是网络的**原始分数**（logits），所以网络最后一层**不加 softmax**
- 内部自动做 softmax + 交叉熵，返回一个标量
- `loss.item()` 把标量张量摘成 Python float 用于打印统计

### 优化器 Adam

`optimizer.step()` 执行 `权重 = 权重 - 学习率 × 梯度`：

- `lr=0.001` 是超参数，太大发散、太小学得慢
- Adam 给每个参数自适应步长 + 动量，新手默认用它几乎不踩坑
- `optimizer.zero_grad()` 每轮必须调，否则 `.grad` 累加发散

### epoch 与 batch

| 概念 | 含义 | 本实验 |
| ---- | ---- | ---- |
| batch | 一次喂进网络的图数 | 64 |
| 一个 epoch | 把 50000 张训练图完整看一遍 | 50000/64 ≈ 782 个 batch |
| 10 epoch | 完整看 10 遍 | 7820 次更新 |

网络要反复看同一批数据，参数才能慢慢调到位。

### 训练 vs 验证

- `model.train()` / `model.eval()`：切模式（影响 Dropout/BatchNorm；LeNet 无感、ResNet 有感）
- `@torch.no_grad()`：验证只前向不算梯度，省显存更快
- 验证集不参与更新，只看「没见过的数据上表现如何」

### 记曲线 + 存最佳权重

- 每个 epoch 记录 `train_loss / train_acc / val_loss / val_acc`，最后画两条曲线
- 存「验证集最高」那版权重 `best_wts = copy.deepcopy(model.state_dict())`，防训练后期过拟合导致 val 变差
- `set_seed(42)` 固定随机种子，保证可复现

## 例子：MNIST 上的结果

LeNet 教学版（`task0_basic/model_train.py`）98.40%，ResNet 任务一正式版（`task1_resnet_mnist/train_resnet.py`）99.14%。两者训练循环完全相同，只是模型换成 [[N017 ResNet-18架构与残差连接]]。

## 语法速查

### Python 通用

| 语法 | 作用 | 结果 / 变体 |
| ---- | ---- | ---- |
| `import torch.nn as nn` | 导入并起短别名 | `from X import Y` 只取某个名字 |
| `f"{epoch+1:2d} {acc*100:5.2f}"` | f-string 嵌入表达式 | 旧式 `"{}".format(x)` |
| `"cuda" if cond else "cpu"` | 三元表达式 | 多行 if/else |
| `def set_seed(seed=42)` | 参数默认值 | 按关键字传 `set_seed(seed=7)` |
| `return a, b` / `x, y = f()` | 返回/解包元组 | 任意多个 |
| `_, preds = torch.max(...)` | `_` 丢弃不关心的值 | `torch.max(...)[1]` |
| `if __name__ == "__main__":` | 被 import 时不跑主逻辑 | 固定写法 |
| `@torch.no_grad()` | 整个函数关梯度 | `with torch.no_grad():` |
| `(preds == labels).sum().item()` | 数预测正确的个数 | 得到 Python int |
| `list.append(x)` | 末尾加元素 | `.extend([..])` 一次加多个 |

### 张量与设备

| 语法 | 作用 | 结果 / 变体 |
| ---- | ---- | ---- |
| `torch.device("cuda")` | 造设备对象 | `"cpu"` / `"cuda:0"` |
| `.to(DEVICE)` | 张量/模型搬到设备 | `.cpu()` / `.cuda()` |
| `torch.max(outputs, 1)` | 沿 dim=1 取最大 | 返回 `(values, indices)`；`x.max(1)` |
| `x.size(0)` | 第 0 维大小（batch 数） | `x.shape` 取整个形状 |
| `x.item()` | 0 维张量 → Python 数 | 只能用于标量 |
| `(preds==labels).sum()` | 布尔张量求和 | 接 `.item()` |

### 数据

| 语法 | 作用 | 注意 |
| ---- | ---- | ---- |
| `transforms.Compose([...])` | 串成流水线，按序执行 | 单个 transform 可直接赋值 |
| `transforms.ToTensor()` | PIL/numpy → 张量，HWC→CHW | `ToPILImage()` 反向 |
| `transforms.Normalize((m,),(s,))` | `(x-mean)/std` | 彩色图每通道一个值 |
| `datasets.MNIST(root=, train=, download=, transform=)` | 加载数据集 | `ImageFolder(root=)` 读自己的图 |
| `random_split(ds, [50000,10000])` | 随机切分 | 按比例先算长度 |
| `DataLoader(ds, batch_size=, shuffle=, num_workers=)` | 打包 batch | 验证集 `shuffle=False` |

### 模型与训练

| 语法 | 作用 | 注意 |
| ---- | ---- | ---- |
| `model.train()` / `model.eval()` | 切训练/评估模式 | 影响 Dropout/BatchNorm |
| `model(images)` | 调 `forward` | 别写 `model.forward()`（绕过钩子） |
| `model.parameters()` | 所有可训练参数 | 交给优化器 |
| `model.state_dict()` | 参数字典 | `load_state_dict(torch.load(p))` |
| `nn.CrossEntropyLoss()` | softmax + 交叉熵 | 输入是原始分数 |
| `torch.optim.Adam(params, lr=)` | 优化器 | `SGD(params, lr=, momentum=)` |
| `optimizer.zero_grad()` | 清梯度 | `set_to_none=True` 更省内存 |
| `optimizer.step()` | 更新权重 | — |
| `loss.backward()` | 反向求梯度 | `retain_graph=True` 可反两次 |
| `loss.item()` | 损失 → float | 只用于打印/记录 |

### 随机种子与保存

| 语法 | 作用 | 注意 |
| ---- | ---- | ---- |
| `torch.manual_seed(seed)` | 固定 CPU 种子 | `torch.cuda.manual_seed_all(seed)` 固定 GPU |
| `copy.deepcopy(x)` | 深拷贝，完全独立 | 存最佳权重必须 deepcopy |
| `torch.save(best_wts, p)` | 保存参数字典 | `torch.load(p)` 读回 |

### matplotlib

| 语法 | 作用 | 注意 |
| ---- | ---- | ---- |
| `matplotlib.use("Agg")` | 无窗口后端，只存图 | 本机 xrdp 连不上必须用 |
| `plt.rcParams["font.family"]=[...]` | 字体及回退顺序 | 列表写法才按字形 fallback |
| `plt.subplots(1,2,figsize=(12,4))` | 1 行 2 列图 | 返回 `(fig, (ax1, ax2))` |
| `ax.plot(x, y, "b-", label=)` | 画折线 | `"r-"` 红实线、`"b--"` 蓝虚线 |
| `plt.tight_layout()` / `plt.savefig(p, dpi=)` | 防重叠 / 存图 | — |

## 坑与边界

- **`loss.item()` vs `loss`**：统计用 `.item()` 摘成纯数字；`backward()` 必须用张量 `loss`。
- **`torch.max(x, 1)` 返回两个值**，`_, preds` 接：第一个是分数，第二个才是预测类别。
- **`state_dict()` 是「参数→张量」的字典，不是模型对象**：保存用 `torch.save(best_wts, ...)`，不要 `torch.save(model, ...)`（重且不推荐）。
- **验证集一定 `shuffle=False`**，否则指标不可复现。
- **`num_workers` 在 WSL2 上默认 8 会 OOM**，先降到 2；排查问题可临时 `workers=0`。

> PS：工程上常见的几件事——`device` 用 `torch.device("cuda" if torch.cuda.is_available() else "cpu")` 只算一次并全局复用；seed 同时设 `random` / `numpy` / `torch` / `torch.cuda`；最佳权重存 `state_dict` 而不是整个模型；训练脚本用 `argparse` 把 lr/batch/epochs 抽成参数；每 epoch 存 `last.pt` 便于断点续训。

## 总结

数据加载是「磁盘 → Dataset（单个样本）→ DataLoader（batch/shuffle/worker）」三层；一个 batch 是 `[N,C,H,W]`。训练循环反复执行「清梯度 → 前向 → 算 loss → 反向 → 更新」；CrossEntropyLoss 吃 logits 内部做 softmax，Adam 按 `权重-lr×梯度` 更新；epoch = 完整看一遍训练集，训练用 `train()+backward`、验证用 `eval()+no_grad`；记曲线、存最佳权重、固定种子对应任务一的评分点。