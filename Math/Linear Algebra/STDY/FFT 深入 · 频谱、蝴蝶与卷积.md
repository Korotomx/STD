实信号里有哪些频率？怎么在 $O(N\log N)$ 内算出来？卷积为什么能用 FFT 加速？这篇笔记从 DFT 的加权求和出发，经过单位根、偶奇分治、蝶形与位反转，最后落到频点含义和卷积定理。线代背景见 [[L24 复矩阵与快速傅里叶变换]]。

## 约定

本笔记统一用工程 / NumPy 约定：

$$
W_N=e^{-2\pi i/N},\qquad
X[k]=\sum_{n=0}^{N-1}x[n]\,W_N^{kn},
\qquad \text{逆变换带 } \frac1N .
$$

L24 用的是 Strang 的共轭约定 $W=e^{+2\pi i/N}$；两边公式结构相同，所有虚部符号相反。跨笔记抄公式时先看指数符号。

## 探针结果

| 依赖线 | 结果 |
| --- | --- |
| 单位根、复数旋转、根求和 | ✅ 稳：$W_8^2=i$、$1+W^2+W^4+W^6=0$ 都答对 |
| FFT 递归复杂度 | ✅ 稳：$T(n)=2T(n/2)+O(n)\Rightarrow O(n\log n)$ |
| DFT 逐项公式 / 下标权重 | ❌ 缺口：把输出当成「全部相加」，$j=1$ 与 $j=2$ 混淆 |
| 频点 $\leftrightarrow$ Hz、采样率 | ❌ 未接触 |
| 卷积（连 2 点线性卷积） | ❌ 未接触 |
| 迭代 FFT / 位反转 | ❌ 未接触 |

## 依赖图

```mermaid
%%{init: {'theme':'base','themeCSS':'.nodeLabel{color:#E5E7EB!important;fill:#E5E7EB!important}.edgeLabel p{background-color:#131312!important}.edgeLabel{color:#E5E7EB!important}svg{background:transparent!important}','themeVariables':{'primaryColor':'#1E1E2E','primaryTextColor':'#E5E7EB','primaryBorderColor':'#A78BFA','lineColor':'#9CA3AF','mainBkg':'#1E1E2E','nodeBorder':'#A78BFA','clusterBkg':'#131312','edgeLabelBackground':'#131312','fontFamily':'Noto Sans CJK SC, sans-serif'}}}%%
flowchart TD
    R1["单位根 W_N^k<br/>单位圆上的等角旋转"]
    R2["卷积定义<br/>翻转·平移·逐点乘·求和"]

    D1["DFT：加权求和<br/>X[k] = Σ x[n] W_N^(kn)<br/>= 多项式在单位根上求值"]
    D2["采样与频点<br/>f_k = k·fs/N，Nyquist = fs/2"]
    D3["偶奇分治<br/>P(z) = P_e(z²) + z·P_o(z²)<br/>W_N² = W_(N/2)，W^(k+N/2) = −W^k"]
    D4["蝶形与递归 FFT<br/>X[k] = E[k] ± W^k·O[k]<br/>O(N log N)"]
    D5["迭代 FFT<br/>位反转输入 + 原地蝴蝶"]
    D6["循环卷积定理<br/>DFT(a ⊛ b) = A · B"]
    D7["线性卷积<br/>补零到 L ≥ N+M−1"]

    R1 --> D1
    D1 --> D2
    D1 --> D3
    R1 --> D3
    D3 --> D4
    D4 --> D5
    D1 --> D6
    R2 --> D6
    D6 --> D7
classDef default fill:#1E1E2E,stroke:#A78BFA,stroke-width:1.5px,color:#E5E7EB
linkStyle default stroke:#9CA3AF
```

## 节点 1 · DFT：用单位根做加权求和

### 动机

