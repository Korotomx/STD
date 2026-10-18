---
tags:
  - 功能实现
  - 自动求导autograd
  - requires_grad
  - 计算图
  - 反向传播Backprop
  - 梯度Gradient
---

# 自动求导 autograd：requires_grad / 计算图 / backward · 功能实现 · N002

**时间:** 2026-10-17
**标签:** #功能实现 #自动求导autograd #requires_grad #计算图 #反向传播Backprop #梯度Gradient
**关联:** [[N001 张量基础dtype-shape-device与GPU]]（前置：张量）

## 实际情况

代码 `task1_resnet_mnist/02_autograd.py`，实测跑通（RTX 5060 / dl_env）。

### 1. 为什么要自动求导

训练的本质是**反复调权重让 loss 变小**。要往哪个方向调，就得知道 loss 对每个权重的**导数（梯度）**。一个二次函数手推还行，几十层网络手动求导不现实。

`autograd` 干的事：**你只写「前向」计算那一步，PyTorch 自动用链式法则算出所有梯度**。这是整个「训练 = 算 loss → 反向 → 更新权重」闭环的引擎。

### 2. requires_grad：标记「要算梯度」

```python
w = torch.tensor(2.0, requires_grad=True)   # 当成「权重」
```

- 默认 `requires_grad=False`（输入数据、常量一般不开）
- 只有**要更新的参数**才打开这个开关

### 3. 前向：autograd 偷偷记下计算图

```python
y = w * w        # y = w^2
z = 3 * y + 1    # z = 3w^2 + 1
```

这几行会记下一张**计算图**：`w → y → z`。每个节点都有 `grad_fn`（谁把它算出来的），如 `MulBackward0`、`AddBackward0`。反向传播就是**从输出倒着走这张图**。

### 4. backward()：梯度自动写进 .grad

```python
z.backward()          # z 必须是标量
print(w.grad)         # tensor(12.)
```

手算核对：`z = 3w² + 1` → `dz/dw = 6w`，`w = 2` → `12` ✓。梯度自动落到叶子张量的 `.grad` 属性。

### 5. 两个坑：梯度累加 + 图只能反一次

**坑 A — 梯度是「累加」不是「覆盖」：**

```python
z = 3 * w * w + 1    # 重建图（= 模拟下一轮训练）
z.backward()
print(w.grad)        # tensor(24.)   ← 12 + 12，不是 12！
```

所以**每轮训练前必须清零**，训练循环里由 `optimizer.zero_grad()` 代劳（手动是 `w.grad.zero_()`）。不清零 → 梯度越积越大 → 训练发散。

**坑 B — 同一个图不能连续 backward 两次：**

计算图反完一次就释放了，再对**同一个** `z` 调 `backward()` 会报 `RuntimeError: Trying to backward through the graph a second time`。真要反两次需 `z.backward(retain_graph=True)`。

### 6. 推理用 no_grad()：关掉梯度

```python
with torch.no_grad():
    out = w * w          # out.requires_grad = False
```

评估/预测只算前向、不反向，关掉记录图能**省显存、算得更快**。更新权重那步也要放 `no_grad()` 里（`w -= lr * w.grad`，否则对带梯度的叶子张量原地改会报错）。

### 7. 完整闭环：极简梯度下降

```python
w = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)
lr = 0.01
for step in range(5):
    y_pred = w * x + b                    # 前向
    loss = (y_pred - y_true) ** 2         # 算损失（MSE）
    loss.backward()                       # 反向：求梯度
    with torch.no_grad():                 # 更新：w -= lr * grad
        w -= lr * w.grad
        b -= lr * b.grad
    w.grad.zero_(); b.grad.zero_()        # 清零
```

实测 loss 从 4.0 一路下降收敛。**这 6 行就是后面所有训练循环的骨架**：前向 → 算 loss → backward → 更新 → 清零。

## 思考

（留白 —— 为什么 `backward()` 要求 `z` 是**标量**？如果 loss 是一个向量/矩阵，反传时该传什么给 `backward`？）

这种内容也是可以求导的吗?
## 总结

**本质：** autograd 记录前向的「计算图」，`backward()` 沿图反向用链式法则自动求导，梯度写进 `.grad`。`requires_grad=True` 标记要更新的参数；`.grad` 是累加的，每轮必须 `zero_grad()`（训练里 `optimizer.zero_grad()`）；同一张图只能 backward 一次（除非 `retain_graph=True`）；推理/更新用 `torch.no_grad()` 关梯度。训练闭环 = 前向 → loss → backward → 更新 → 清零。
**标签:** #功能实现 #自动求导autograd #requires_grad #计算图 #反向传播Backprop #梯度Gradient
