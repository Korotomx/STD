---
tags:
  - PyTorch
  - 张量Tensor
  - 自动求导autograd
  - 训练循环TrainLoop
  - 优化器Optimizer
  - 激活函数Activation
  - 损失函数Loss
  - nn.Module
  - DataLoader
---

# PyTorch 全景 · 五步训练循环与核心语法

**时间:** 2026-10-20 观看 · 2026-10-20 整理
**来源:** Zachary Huang《Give me 31 minutes, I will make PyTorch click forever》(YouTube `K1ksiPHfgVs`)
**标签:** #PyTorch #张量Tensor #自动求导autograd #训练循环 #优化器 #激活函数 #损失函数
**关联:** [[N001 张量基础dtype-shape-device与GPU]] · [[N002 自动求导autograd]] · [[N015 数据加载Dataset与DataLoader]] · [[N016 训练循环五步闭环]] · [[训练循环语法速查表]]

## 一句话

PyTorch 的一切都浓缩成**五步训练循环**——`预测 → 算损失 → 反向求梯度 → 更新权重 → 清梯度`。张量是装数字的网格,loss 是「错得多离谱」的一个数,autograd 沿着计算图自动求梯度,optimizer 负责按梯度更新权重。整个视频用「NYC 出租车费 = 英里数 × 单价 + 起步价」这条一元线性回归,从手推梯度到五行代码把整个框架串起来。

## 实际情况

### 0. 五步训练循环(全片纲领)

每个训练脚本本质上都是这五行:

```python
pred = model(X)          # 1. 预测
loss = loss_fn(pred, y)  # 2. 衡量损失
loss.backward()          # 3. 反向传播求梯度
optimizer.step()         # 4. 沿梯度更新权重
optimizer.zero_grad()    # 5. 清空梯度(避免累加)
```

三个待回答的核心问题:**backward 到底算了什么?**(每个权重的梯度)**step 改了什么?**(按 `权重 - lr×梯度` 更新)**为什么要清?**(backward 是累加进 `.grad`,不清会越叠越大、步长爆炸)。

### 1. 张量 Tensor:装数字的网格

- 张量 = 多维数字网格,想几维几维;`torch.tensor([[行],[行]])` 给出行列 → `shape` 是 (3, 12)。
- **axis / dim 从 0 数起**:dim 0 是「行方向」,dim 1 是「列方向」;shape 给出每个 dim 的长度。
- **创建**:
  - `torch.zeros(2,3)` / `torch.ones(2,3)` — 全 0 / 全 1;
  - `torch.full((shape,), 7)` — 填指定值(shape 作为**一个元组**传入);
  - `torch.eye(3)` — 对角 1 的方阵;
  - `torch.rand(2,3)` — [0,1) 均匀;`torch.randn(2,3)` — 均值 0 的正态(模型初始化的起点);
  - `torch.arange(12)` — 0..11,和 Python `range` 一样**右开**。

### 2. 张量运算:取数 / 组合 / 变形

- **索引** `fairs[0]` — 取第 0 行,**降掉一个轴**(shape 12);`fairs[:, 6]` — 逗号分隔各轴,`:` 表示「这一轴全取」。
- **切片** `fairs[:, :3]` — 取范围,**保留该轴**(shape 3×3)。
- **布尔掩码** `fairs > 30` → 同 shape 的 True/False 网格;用它索引 `fairs[pricey]` 只抽出 True 的格子;`torch.where(pricey, 30, fairs)` 逐格二选一。
- **聚合(重点:dim 是被「吃掉」的那个轴)**:
  - `fairs.mean(dim=0)` — **dim=0 是「天」轴 → 被平均掉**,得到「每个时段」一个数(12 个);
  - `fairs.mean(dim=1)` — dim=1 被平均掉 → 每天一个数(3 个)。
  - 口诀:**你传的 dim,就是那个会被聚合消失的轴**。`max(dim=1)` 返回两个张量(最大值 + 所在下标);`fairs.max()` 不带 dim = 全局单个最大。`topk(3)` 取最大的 3 个(不聚合、只缩轴)。`sum`/`argmax` 同理。
- **变形**:
  - `t.T` 转置(交换两个轴);`reshape(3,4,3)` 换 shape 不换元素;`flatten()` 摊成一行(用于把矩阵喂给全连接/回归);
  - `@` = 矩阵乘(行×列),`*` = 逐格乘;`view`≈`reshape`、`permute`≈`T` 的重排、`unsqueeze`/`squeeze` 加/去 size-1 的轴、`gather` 按下标逐行取、`clamp` 把数夹进区间。
- **拼接**:`torch.stack([a,b], dim=1)` 沿新轴并排(两行 → 36 个 pair);`torch.cat` 是首尾相接(一行 72)。

### 3. 前向传播 + 损失

- 一元线性回归:**预测 = 权重 W × 英里 + 偏置 b**;W 是斜率(单价),b 是截距(起步价)。**模型要学的数统一叫权重,PyTorch 叫参数 parameter**。
- **广播 broadcasting**:一个 W、一个 b 自动作用到 36 个样本上(标量自动复制补齐)。
- **损失 loss = 一个数**,衡量「错多少」。36 个误差不能直接平均(正负抵消),所以**平方后再平均** → **MSE 均方误差** = mean((pred−y)²)。
- 平方的副作用:一个大错(6²=36)比三个小错(2²×3=12)「罪过」重得多——MSE 对离群值敏感。