手上有 $N$ 个采样点 $x[0],\ldots,x[N-1]$，想知道「其中频率 $k$ 的成分有多强」。最直接的办法：造一个同频率的测试信号，和 $x$ 逐点相乘再求和。同相时相加变大，不同相时正负抵消。DFT 就是把这件事做到极致：测试信号取单位圆上的 $N$ 个等角点。

### 建立

取 $W_N=e^{-2\pi i/N}$。第 $k$ 个测试信号是

$$
\tau_k[n]=W_N^{kn}=e^{-2\pi ikn/N},\qquad n=0,\ldots,N-1 .
$$

$n$ 每走一步，相位前进 $2\pi k/N$；$k$ 就是「一圈里转几圈」。定义

$$
X[k]=\sum_{n=0}^{N-1}x[n]\,W_N^{kn}.
$$

- $k=0$：权重全是 $1$，$X[0]$ 就是所有样本之和（直流分量）。
- $k=1$：权重是 $1,W_N,W_N^2,\ldots$，每步转 $2\pi/N$。
- $k=2$：每步转 $4\pi/N$，一圈转两圈。

关键：第 $k$ 个输出用的是 $W_N$ 的 $0,k,2k,\ldots$ 次幂，**步长是 $k$**，不是 $1$。

### 数字例子

$N=4$，$W_4=e^{-2\pi i/4}=-i$，$x=(1,2,3,4)$。

$$
\begin{aligned}
X[0]&=1+2+3+4=10,\\
X[1]&=1+2(-i)+3(-i)^2+4(-i)^3\\
&=1-2i-3+4i=-2+2i.
\end{aligned}
$$

继续：

$$
\begin{aligned}
X[2]&=1+2(-i)^2+3(-i)^4+4(-i)^6\\
&=1-2+3-4=-2,\\
X[3]&=1+2(-i)^3+3(-i)^6+4(-i)^9\\
&=1+2i-3-4i=-2-2i.
\end{aligned}
$$

于是

$$
F_4x=(10,\,-2+2i,\,-2,\,-2-2i).
$$

> [!question] 接上面的例子：$x=(1,2,3,4)$，$N=4$，$W_4=-i$。$X[2]$ 等于多少？
> - $-2-2i$
> - $-2$
> - $2$
> - 不知道

> [!success]- ✓ 正确 —— $X[2]=-2$
> $X[2]=1+2(-i)^2+3(-i)^4+4(-i)^6=1-2+3-4=-2$。中途误选了一次 $2$，复核后确认是 $-2$；公式、复数幂和最后求和都已落地，不是概念缺口。

## 节点 2 · 采样与频点：$X[k]$ 到底是多少 Hz

### 从零重建：频率、采样率、记录时长（2026-11-06）

前面直接从复指数推到 $f_k=k f_s/N$，跳过了「频率」本身。补一条地面：

- **频率 = 每秒重复几次。** $2$ Hz 的声音一秒完整振动 $2$ 次，周期 $0.5$ s。
- **采样率 = 每秒取几个点。** $f_s=8000$ Hz 表示点间隔 $1/8000$ s。
- $N$ 个点覆盖的时长 $T=N/f_s$。$N=1024,\ f_s=8000$ 时 $T=0.128$ s。
- DFT 的第 $k$ 个测试信号，在这段记录里正好转 $k$ 圈。所以它的频率是「圈数 ÷ 时长」：

$$
f_k=\frac{k}{T}=\frac{k f_s}{N}.
$$

数字：$\Delta f=8000/1024=7.8125$ Hz，$k=64$ 即 $64\times7.8125=500$ Hz。$k$ 是格子编号，不是 Hz。

- 一个周期至少要两个采样点才看得出来，所以最高频率是 $f_s/2$，对应 $k=N/2$。

### 动机

节点 1 给出的 $X[k]$ 只是编号为 $k$ 的复数。要知道它在说哪个频率，必须把「离散下标」翻译成「每秒多少次」。

### 建立

