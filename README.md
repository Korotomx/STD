> 更新：2026-11-04

主线并列如下。每天完成的内容直接追加到对应主干下，不再单独维护「今日学习」大栏和历史归档。

**复习入口**：[[Review]] · **素材入口**：[[Inbox]] — 新到的文件先登记一行，处理完改状态；原始材料只读，不移动不改正文。

## ROS 2

**进度**：课程设计「乌龟追逐」已完成并提交（2026-10-15）；基础笔记与项目总结已归档。

**今日完成**：

-

**下一步**：按需复习；有新课再开新线。

**笔记**：[[ROS2/Overview]]

## 数学 · 线性代数

**进度**：MIT 18.06 L1~L23、L25 笔记完成；专题笔记《马尔可夫链》《线性规划与单纯形法》已完成；L24（lecture 26）暂跳，讲次号预留。

**今日完成**：

- 2026-11-04：新建专题笔记 [[马尔可夫链]]（链的随机过程视角 + MCMC/PageRank/LLM）与 [[线性规划与单纯形法]]（Simplex 视频转写），同步 STDY、Ref、Inbox、Concentrated、Overview。
- 2026-11-03：补写 [[L23 对称矩阵与正定矩阵]]（lecture 25 + 18.06SC 习题课）——实特征值与正交特征基、谱定理 $A=Q\Lambda Q^{\mathsf T}$、投影叠加/主轴定理、主元符号=特征值符号、正定四判据与两个 $2\times2$ 例子、$A^{\mathsf T}A$ 与列满秩。
- 2026-11-03：补写 [[L22 马尔可夫矩阵与傅里叶级数]]（lecture 24 + 18.06SC 习题课）——列和为 $1$ → $\lambda=1$、$A-I$ 奇异与平稳分布、收敛速度、加州/马萨诸塞与两状态粒子两例、正交基展开、Fourier 系数积分公式；延伸整理 Metropolis–Hastings（细致平衡、burn-in、多峰陷阱）。同步 Ref 索引、STDY、Concentrated 与 Overview。
- 2026-11-02：补写 [[L21 微分方程与矩阵指数]]（lecture 23 + 18.06SC 习题课）——纯指数解、$e^{At}=Se^{\Lambda t}S^{-1}$、稳定性与左半平面、迹/行列式判据、高阶方程转 companion 矩阵、三阶数例；配相图/稳定区图。另按专题视频给 [[L12 图·网络·关联矩阵]] 增补「矩阵即图」一节（邻接矩阵、强连通分量、置换相似、Frobenius 标准形）并配块结构图；同步 Ref 索引、STDY、Overview 与主页。
- 整理 [[L15 正交矩阵与 Gram-Schmidt]]、[[L16 行列式的性质]] 两篇笔记，并同步主页与索引。
- 2026-10-30：整理 [[L17 行列式公式与代数余子式]]（大公式、余子式展开、5×5 行差列和数例、三对角递推），同步主页与索引。
- 2026-10-31：整理 [[L18 行列式的应用 Cramer法则与体积]]、[[L19 特征值与特征向量]]、[[L20 对角化与矩阵的幂]]；重点补 Cramer 的体积比/灵敏度作用，以及特征基换坐标的解耦视角；同步主页、索引、Overview 与 Inbox。
- 2026-11-01：用专题视频深化两篇笔记——L19 补「迹=散度」的几何意义与 $\det(e^{At})=e^{t\operatorname{tr}A}$；L20 补耦合振子（简正模式）、PCA（方差极值）、PageRank（$\lambda=1$）三个图景；同步 Overview、主页、Review 与 Inbox。
- 2026-11-01：按当前学习重点跳过 lecture 23~26，建立 L21~L24 占位笔记，讲次号保留待补。
- 2026-11-01：整理 [[L25 正定矩阵与极小值]]（lecture 27 + 习题课）——四种判别法、配方=消元、碗与马鞍、椭圆主轴、Hessian 与极小值、三对角与参数 $c$ 数例；配三张英文标注彩色图；同步 STDY、Overview、主页、Review 与 Inbox。
- 2026-11-01：为 [[L1 线性方程的几何]]、[[L10 四个基本子空间]]、[[L12 图·网络·关联矩阵]]、[[L13 正交向量与子空间]]、[[L14 投影与最小二乘]]、[[L15 正交矩阵与 Gram-Schmidt]]、[[L18 行列式的应用 Cramer法则与体积]]、[[L19 特征值与特征向量]]、[[L20 对角化与矩阵的幂]] 各补一张英文标注彩色示意图（行/列图像、四空间正交补、图与关联矩阵、正交补与勾股定理、投影与最小二乘、Gram-Schmidt、行列式与面积、特征向量几何、换坐标）。
- 2026-11-01：再补三张几何图——[[L14 投影与最小二乘]] 的散点+残差+能量等值线、[[L16 行列式的性质]] 的剪切/换行/倍乘三联图、[[L20 对角化与矩阵的幂]] 的 PCA 数据云与主方向；全部绘图代码归档为 `STDY/assets/make_la_figs.py`（英文标注、固定配色、dpi 200）。