### 4. 手推梯度下降(autograd 之前先看懂)

- **梯度** = 损失对每个权重的导数:`∂L/∂W`(只动 W 时损失变多快)、`∂L/∂b`。几个权重,梯度就是几个数。
- **链式法则**(唯一需要的微积分):`pred = W·m + b`,`loss = mean(miss²)`,(x²)' = 2x。于是每个样本对 W 的贡献 = `2·miss·m`,对 b 的贡献 = `2·miss`;再对 36 个样本取平均。
- **沿梯度反方向走一小步**:`W ← W − lr·∂L/∂W`。**lr = 学习率**,不能拿整段梯度直接跳(会越过谷底),要乘个小的 lr(如 0.01)。
- 走 1000 步后 W≈3.76、b≈5.66,和计价表 3.50/英里很接近;b 偏高是因为堵车时计程表按时长加价。
- 手推 W 和 b 时 **b 爬得慢**:因为动 W 一下,每个误差变 m(英里),而动 b 一下只变 1——W 的导数天然大、b 的导数天然小。这个「爬得慢」后面用 optimizer 解决。

### 5. autograd:自动求导

- 建 W、b 时加 `requires_grad=True`,PyTorch 从此**记录**由它们算出的每一步,每个运算变成一个**节点、连成计算图**(乘 → 加 → 减 → 平方 → 平均)。
- `loss.backward()` **从 loss 往回走**计算图,把梯度填进 `w.grad` / `b.grad`——结果和手推一致。往回走时每个节点把自己的局部导数乘进梯度,这就是**链式法则自动执行**。
- ⚠️ **backward 是「累加」不是「覆盖」**:再跑一次 backward,`.grad` 翻倍。所以训练每步结束后必须清零——`zero_grad()`。不清的话旧梯度一直往上叠、步长越走越大。
- **更新要在 `torch.no_grad()` 里做**:更新不属于模型数学,不该被记录;在记录中的张量上原地改值会报错。

### 6. 专业循环:optim / nn.Module / nn.Linear

- **optimizer** = 一个对象,替你持有权重并更新。`opt = torch.optim.SGD(weights, lr=0.01)`,`opt.step()` 更新所有权重,`opt.zero_grad()` 清所有 `.grad`。SGD = stochastic gradient descent,「stochastic」来自后面随机分批。
- **nn.Module** = 模型的基类:子类化它,把每个权重存成 `nn.Parameter`(自带 requires_grad);`model.parameters()` 自动找出全部权重;`forward()` 定义「输入怎么变输出」,`model(x)` 直接调用。Module 还会递归找到嵌套层的参数。
- **nn.Linear(1,1)** = 内置的「权重×输入+偏置」(1 进 1 出)。⚠️ 它把**最后一维**当输入宽度:一行 36 个数会被当成「1 个样本 36 个输入」,要用 `m[:, None]` 把行变列(36 个样本各 1 宽)。
- **保存/加载**:`state_dict()` 按名字持有权重,`torch.save` 写文件,新模型 `load_state_dict` 读回。
- `nn.MSELoss()` 内置了 MSE;`nn.Linear` + `nn.MSELoss` + `optim.SGD` 就是开头那五行。

### 7. DataLoader:分批

- 数据太大不能一次全喂 → `TensorDataset`(把每个样本的输入/标签并排成 pair)+ `DataLoader(batch_size=12, shuffle=True)` 分批**打乱**取出。
- 五步循环改成**每批跑一次**;**一轮把所有批过完 = 1 个 epoch**(36 个样本、batch 12 → 3 批 = 1 epoch)。随机分批正是 SGD 里「stochastic」的来源。

### 8. 三个「菜单」:优化器 / 激活 / 损失

**优化器(治 b 爬得慢):**
- `SGD` 朴素梯度下降(551 步才收敛);
- `SGD(momentum=…)` **动量**——保留近几步的速度、旧速度渐衰,让 b 的小推力累积起来(100 步);
- `Adam` **每个权重各有一个步长**,导数再小也给足步长(88 步)。换优化器只改一行,循环不变。

**激活函数(让模型能拟合曲线):**
- `ReLU` 负数置 0、`GELU` 平滑版 ReLU、`sigmoid` 压到 (0,1)、`tanh` 压到 (−1,1)、`softmax` 把一行变成概率。
- 两层线性之间**必须夹激活**:两个线性层连着还是直线,加一个 ReLU 就能折弯。实测拟合「各时段平均车速」:直线最差 7.1mph,加一个 ReLU 掉到 1.62。

**损失函数(按任务选):**
- 回归(连续值):`MSE`(对大错敏感)/ `L1`(大错不额外加重)/ `Huber`(小错平方、大错线性,折中);
- 分类(挑类别):`CrossEntropyLoss`(多分类)/ `BCELoss`(二分类 yes/no)。

## 总结

**本质:** PyTorch 训练 = 五步循环(预测 → 损失 → backward → step → zero_grad)。张量装数、dim 从 0 数、聚合时「传的 dim 就是被吃掉的轴」;loss 把错误压成一个数(MSE 平方后平均);autograd 沿计算图自动求梯度(backward 是累加,必须 zero_grad);optimizer 持有权重并更新(SGD→动量→Adam 越走越快);nn.Module/nn.Linear/DataLoader 把裸循环变成工程化的五行。
**标签:** #PyTorch #张量Tensor #自动求导autograd #训练循环 #优化器 #激活函数 #损失函数