以采样率 $f_s$ 采样，采样间隔 $T_s=1/f_s$。第 $n$ 个样本对应时间 $t_n=nT_s$，记录长度

$$
T=N T_s=\frac{N}{f_s}.
$$

测试信号 $\tau_k[n]=e^{-2\pi ikn/N}$。把它看成连续时间复指数 $e^{-2\pi i f t}$ 在 $t=nT_s$ 处的采样：

$$
e^{-2\pi i f_k nT_s}=e^{-2\pi ikn/N}
\quad\Longrightarrow\quad
2\pi f_kT_s=\frac{2\pi k}{N}
\quad\Longrightarrow\quad
f_k=\frac{k}{NT_s}=\frac{k f_s}{N}.
$$

所以第 $k$ 个 bin 的频率是

$$
f_k=\frac{k f_s}{N},
\qquad
\Delta f=\frac{f_s}{N}=\frac1T .
$$

- $k=0$：$0$ Hz，直流分量。
- $k=N/2$（$N$ 为偶数）：$f_s/2$，**Nyquist 频率**，是可表示的最高频率。
- $k>N/2$：应解释为负频率 $f_k=(k-N)f_s/N$。因为 $e^{-2\pi ikn/N}$ 对 $k$ 以 $N$ 为周期，$k$ 与 $k+N$ 是同一个测试信号。
- 实信号 $x[n]\in\mathbb R$：$X[N-k]=\overline{X[k]}$。$k$ 与 $N-k$ 是共轭对，所以只需看 $k=0,\ldots,N/2$；幅度谱偶对称、相位谱奇对称。

### 数字例子

$f_s=1000$ Hz，$N=1000$：

$$
\Delta f=1\ \text{Hz},\qquad
k=50\Rightarrow 50\ \text{Hz},\qquad
k=500\Rightarrow 500\ \text{Hz（Nyquist）}.
$$

若 $k=600$，则

$$
f_{600}=(600-1000)\cdot\frac{1000}{1000}=-400\ \text{Hz}.
$$

换一组：$f_s=8000$ Hz，$N=1024$，

$$
\Delta f=\frac{8000}{1024}=7.8125\ \text{Hz},\qquad
k=64\Rightarrow 64\times7.8125=500\ \text{Hz}.
$$

### 两个易混点

- **「频率分辨率」**：bin 间距是 $f_s/N$；补零会让 bin 更密，但真正能分辨两个邻近频率的能力由记录时长 $T$ 决定（约 $1/T$），补零不提高真实分辨率。
- **Nyquist 频率** $f_s/2$ 是能表示的最高频率；采样定理要求 $f_s>2f_{\max}$，否则高频会折叠（混叠）。

### 幅度（读谱时用）

实正弦若频率正好落在 bin 上，单边幅度

$$
A_k=\frac{2|X[k]|}{N}\quad(0<k<N/2),
$$

DC 与 Nyquist 不乘 $2$。

> 连接：$f_k=k f_s/N$ 只用到「采样间隔」和「测试信号每步转多少相位」，没有引入新假设；它把节点 1 的编号 $k$ 接上了物理频率轴。

### 概念澄清：bin、DC、Nyquist

- **bin**：DFT 输出有 $N$ 个复数，每个编号 $k$ 是一个频点 / 频率槽。把 $0$ 到 $f_s$ 的频率轴切成 $N$ 格，第 $k$ 格的中心频率是 $k f_s/N$。
- **直流分量**：$k=0$，频率为 $0$，不振荡。$X[0]=\sum_n x[n]$，所以 $X[0]/N$ 是记录内平均值 / 恒定偏置。
- **为什么 $N/2$ 是最高**：采样后 $f$ 与 $f+f_s$ 给出同一串样本，唯一频带是 $[-f_s/2,\ f_s/2)$；$k=N/2$ 对应 $f_s/2$，是边界。$k>N/2$ 应读作负频率。实信号还有 $X[N-k]=\overline{X[k]}$，$0,\ldots,N/2$ 已含全部信息。

