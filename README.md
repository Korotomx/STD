> 更新：2026-11-01

主线并列如下。每天完成的内容直接追加到对应主干下，不再单独维护「今日学习」大栏和历史归档。

**复习入口**：[[Review]] · **素材入口**：[[Inbox]] — 新到的文件先登记一行，处理完改状态；原始材料只读，不移动不改正文。

## ROS 2

**进度**：课程设计「乌龟追逐」已完成并提交（2026-10-15）；基础笔记与项目总结已归档。

**今日完成**：

-

**下一步**：按需复习；有新课再开新线。

**笔记**：[[ROS2/主页]]

## 数学 · 线性代数

**进度**：MIT 18.06 L1~L20、L25 笔记完成；L21~L24（lecture 23~26）暂跳，讲次号预留。

**今日完成**：

- 整理 [[L15 正交矩阵与 Gram-Schmidt]]、[[L16 行列式的性质]] 两篇笔记，并同步主页与索引。
- 2026-10-30：整理 [[L17 行列式公式与代数余子式]]（大公式、余子式展开、5×5 行差列和数例、三对角递推），同步主页与索引。
- 2026-10-31：整理 [[L18 行列式的应用 Cramer法则与体积]]、[[L19 特征值与特征向量]]、[[L20 对角化与矩阵的幂]]；重点补 Cramer 的体积比/灵敏度作用，以及特征基换坐标的解耦视角；同步主页、索引、Overview 与 Inbox。
- 2026-11-01：用专题视频深化两篇笔记——L19 补「迹=散度」的几何意义与 $\det(e^{At})=e^{t\operatorname{tr}A}$；L20 补耦合振子（简正模式）、PCA（方差极值）、PageRank（$\lambda=1$）三个图景；同步 Overview、主页、Review 与 Inbox。
- 2026-11-01：按当前学习重点跳过 lecture 23~26，建立 L21~L24 占位笔记，讲次号保留待补。
- 2026-11-01：整理 [[L25 正定矩阵与极小值]]（lecture 27 + 习题课）——四种判别法、配方=消元、碗与马鞍、椭圆主轴、Hessian 与极小值、三对角与参数 $c$ 数例；配三张英文标注彩色图；同步 STDY、Overview、主页、Review 与 Inbox。
- 2026-11-01：为 [[L1 线性方程的几何]]、[[L10 四个基本子空间]]、[[L12 图·网络·关联矩阵]]、[[L13 正交向量与子空间]]、[[L14 投影与最小二乘]]、[[L15 正交矩阵与 Gram-Schmidt]]、[[L18 行列式的应用 Cramer法则与体积]]、[[L19 特征值与特征向量]]、[[L20 对角化与矩阵的幂]] 各补一张英文标注彩色示意图（行/列图像、四空间正交补、图与关联矩阵、正交补与勾股定理、投影与最小二乘、Gram-Schmidt、行列式与面积、特征向量几何、换坐标）。
- 2026-11-01：再补三张几何图——[[L14 投影与最小二乘]] 的散点+残差+能量等值线、[[L16 行列式的性质]] 的剪切/换行/倍乘三联图、[[L20 对角化与矩阵的幂]] 的 PCA 数据云与主方向；全部绘图代码归档为 `STDY/assets/make_la_figs.py`（英文标注、固定配色、dpi 200）。

**下一步**：L21~L24 有材料再回补；主线从 lecture 28 起，等 Ref 材料。

**笔记**：[[Math/主页]]

## AI · MIT 6.S191

**进度**：L1~L6 笔记全部完成；客座 L8「AI for Science」已完成（L7 暂未见材料）。

**今日完成**：

- 整理 6.S191 L3 CNN、L4 生成模型、L5 强化学习、L6 语言模型四篇学习笔记，同步主页与索引。
- 2026-10-30：整理 [[L8 AI for Science]]（emulator 两阶段、no free lunch 与 bitter lesson、DFT/Skala、MatGen、蛋白动力学），同步主页与索引。

**下一步**：L1~L6、L8 按需复习；L7 有材料再补。

**笔记**：[[Artificial_Intelligence/MIT 6.S191/主页|6.S191 主页]]

## AI · CUDA / TensorRT

**进度**：CUDA C01/C02 完成（向量加法 0.60 ms / 335 GB/s）；TensorRT `01_deserialize`、`02_start`、`02_runner` 完成，裸 FP16 engine 已建（711 → 1428 qps）。

**今日完成**：

- 整理 [[X01 Triton 与 TileLang]]；把 UltraLytics 三份官方文档整理成 [[YOLO 导出 格式与量化]]、[[OpenCV 高效遍历像素]]、[[TensorRT-RTX 快速入门]]。
- 2026-10-29：完成 TensorRT `02_runner`（反序列化 → 按维度 `cudaMalloc` → `setTensorAddress` → `enqueueV3` + 同步 → D2H），精简到 73 行；对照官方端到端例子理清 runtime 链路，输入填充留给预处理。

**下一步**：`03_yolo`（真实图片 → letterbox → 推理 → 解码，按需）。

**笔记**：[[Artificial_Intelligence/CUDA/主页|CUDA 主页]] · [[Artificial_Intelligence/CUDA/TensorRT 部署学习路径|TensorRT 路径]] · [[Artificial_Intelligence/UltraLytics/主页|UltraLytics 主页]]

## AI · DeepLearningRM（RoboMaster 考核）

**进度**：任务一 ResNet-18 / MNIST 完成（99.14%）；任务二 C++ ONNX + ROS2 整链完成（ZLLC mAP50 0.789，CPU ~17 FPS，报告 2026-10-21）；任务三标定 + PnP 未开始。

**今日完成**：

-

**下一步**：任务三（或补任务一/二演示视频）。

**笔记**：[[Artificial_Intelligence/DeepLearningRM/主页|DeepLearningRM 主页]]

## Python

**进度**：对象模型、dict / set、特殊性质、装饰器与上下文管理器。

**今日完成**：

-

**下一步**：异常处理、NumPy。

**笔记**：[[Artificial_Intelligence/Python/STDY/STDY|Python 笔记]]

## 英语

**进度**：有道「CS」单词本累计 758 词，按天归档；最新 2026-10-30（27 词）。

**今日完成**：

- 2026-10-30：补录 27 词（有道「CS」单词本），同步主页与索引。

**笔记**：[[English/主页]]