- 2026-11-01：整理 [[L12 图·网络·关联矩阵]]、[[L13 正交向量与子空间]] 两篇笔记并配图；把 DeepLearning 下「曲线拟合的概率视角」并入 [[L14 投影与最小二乘]]，补概率/正则化对照图。
- 2026-11-01：建立 [[Linear Algebra/Ref/Ref|Ref 原始材料索引]]（18.06 字幕、18.06SC、3b1b、数学不难、专题视频全部登记）；线性代数总入口统一为 [[Linear Algebra/Overview|Overview]]（含命题速查），原「主页」改为跳转。
- 2026-11-01：按 `Downloads/LinearAlgebra` 15 份讲义整理 [[Linear Algebra/Exam|Exam]]（逐讲知识点 + ✅/◐/○ 覆盖标记 + 未学清单 + 参照 Threshold test I 的备考建议）；按主题汇编已学定理与性质为 [[Linear Algebra/Concentrated|Concentrated]]。
- 2026-11-01：给 [[L19 特征值与特征向量]] 补「速算技巧」——信号表（行和/秩 1/三角/置换/零化多项式）、行和与秩 1 数例、$p(A)=O\Rightarrow p(\lambda)=0$、$2\times2$/$3\times3$ 展开式、特征向量快取，以及「行变换不保特征值」的坑；同步 Concentrated。

**下一步**：补 Exam 里标记 ○ 的四块算法缺口（初等变换/标准形、坐标与过渡矩阵、正交对角化、二次型标准形）；L24 有材料再回补；主线从 lecture 28 起，等 Ref 材料。

**笔记**：[[Math/Overview]]

## AI · MIT 6.S191

**进度**：L1~L6 笔记全部完成；客座 L8「AI for Science」已完成（L7 暂未见材料）；L9「大规模并行训练」已完成。

**今日完成**：

- 2026-11-03：整理 [[L9 大规模并行训练]]（Mathias Lechner 客座讲，视频描述标 Lecture 8，按序列记为 L9）——显存账本与激活检查点/offload、集群拓扑、数据/优化器/流水线/张量/序列/专家并行、ZeRO/FSDP/Megatron、5D 组合与问答；同步 6.S191 主页与 STDY 索引。
- 整理 6.S191 L3 CNN、L4 生成模型、L5 强化学习、L6 语言模型四篇学习笔记，同步主页与索引。
- 2026-10-30：整理 [[L8 AI for Science]]（emulator 两阶段、no free lunch 与 bitter lesson、DFT/Skala、MatGen、蛋白动力学），同步主页与索引。

**下一步**：L1~L6、L8、L9 按需复习；L7 有材料再补。

**笔记**：[[Artificial_Intelligence/MIT 6.S191/Overview|6.S191 主页]]

## AI · CUDA / TensorRT

**进度**：CUDA C01/C02 完成（向量加法 0.60 ms / 335 GB/s）；TensorRT `01_deserialize`、`02_start`、`02_runner` 完成，裸 FP16 engine 已建（711 → 1428 qps）。

**今日完成**：

- 整理 [[X01 Triton 与 TileLang]]；把 UltraLytics 三份官方文档整理成 [[YOLO 导出 格式与量化]]、[[OpenCV 高效遍历像素]]、[[TensorRT-RTX 快速入门]]。
- 2026-10-29：完成 TensorRT `02_runner`（反序列化 → 按维度 `cudaMalloc` → `setTensorAddress` → `enqueueV3` + 同步 → D2H），精简到 73 行；对照官方端到端例子理清 runtime 链路，输入填充留给预处理。

**下一步**：`03_yolo`（真实图片 → letterbox → 推理 → 解码，按需）。

**笔记**：[[Artificial_Intelligence/CUDA/Overview|CUDA 主页]] · [[Artificial_Intelligence/CUDA/TensorRT 部署学习路径|TensorRT 路径]] · [[Artificial_Intelligence/UltraLytics/Overview|UltraLytics 主页]]

## AI · DeepLearningRM（RoboMaster 考核）

**进度**：任务一 ResNet-18 / MNIST（99.14%）与任务二 C++ ONNX + ROS2 + TensorRT（ZLLC mAP50 0.789，130~240 FPS）完成；任务三不做，RM 线 2026-11-01 收官。

**今日完成**：

- 2026-11-02：确认 RM 线收官，任务三不做，不再排期。

**下一步**：已收官，不再安排；隔较长时间后需要时再按需复习。

**笔记**：[[Artificial_Intelligence/DeepLearningRM/Overview|DeepLearningRM 主页]]

## Python

**进度**：对象模型、dict / set、特殊性质、装饰器与上下文管理器。

**今日完成**：

-

**下一步**：异常处理、NumPy。

**笔记**：[[Artificial_Intelligence/Python/STDY/STDY|Python 笔记]]

## 英语

**进度**：有道「CS」单词本累计 819 词，按天归档；最新 2026-11-03（28 词）。

**今日完成**：

- 2026-11-03：补录 61 词（10-31 起积压），成 [[2026-10-31]]（8）、[[2026-11-01]]（25）、[[2026-11-03]]（28，含 11-02 的 2 词按攒批规则并入）；同步 Overview 索引。
- 2026-10-30：补录 27 词（有道「CS」单词本），同步主页与索引。

**笔记**：[[English/Overview]]