### 确认题（2026-11-06）

> [!question] $f_s=8000$ Hz，$N=1024$ 点 DFT，峰值在 $k=32$。对应多少 Hz？
> - $250$ Hz
> - $32$ Hz
> - $500$ Hz
> - 不知道

> [!failure] ✗ 选了 500 Hz —— 正确答案是 250 Hz
> 500 Hz 是上一个例子 $k=64$ 的答案。$k$ 减半（$64\to32$），频率也减半：$500/2=250$ Hz，或直接算 $32\times7.8125=250$ Hz。先把「$k$ 与 Hz 成正比」钉住，再用乘法核对。

> [!success] ✓ 正确 —— $1000$ Hz
> $128\times7.8125=1000$ Hz，也等于 $2\times500$：$k$ 翻倍，Hz 翻倍。比例关系落地。

### 多项式视角

把 $x$ 当成系数：

$$
P(z)=x_0+x_1z+\cdots+x_{N-1}z^{N-1}.
$$

那么

$$
X[k]=P(W_N^k).
$$

也就是说，**做一次 DFT = 把多项式在 $N$ 个单位根上同时求值**。这个视角下一步会把「求值」拆成两半，这就是 FFT 的入口。

> 连接：这一步只用到你已经稳的单位根 $W_N^{kn}$；「为什么是加权求和」来自相关性/投影，而「步长是 $k$」正是你之前混淆的地方。下一节点把它翻译成频率。

## 节点 3 · 偶奇分治：把求值拆成两半

### 动机

直接算 DFT 要 $N^2$ 次乘法：$N=1024$ 约 $105$ 万次，$N=2048$ 就到 $419$ 万次。翻倍的数据量让计算量翻四倍，但数据本身没变复杂——问题是同一批数被反复相乘。能不能复用？

节点 1 的多项式视角给了入口：DFT 是在 $N$ 个单位根上同时求 $P(z)$ 的值。求值可以按系数拆开。

### 建立

把系数按奇偶分开：

$$
\begin{aligned}
P(z)&=(x_0+x_2z^2+x_4z^4+\cdots)+z\,(x_1+x_3z^2+x_5z^4+\cdots)\\
&=P_e(z^2)+z\,P_o(z^2).
\end{aligned}
$$

$P_e$ 和 $P_o$ 都只有 $N/2$ 个系数。现在代入 $z=W_N^k$，用探针里已经稳的两条事实：

$$
W_N^2=W_{N/2},\qquad (W_N^k)^2=W_{N/2}^k ;
$$

$$
W_N^{k+N/2}=-W_N^k .
$$

于是

$$
E[k]=P_e(W_{N/2}^k),\qquad O[k]=P_o(W_{N/2}^k)
$$

正好是两组 $N/2$ 点 DFT 的第 $k$ 项，而 $k+N/2$ 只用把同一个 $E[k],O[k]$ 取负：

$$
\boxed{
\begin{aligned}
X[k]&=E[k]+W_N^k\,O[k],\\
X[k+N/2]&=E[k]-W_N^k\,O[k],
\end{aligned}}
\qquad k=0,\ldots,\tfrac N2-1 .
$$

一个 $N$ 点 DFT 变成两个 $N/2$ 点 DFT，外加 $N/2$ 次乘法和 $N$ 次加减。递推

$$
T(N)=2T(N/2)+O(N)\;\Longrightarrow\;T(N)=O(N\log N).
$$

这一对「相加 / 相减」就是蝶形（butterfly）。 

