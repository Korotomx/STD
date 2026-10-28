PyTorch 训练前的三件基础设施：隔离的 Python 环境（venv）、装数字的张量（dtype/shape/device）、自动求导（autograd）。三者依次是「在哪跑 → 拿什么算 → 怎么求梯度」，串起来就是训练循环的底座。

## 环境：venv 隔离的 Python

虚拟环境 = 自己的解释器 + 自己的第三方库目录，和系统 Python 完全隔离。C/C++ 类比：每个项目一套独立的「编译器 + include/lib」，而不是全系统共用 `/usr/lib` 和一个 gcc 版本。

本机两个环境：

| 环境 | 位置 | 解释器 | 有 torch? |
| ---- | ---- | ---- | ---- |
| 系统 Python | `/usr/bin/python3` | 3.14 | ❌（太新，torch 没有对应 wheel） |
| dl_env（venv） | `/home/akiha/dl_env/` | 3.11.15 | ✅ 2.11.0+cu128 |

```bash
python3.11 -m venv /home/akiha/dl_env        # 创建（已建好）
source /home/akiha/dl_env/bin/activate       # 激活，提示符前出现 (dl_env)
python 02_autograd.py
deactivate
```

不激活也可用全路径 `/home/akiha/dl_env/bin/python xx.py`。VS Code 用 `Python: Select Interpreter` 选 dl_env，或在 `.vscode/settings.json` 写 `python.defaultInterpreterPath` 固定。

Anaconda/conda 与 venv 是同一概念的不同工具：conda 还能管非 Python 依赖（某些 C 库），纯 PyTorch 项目 venv 够用、更轻。

## 张量：多维数组

张量和 NumPy 的 `ndarray` 是同一套心智：连续内存 + 元素同类型 + 下标访问。

| 维度 | 名字 | 例子 |
| ---- | ---- | ---- |
| 0 维 | 标量 scalar | `5` |
| 1 维 | 向量 vector | `[1,2,3]` |
| 2 维 | 矩阵 matrix | `[[1,2],[3,4]]` |
| 3 维+ | 张量 tensor | 图像批量 |

深度学习最常见 4 维 `[N, C, H, W]`（批量、通道、高、宽）；`shape=[2,3]` 读作「2 行 3 列」，从外到内数。

三个核心属性：

- `dtype` 元素类型 —— 深度学习几乎只用 **float32**
- `shape` 形状
- `device` 在哪算 —— `cpu` 或 `cuda:0`

**torch 浮点字面量默认 float32，NumPy 默认 float64**（torch 专为深度学习造）。所以显式写 `dtype=torch.float32` 是标配；整数 torch 默认 int64，和 NumPy 一致。

```python
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
torch.zeros(2, 3)   # 全 0
torch.ones(2, 3)    # 全 1
torch.arange(6)     # [0,1,2,3,4,5]
torch.randn(2, 3)   # 标准正态 N(0,1)，初始化权重常用
```

### 搬上 GPU

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.randn(3, 4)      # 默认 CPU
x_gpu = x.to(device)       # 复制到 GPU（别名 .cuda()）
```

**最大的坑：CPU 张量和 GPU 张量不能直接运算**，必须同处一个设备。模型和数据都要 `.to(device)`。

### 广播 broadcast

形状不同的张量逐元素运算时，小的一方自动复制补齐。规则：**从右往左对齐维度，每一维要么相等、要么其中一个是 1（或缺失）**。

```python
m = torch.tensor([[1., 2., 3.], [4., 5., 6.]])  # 2x3
v = torch.tensor([10., 20., 30.])               # 长度 3
m + v   # v 被广播成 [[10,20,30],[10,20,30]]
```

这是「向量化」的核心机制，NumPy/PyTorch 大量靠它免写循环。

## 自动求导 autograd

训练 = 反复调权重让 loss 变小；往哪调要知道 loss 对每个权重的导数。几十层网络手推不现实，autograd 让你只写前向，梯度和链式法则全自动。

### requires_grad 与计算图

```python
w = torch.tensor(2.0, requires_grad=True)   # 当成「权重」，默认 False
y = w * w          # y = w^2
z = 3 * y + 1      # z = 3w^2 + 1
```

这几行会记下一张**计算图** `w → y → z`，每个节点有 `grad_fn`（`MulBackward0`、`AddBackward0`）。只有要更新的参数才打开 `requires_grad`；输入数据、常量一般不开。

### backward 与梯度累加

```python
z.backward()       # z 必须是标量
print(w.grad)      # tensor(12.)   手算 dz/dw = 6w = 12 ✓
```

**坑 A：梯度是累加不是覆盖**。再跑一次 `z.backward()`，`.grad` 变 24（12+12）。所以每轮训练必须清零：训练循环里由 `optimizer.zero_grad()` 代劳（手动 `w.grad.zero_()`）。不清零 → 梯度越积越大 → 发散。

**坑 B：同一个图不能连续 backward 两次**。图反完一次就释放，再调用报 `Trying to backward through the graph a second time`；真要反两次用 `retain_graph=True`。

### no_grad

```python
with torch.no_grad():
    out = w * w          # out.requires_grad = False
```

评估/预测只算前向，关掉记录图省显存、更快。更新权重那步也要放 `no_grad()` 里（`w -= lr * w.grad`），否则对带梯度的叶子张量原地改会报错。

### 极简梯度下降闭环

```python
w = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)
lr = 0.01
for step in range(5):
    y_pred = w * x + b                    # 前向
    loss = (y_pred - y_true) ** 2         # 算损失（MSE）
    loss.backward()                       # 反向：求梯度
    with torch.no_grad():                 # 更新
        w -= lr * w.grad
        b -= lr * b.grad
    w.grad.zero_(); b.grad.zero_()        # 清零
```

实测 loss 从 4.0 一路下降收敛。这 6 行是后面所有训练循环的骨架：前向 → loss → backward → 更新 → 清零（完整工程版见 [[N015 数据加载Dataset与DataLoader]]）。

## 坑与边界

- `dtype` 不显式写，torch 会猜；和 NumPy 混用时 float64 会悄悄进来。
- `.to(device)` 是**复制**，不是原地搬；原张量还在 CPU。
- 广播只在「兼容」时成立，形状对不上会直接报错，不会自动 reshape。
- `backward()` 要求标量；loss 是向量/矩阵时要给 `gradient=` 参数。
- `w.grad` 在第一次 backward 前是 `None`。

## 总结

venv 提供隔离的 Python（本机 dl_env：3.11 + torch 2.11 cu128）；张量三属性 dtype/shape/device，DL 统一 float32、显式声明，CPU/GPU 张量不能混算，广播让小张量自动补齐；autograd 记录前向计算图，`backward()` 沿图求梯度写入 `.grad`，梯度累加必须 `zero_grad()`，推理用 `no_grad()`；训练闭环 = 前向 → loss → backward → 更新 → 清零。