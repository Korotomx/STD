> 更新：2026-11-05

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

- 2026-11-05：给 [[L5 转置·置换·向量空间]] 补「转置的几何意义」——点积写成 $v^{\mathsf T}x$、剪切把点积从 2 变 6、$A^{\mathsf T}A=I$ 才保点积、只变换 $x$ 时另一侧用 $(A^{-1})^{\mathsf T}$、不可逆时用 $x\cdot(A^{\mathsf T}\bar v)=(Ax)\cdot\bar v$、SVD 下 $A^{\mathsf T}=R_2\Sigma R_1^{\mathsf T}$、转置 vs 逆；配四联图 `L5_transpose_dot_product.png`（剪切/转置配对/正交旋转/SVD）和 manim 动画 `L5_four_svd_transforms.gif`（$A,A^{-1},A^{-\mathsf T},A^{\mathsf T}$ 四条「旋转—缩放—旋转」路线并行演示）；同步 STDY、Ref、Concentrated、Inbox 与 Overview。
- 2026-11-04：给 [[L2 消元]]、[[L3 矩阵乘法与逆]]、[[L4 A=LU 分解]]、[[L5 转置·置换·向量空间]]、[[L22 马尔可夫矩阵与傅里叶级数]]、[[L23 对称矩阵与正定矩阵]] 补 7 张英文标注示意图（消元行图像与 $E_{21}A=U$、秩 1 外积与奇异塌缩、$LU$ 账本与多右端运算量、转置/子空间/列空间、马尔可夫收敛、Fourier 部分和与系数衰减、谱分解主轴与投影伸缩）；绘图代码并入 `STDY/assets/make_la_figs.py`。
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

**进度**：CUDA C01/C02 完成（向量加法 0.60 ms / 335 GB/s）；TensorRT `01_deserialize`、`02_start`、`02_runner`、`03_yolo` 完成——CPU 预处理已换成 GPU `warp_affine` 核（letterbox + 双线性 + BGR→RGB + /255 + HWC→CHW），结果直接写 engine 输入，全链路闭环，框/关键点与 CPU 版一致（整图平均像素差 `0.036`）。

**今日完成**：

- 2026-11-05：完成 TensorRT `03_yolo` GPU 预处理核——`preprocess_kernel.cu`（`affine` + `warp_affine`，16×16 block，每线程一个目标像素）替代 `cv::resize + copyMakeBorder + blobFromImage`；原图整块 `cudaMemcpy` H2D 后，kernel 直接写 engine 输入 buffer，省掉 CPU 预处理和 blob 的 H2D，只保留原图一次 H2D；逆仿射矩阵经 `__constant__ float mat[6]` + `cudaMemcpyToSymbol` 传入；构建拆成 `nvcc -c` + `g++-14` 链接，记下 `-ccbin g++-14`、`-Xcompiler=-U_GNU_SOURCE` 两个坑。验证：GPU 版与 CPU 版框、8 关键点完全一致，`mean diff 0.036`（差异集中在框线边缘）。另把宿主手推的逆仿射矩阵换成 `Affine` 类（正/逆两份，全浮点不取整，解码直接用 `mat_inv`），与导师代码对齐；笔记补「矩阵运算：host 推导，device 求值」。
- 2026-11-04：完成 TensorRT `03_yolo` CPU 版——`imread` → letterbox（114 灰边）→ `cv::dnn::blobFromImage`（/255、BGR→RGB、HWC→CHW）→ `cudaMemcpy` 一次线性拷贝 → `enqueueV3(nullptr)` 默认流 → 解码逆 letterbox → 画框/关键点；弄通「连续内存 vs ROI」「`cudaMemcpy2D`+`cudaMallocPitch` 何时才需要」「先默认流后 stream」三点；数据集移入 `trt_lab/datasets`，修复 `infer_engine.py` 路径。
- 整理 [[X01 Triton 与 TileLang]]；把 UltraLytics 三份官方文档整理成 [[YOLO 导出 格式与量化]]、[[OpenCV 高效遍历像素]]、[[TensorRT-RTX 快速入门]]。
- 2026-10-29：完成 TensorRT `02_runner`（反序列化 → 按维度 `cudaMalloc` → `setTensorAddress` → `enqueueV3` + 同步 → D2H），精简到 73 行；对照官方端到端例子理清 runtime 链路，输入填充留给预处理。

**下一步**：分阶段计时（预处理 kernel / H2D / 推理 / D2H，对照 Python 2.3/6.0 ms）→ postprocess 搬 GPU → pinned memory + 显式 stream / `cudaMemcpyAsync` overlap。

**笔记**：[[Artificial_Intelligence/CUDA/Overview|CUDA 主页]] · [[Artificial_Intelligence/CUDA/TensorRT 部署学习路径|TensorRT 路径]] · [[Artificial_Intelligence/UltraLytics/Overview|UltraLytics 主页]]

## AI · DeepLearningRM（RoboMaster 考核）

**进度**：任务一 ResNet-18 / MNIST（99.14%）与任务二 C++ ONNX + ROS2 + TensorRT（ZLLC mAP50 0.789，130~240 FPS）完成；任务三不做，RM 线 2026-11-01 收官。

**今日完成**：

- 2026-11-02：确认 RM 线收官，任务三不做，不再排期。

**下一步**：已收官，不再安排；隔较长时间后需要时再按需复习。

**笔记**：[[Artificial_Intelligence/DeepLearningRM/Overview|DeepLearningRM 主页]]

## AI · Unlimited（补充）

**进度**：补充/零散笔记持续更新；最新《量化 让模型更小更快》（2026-11-05）。

**今日完成**：

- 2026-11-05：整理 [[量化 让模型更小更快]]（IBM Technology 视频）——70B 模型 FP16 140 GB / INT8 70 GB / INT4 35 GB 的比特账本、逐层 scale+round 映射、FP16/FP8/INT8/INT4 对照、PTQ vs QAT；配显存条形图与量化数轴图；同步 Unlimited 与 AI 主页、Inbox。

**下一步**：按素材继续补；索引见 [[Artificial_Intelligence/Unlimited/Overview|Unlimited 主页]]。

**笔记**：[[Artificial_Intelligence/Unlimited/Overview|Unlimited 主页]]

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