```mermaid
%%{init: {'theme':'base','themeCSS':'.nodeLabel{color:#E5E7EB!important;fill:#E5E7EB!important}.edgeLabel p{background-color:#131312!important}.edgeLabel{color:#E5E7EB!important}svg{background:transparent!important}','themeVariables':{'primaryColor':'#1E1E2E','primaryTextColor':'#E5E7EB','primaryBorderColor':'#A78BFA','lineColor':'#9CA3AF','mainBkg':'#1E1E2E','nodeBorder':'#A78BFA','clusterBkg':'#131312','edgeLabelBackground':'#131312','fontFamily':'Noto Sans CJK SC, sans-serif'}}}%%
flowchart LR
    E["E[k]"] --> S["X[k] = E + W·O"]
    O["O[k]"] --> W["W_N^k · O[k]"]
    W --> S
    E --> D["X[k+N/2] = E − W·O"]
    W --> D
classDef default fill:#1E1E2E,stroke:#A78BFA,stroke-width:1.5px,color:#E5E7EB
linkStyle default stroke:#9CA3AF
```

### 数字例子

用节点 1 的同一组数据：$N=4$，$x=(1,2,3,4)$，当时暴力算出

$$
X=(10,\,-2+2i,\,-2,\,-2-2i).
$$

现在分治。偶数样本 $(1,3)$，奇数样本 $(2,4)$：

$$
E=\mathrm{DFT}_2(1,3)=(4,-2),\qquad
O=\mathrm{DFT}_2(2,4)=(6,-2).
$$

**$E$ 与 $O$ 是怎么来的（2026-11-07 补）**

$\mathrm{DFT}_2$ 不是新东西，就是节点 1 的公式取 $N=2$。$W_2=e^{-2\pi i/2}=e^{-i\pi}=-1$，两个单位根只有 $1$ 和 $-1$，所以

$$
\mathrm{DFT}_2(a,b)=\bigl(a+b,\;a-b\bigr),
$$

也就是「和与差」：

$$
E=\mathrm{DFT}_2(1,3)=(1+3,\;1-3)=(4,-2),\qquad
O=\mathrm{DFT}_2(2,4)=(6,-2).
$$

从多项式视角看是同一件事：$P_e(z)=1+3z$，$E[0]=P_e(1)=4$，$E[1]=P_e(-1)=-2$。递归到 $N=2$ 就停，因为一个 2 点蝶形只要一次加法和一次减法。

> [!question] $\mathrm{DFT}_2(5,1)$ 等于多少？
> - $(6,4)$
> - $(6,-4)$
> - $(4,6)$
> - 不知道

> [!success] ✓ 正确 —— $(6,4)$
> $5+1=6$，$5-1=4$。$k=0$ 时两个样本同号相加；$k=1$ 时第二个样本乘 $W_2=-1$ 后相加。

$W_4^0=1$，$W_4^1=-i$。逐项：

$$
\begin{aligned}
k=0:&\quad X[0]=4+1\cdot6=10, &&X[2]=4-6=-2,\\
k=1:&\quad X[1]=-2+(-i)(-2)=-2+2i, &&X[3]=-2-(-i)(-2)=-2-2i.
\end{aligned}
$$

四个数与暴力计算逐个吻合，但只做了两次 2 点 DFT。

### 连接

用到的三样东西都已就位：DFT 定义（节点 1）、$W_N^2=W_{N/2}$（探针稳）、$W^{k+N/2}=-W^k$（探针稳）。分治没有引入新事实，只是把「在 $N$ 个根上求值」重新分组。

## 下次从这里继续

> [!question] $N=4$，$x=(1,2,3,4)$，$E=(4,-2)$，$O=(6,-2)$，$W_4^1=-i$。按蝶形公式，$X[3]$ 等于多少？
> - $-2+2i$
> - $-2-2i$
> - $10$
> - 不知道

E/O 的 2 点 DFT 已在上面补讲并确认（2026-11-07）；回到这道题。答完进入节点 4（迭代 FFT 与位反转）。节点 2 已补「从零重建」并把 $k\leftrightarrow$ Hz 的比例确认过一遍。
