![](https://www.youtube.com/watch?v=YH1n1OEpAF4)

What does eigenvalue decomposition mean geometrically?  
Why are eigenvectors the most stable directions of a matrix?  
  
In this video, we provide a geometric explanation of Eigenvalue Decomposition (EVD),  
with a focus on the spectral decomposition of real symmetric matrices.  
We explore how a matrix transforms space, identify eigenvectors as invariant directions,  
and see how eigenvalues quantify stretching or compression along those directions.  
  
In the 2×2 case, spectral decomposition can be understood as a clear geometric process:  
rotate → scale → rotate back.  
A matrix transforms the unit circle into a rotated ellipse, where:  
• eigenvalues determine the lengths of the semi-major and semi-minor axes  
• eigenvectors determine the orientation of the ellipse  
  
The video also reveals the natural connection between spectral decomposition and  
Principal Component Analysis (PCA).  
Since the covariance matrix is real and symmetric, its spectral decomposition  
directly uncovers the most important directions of variation in the data.  
  
\--------------------------------------------------  
  
特征值分解在几何上究竟意味着什么？  
为什么特征向量代表矩阵作用下最稳定的方向？  
  
本视频通过几何直观讲解方阵的特征值分解，  
重点关注实对称矩阵的谱分解（Spectral Decomposition）。  
我们展示矩阵如何作用于空间，  
解释为什么特征向量对应矩阵变换下的不变方向，  
以及特征值如何刻画在这些方向上的伸缩强度。  
  
在 2×2 的情形下，谱分解可以理解为一个非常清晰的几何过程：  
旋转 → 缩放 → 再旋转回去。  
矩阵将单位圆变换为一个旋转的椭圆，其中：  
• 特征值对应椭圆的半长轴与半短轴长度  
• 特征向量对应椭圆的方向  
  
视频还展示了谱分解与 PCA 主成分分析之间的自然联系。  
由于协方差矩阵是实对称矩阵，  
其谱分解直接揭示了数据中最重要的变化方向。  
  
\--------------------------------------------------  
  
Chapters:  
00:00 Intuition of Eigenvectors & Eigenvalues (Av = λv) ｜特征值与特征向量的直观理解  
02:51 A Symmetric Matrix Turns a Unit Circle into a Rotated Ellipse ｜单位圆 → 旋转椭圆  
04:47 Eigenvalue Decomposition: A = VΛV⁻¹ ｜特征值分解形式  
07:28 Spectral Decomposition: Rotate → Scale → Rotate Back ｜谱分解的几何过程  
12:08 Spectral Decomposition of an n×n Real Symmetric Matrix ｜高维实对称矩阵  
13:13 Connection Between Spectral Decomposition and PCA ｜与 PCA 的关系  
14:05 Eigenvalue Decomposition of Non-Symmetric Matrices ｜非对称矩阵的几何理解  
  
\--------------------------------------------------  
  
📘 Open-source books & Python code:  
https://github.com/Visualize-ML  
  
🎬 Full playlist:  
https://youtube.com/playlist?list=PLYvOmMwPgVxPfHD82QM07gKwaQ5FhPa07  
  
☕ Support the project:  
https://buymeacoffee.com/drginger\_jiang  
  
📩 Contact:  
jiang.visualize.ml@gmail.com  
  
\--------------------------------------------------  
  
This video is part of \*Linear Algebra Made Easy\* (Iris Book Series),  
an open-source project focused on building geometric intuition  
for linear algebra, data analysis, and machine learning.  
  
We create visual explanations to make mathematics simple, elegant, and accessible.  
If this video helped something click, consider liking 👍 sharing, and subscribing 🔔  
You can also support the project via ❤️ Super Thanks or ☕ Buy Me a Coffee.  
  
English & Chinese subtitles available.

## Transcript

### Intuition of Eigenvectors & Eigenvalues (Av = λv) ｜特征值与特征向量的直观理解

**0:01** · 这个视频聊一聊特征值分解 让我们先看一个简单的矩阵乘法 A₂ₓ₂ 乘以水平正方向的单位向量 e₁， 得到的仍然是一个 2 行 1 列的列向量 这个列向量仍然代表平面上的一个点或者一个方向

**0:27** · 它描述了单位向量 e₁ 经过方阵 A 线性变换后的位置 在平面上，给定一个单位向量 v 不断改变 v 的方向， 一般情况下，Av 的结果对应的向量的长度和方向都会随之变化

**0:50** · 然而，在所有可能的方向当中， 存在一些特殊的单位向量 当我们用矩阵 A 去作用它们时， 结果向量的方向为同向或反向， 只是长度发生了缩放 换句话说，给定方阵 A， 如果对于某个非零向量 v 满足 Av = λv

**1:20** · 则意味着方阵 A 对 v 的作用 仅仅是让它变长或变短，而方向不变 请大家格外注意， 这里说的“方向不变”包括两种情形： 一种是与原方向相同，另一种是与原方向相反 两者统称“方向不变” 这时，我们称 v 为方阵 A 的特征向量，λ 为特征值

**1:51** · 特征向量代表方阵 A “固有向量”或“自身方向” 特征值则代表方阵 A “固有值”或“自身值” 寻找方阵的特征值和特征向量， 就相当于探索这个方阵的本质特征 这个过程揭示了矩阵在空间最核心的作用方式： 在哪些方向上，矩阵只是简单地拉伸或压缩，而不改变方向

**2:22** · 换句话说， 特征向量代表了矩阵作用下最稳定的方向， 而特征值则刻画了这种作用的强度 实际上，特征值分解对应的英文 叫做 Eigenvalue decomposition 而 eigen 来自德语 在德语当中，eigen的意思就是“自身的”、“固有的” 为了方便大家理解， 我们看一下如何用几何视角来理解特征值分解

### A Symmetric Matrix Turns a Unit Circle into a Rotated Ellipse ｜单位圆 → 旋转椭圆

**2:51** · 首先看第一个例子 屏幕上大家看到的方阵 A 是一个对称矩阵 让矩阵 A 对屏幕上的单位向量进行线性变换

**3:07** · 大家知道， 平面上的单位向量如果起点位于原点， 则它们的终点落在单位圆的圆周上 我们发现几个特殊向量， 经过方阵 A 的线性变换后， 它们的方向不变，仅仅长度发生缩放 更有意思的是， 大家可以发现，单位圆变成了一个旋转的椭圆 首先让我们来看，单位向量 v₁, 经过 A 线性变换后，得到 2v₁

**3:42** · 这告诉我们，v₁ 是 A 的特征向量，对应的特征值 λ₁ = 2 v₁ 的反向量 -v₁ 也满足，屏幕上的等式关系 这告诉我们， 给定特征值，对应的特征向量并不唯一 特征向量的任意非零标量 k 缩放结果 仍然是该特征值 λ₁ = 2 对应的特征向量 因此，所有的特征向量构成一条过原点的直线

**4:18** · 一般情况下， 我们会把特征向量进一步处理为单位向量 因为在特征值分解当中， 我们真正关心的是向量所代表的方向， 而不是它们的长度 观察单位圆，我们还发现另外一个向量 v₂ 经过 A 的线性变换之后，变成 0.5v₂ v₂ 也是 A 的特征向量，对应的特征值 λ₂ = 0.5

### Eigenvalue Decomposition: A = VΛV⁻¹ ｜特征值分解形式

**4:47** · 到目前为止，我们已经得到两个矩阵乘法 特征值分解肯定是一种矩阵分解 也就是把矩阵写成若干矩阵的连乘 大家可能会问， 为什么到现在我们还没有看到矩阵分解这种形式呢？

**5:08** · 下面我们就试着把这两个矩阵乘法整理成屏幕上的形式 很容易通过计算得到， V 的行列式不为 0，因此 V 可逆 所以，我们可以把 A 写成屏幕上这种矩阵分解的形式

**5:32** · 至此，我们便得到了大家想要看到的特征值分解 反过来看， 矩阵 A 左乘 V⁻¹，右乘 V，便得到对角方阵 Λ

**5:47** · 能写成屏幕上这种形式的矩阵叫可对角化矩阵 可对角化矩阵的几何意义在于， 它把复杂的几何变换拆解成沿特征向量方向的独立伸缩， 使问题变得简单 需要大家注意的是， 对于任意实数方阵 A， 存在特征值、特征向量并不代表可以对角化 刚才提到的，特征向量线性无关 ( 即 V 可逆 ) 便是重要的条件

**6:22** · 需要大家格外注意的是， 方阵 A 列向量线性无关并不能保证 A 的特征向量线性无关！

**6:33** · 让我们再仔细的地看一看 A 的特征值分解 大家是否惊奇地发现， 上式中的 V 正是之前视频提到过的旋转矩阵！

**6:47** · 旋转矩阵 V 是一种正交矩阵，因此 V⁻¹ = Vᵀ 从几何角度来看， A 的特征值分解对应的几何变换便拆解为“旋转 → 缩放 → 旋转” 需要给大家提醒一点： 能够产生这样的几何变换的分解 是因为 A 是一个实对称矩阵！

**7:14** · 简单来说， 实对称矩阵是一个对称方阵，所有的元素均为实数 而实对称矩阵的特征值分解有自己的名字： 谱分解 (spectral decomposition) 下面聊一聊这个谱分解 给定一个实对称矩阵 A， 它的谱分解可以写成屏幕上的形式 V 为正交矩阵，满足 VVᵀ = VᵀV = I

### Spectral Decomposition: Rotate → Scale → Rotate Back ｜谱分解的几何过程

**7:48** · 为了方便讨论以及可视化， 本视频中给出的正交矩阵对应的几何变换 被简单的视为纯粹的旋转 实际上，除了旋转以外， 镜像变换、坐标轴置换等操作也都对应正交矩阵 Λ 为对角方阵，Λ 的主对角线元素为 A 的特征值

**8:16** · 大家可以看到，Λ 对应的操作为缩放 因此，谱分解的结果，从几何角度来看， 可以理解为“先旋转，再缩放，再旋转回去”的过程 让我们回顾视频开头的例子， 看一下矩阵 A 如何作用于它的特征向量 v₁ 和 v₂ 经过 A 的变换，v₁ 的长度放大为 2 倍， v₂ 的长度缩小为1/2

**8:49** · A 的谱分解告诉我们， A 的几何操作可以分解为“旋转 > 缩放 > 旋转” 所以矩阵乘法 Ax 可以写成 VΛVᵀx

**9:05** · 需要大家格外注意的是几何操作的先后顺序 也就是说，先用 Vᵀ 旋转，再用 Λ 缩放，最后再用 V 旋转 先看一下 Vᵀ 对 v₁ 的旋转结果 大家可以发现，v₁ 变成了水平方向的单位向量 e₁ Vᵀ 对 v₂ 的旋转结果，得到的是竖直正方向的单位向量 e₂

**9:37** · 而单位圆的形状没有发生变化，仅仅是角度发生了旋转 然后，我们再用 Λ 进行缩放 很明显，单位圆变成了椭圆 椭圆的半长轴和半短轴是描述椭圆形状的最重要的两条线段

**9:58** · 这是我们在高中阶段学过的知识 让我们简单回顾一下 椭圆的中心到椭圆上最远点的距离称为半长轴， 它决定了椭圆在最长方向的尺度； 椭圆中心到椭圆上最近点的距离称为半短轴， 它决定了椭圆在最短方向上的尺度 半长轴和半短轴共同决定了椭圆的扁平程度与整体几何形状

**10:29** · 给大家 5 秒钟，请大家思考: 屏幕上的这个椭圆的半长轴、半短轴的长度是什么？

**10:43** · 答案很明显，对称矩阵 A 的特征值 λ₁、λ₂ 就分别是椭圆的半长轴、半短轴的长度 最后，再用 V 做反向旋转，我们得到一个旋转椭圆 显然，旋转椭圆的大小没有变化，半长轴、半短轴没有变化

**11:09** · 只不过半长轴的方向对应 v₁ ，半短轴的方向对应 v₂ 正交矩阵 V 的列向量构成一个规范正交基 在 \[v₁, v₂\] 中观察椭圆，旋转椭圆变成了正椭圆 因此，几何角度来看， 谱分解相当于帮我们找到一个坐标系将椭圆摆正！

**11:34** · 而得到的特征值， 实际上帮我们找到了旋转椭圆的半长轴、半短轴的长度 总结来说， 谱分解帮助我们找到旋转椭圆的半长轴、半短轴的方向与长度 换句话说，特征值对应半轴的长度，特征向量对应半轴的指向

**11:59** · 有了谱分解， 我们就可以把椭圆的结构完全拆解出来， 使其形状和方向都变得清晰可解释 理解了 2 × 2 实对称矩阵 A 的谱分解之后， 让我们聊一聊更一般的谱分解 n × n 实对称矩阵 A，谱分解后的结果为 A = VΛ Vᵀ

### Spectral Decomposition of an n×n Real Symmetric Matrix ｜高维实对称矩阵

**12:29** · 用矩阵乘法第二视角——外积视角 把 A = VΛ Vᵀ 写成屏幕上看到的形式 大家是否惊奇地发现， 一个实对称矩阵谱分解之后 就是将它“拆解” 成 n 个矩阵的叠加

**12:53** · 而得到的这 n 个矩阵， 就像是白光通过棱镜被分解时， 展现出一系列有序排列的颜色带， 这些不同颜色的光代表 不同波长的成分 其中的 λ 的值越大， 则代表对应的方向越重要 这种思路对主成分分析具有重要的意义 主成分分析的目标， 就是从数据的协方差矩阵中找到最重要的方向，

### Connection Between Spectral Decomposition and PCA ｜与 PCA 的关系

**13:25** · 而协方差矩阵本身就是一个实对称矩阵 通过谱分解， 我们自然能够将数据的方差分解到不同的正交方向上 并按照特征值大小排序，进而识别出最“亮”的颜色 也就是方差信息最大的主方向 保留最大的几个特征值以及对应的特征向量， 就等价于保留光谱中最强的部分， 从而达到数据的降维、去噪以及提取核心结构的目的

**14:01** · 主成分分析是我们将在后续视频特别介绍的内容 实对称矩阵的特征值分解结果对应“旋转 → 缩放 → 旋转”； 但是，很多非对称矩阵的特征值分解结果 对应的几何操作就没有那么显而易见了 下面，让我们看一个简单的例子 给定屏幕上非对称方阵 A 特征值分解得到的结果

### Eigenvalue Decomposition of Non-Symmetric Matrices ｜非对称矩阵的几何理解

**14:38** · 显然 V 不是正交矩阵 大家可以试着算算 V@Vᵀ 和 Vᵀ@V 的结果 但是细心的观众可以发现， V 可以拆解成两个矩阵的乘积 其中 K 是沿横轴剪切，S 则代表缩放 反向来看，V⁻¹的作用相当于先用 S⁻¹ 进行缩放，再用 K⁻¹剪切

**15:09** · 矩阵 A 的特征值分解可以拆解成这样的一系列动作： “缩放 (S⁻¹) → 剪切 (K⁻¹) → 缩放 (Λ) → 剪切 (K) → 缩放 (S)” 这比之前视频提到的实对称矩阵谱分解 对应的几何操作——旋转、缩放、旋转——复杂得多

**15:27** · 当然，特征值分解的世界并不止于此 有些实数方阵的特征值分解 得到的特征值和特征向量会以复数的形式出现 它们同样蕴含着丰富的几何与代数的意义 关于特征值分解， 还有很多有趣的性质与应用 等待大家自己去发现去探索 这个视频就到这里，我们下一个视频再见

关联：[[Linear Algebra/主页|线性代数]]
