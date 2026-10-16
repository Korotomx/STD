---
tags:
  - 功能实现
  - 张量Tensor
  - dtype类型
  - shape形状
  - device设备
  - GPU
  - 广播Broadcast
  - NumPy
---

# 张量基础：dtype/shape/device 与 GPU · 功能实现 · N001

**时间:** 2026-10-16 12:20
**标签:** #功能实现 #张量Tensor #dtype类型 #shape形状 #device设备 #GPU #广播Broadcast #NumPy
**关联:** （首篇，待续）

## 实际情况

代码 `task1_resnet_mnist/01_tensor.py`，实测跑通。

### 1. 张量 = 多维数组

张量（tensor）本质就是「多维数组」，和 C 的数组同构：连续内存 + 元素同类型 + 下标访问。区别只在维度：

| 维度 | 名字 | 例子 |
| ---- | ---- | ---- |
| 0 维 | 标量 scalar | 一个数 `5` |
| 1 维 | 向量 vector | `[1,2,3]` |
| 2 维 | 矩阵 matrix | `[[1,2],[3,4]]` |
| 3 维+ | 张量 tensor | 图像批量 |

深度学习最常见是 4 维：`[批量N, 通道C, 高H, 宽W]`（卷积时展开）。`shape=[2,3]` 读作「2 行 3 列」，从外到内数。

torch 的 `tensor` 和 NumPy 的 `ndarray` 是**同一套心智**，写法几乎一样：

```python
t = torch.tensor([[1, 2, 3], [4, 5, 6]])   # torch 张量
a = np.array([[1, 2, 3], [4, 5, 6]])       # NumPy 数组
```

### 2. 三个关键属性：dtype / shape / device

每个张量都有三个核心属性：

- `dtype` 元素类型 —— 深度学习**几乎只用 float32**（省显存、GPU 算得快）
- `shape` 形状
- `device` 在哪算 —— `cpu` 还是 `cuda:0`

**关键差异：torch 浮点字面量默认 float32，NumPy 默认 float64**。torch 专为深度学习造，默认就偏 float32。所以显式写 `dtype=torch.float32` 是标配，别让 torch 猜：

```python
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)   # float32
```

（整数 torch 默认 int64，和 numpy 一样。）

### 3. 常用创建函数

`zeros/ones/arange/randn` 不用手敲元素：

```python
torch.zeros(2, 3)   # 全 0
torch.ones(2, 3)    # 全 1
torch.arange(6)     # [0,1,2,3,4,5] —— C 里 for(i=0;i<6;i++) 的一行版
torch.randn(2, 3)   # 标准正态 N(0,1) 随机数 —— 初始化权重常用
```

### 4. 搬上 GPU

`device` 属性告诉你张量在哪。`.to('cuda')`（别名 `.cuda()`）把张量**复制**到 GPU：

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.randn(3, 4)      # 默认 CPU
x_gpu = x.to(device)       # 复制到 GPU
```

**最大的坑：CPU 张量和 GPU 张量不能直接一起运算**，必须同处一个设备。实测本机 `cpu -> cuda:0`（RTX 5060）。

### 5. 广播 broadcast

形状不同的张量做逐元素运算时，小的一方自动「复制补齐」。规则：**从右往左对齐维度，每一维要么相等、要么其中一个是 1（或缺失）**：

```python
m = torch.tensor([[1., 2., 3.], [4., 5., 6.]])  # 2x3
v = torch.tensor([10., 20., 30.])               # 长度 3
m + v   # v 被广播成 [[10,20,30],[10,20,30]] 再相加
```

广播是「向量化」的核心机制，NumPy/PyTorch 大量靠它免写循环。

## 思考

（留白 —— 一个 4 维张量 `[8, 3, 32, 32]` 四个数字分别代表什么？为什么「批量」要放在最外层？）

## 总结

**本质：** 张量 = 多维数组（NumPy ndarray 同款心智），三属性 dtype/shape/device 是核心；深度学习统一 float32、显式 `dtype=`；`.to('cuda')` 搬上 GPU，CPU/GPU 张量不能混算；广播让小张量自动复制补齐实现逐元素运算。
**标签:** #功能实现 #张量Tensor #dtype类型 #shape形状 #device设备 #GPU #广播Broadcast #NumPy
