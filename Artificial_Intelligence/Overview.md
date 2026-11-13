> AI / 深度学习入口。几条线并列，进度与今日完成写在各自主干下。

## ALGO（数据结构与算法）

- 进度：A01 LCA、A02 FSM、A03 PNG/QOI 已完成；A04 GCD/LCM、A05 进制转换已从 `Math/trival` 迁入，待按 learn 格式重写
- 下一步：重写 A04/A05；整理 Ref 里的 Every Data Structure、The Most Ambiguous Concept
- 笔记：[[ALGO/Overview|ALGO 主页]]

## MIT 6.S191（主线课程）

- 进度：L1~L6 笔记全部完成（基础 / RNN / CNN / 生成模型 / 强化学习 / 语言模型）；L8「AI for Science」、L9「大规模并行训练」已完成
- 下一步：按需复习；L7 有材料再补；关注 2026 版的 guest lectures 与 labs
- 笔记：[[MIT 6.S191/Overview|6.S191 主页]]

## CUDA / TensorRT

- 进度：CUDA C01/C02；TensorRT `01_deserialize`、`02_start`、`02_runner`、`03_yolo` 完成——GPU 预处理核（letterbox + 双线性 + HWC→CHW）直接写 engine 输入，全链路闭环
- 下一步：分阶段计时 → postprocess 搬 GPU → pinned memory + 显式 stream / `cudaMemcpyAsync` overlap
- 笔记：[[CUDA/Overview|CUDA 主页]] · [[CUDA/TensorRT 部署学习路径|TensorRT 路径]]
- 部署参考：[[UltraLytics/Overview|UltraLytics]] — YOLO 导出与量化、OpenCV 像素遍历、TensorRT-RTX 快速入门

## DeepLearningRM（RoboMaster 考核）

- 进度：任务一 ResNet-18 / MNIST 完成；任务二 C++ ONNX + ROS2 整链完成（mAP50 0.789，CPU ~17 FPS，报告 2026-10-21）；任务三不做，RM 线 2026-11-01 收官
- 下一步：已收官，不再安排；按需复习
- 笔记：[[DeepLearningRM/Overview|DeepLearningRM 主页]]

## Python

- 进度：对象模型、dict / set、特殊性质、装饰器与上下文管理器
- 下一步：异常处理、NumPy
- 笔记：[[Python/STDY/STDY|Python 笔记]]

## VibeCoding（AI 编程）

- 进度：L1 流程与环境、L2 仓库与工具、L3 LLM 的限制
- 笔记：[[VibeCoding/Overview|VibeCoding 主页]]

## Projects（项目归档）

- 笔记：[[Projects/Overview|Projects 主页]] — NIKKE 自动化、架构决策方法

## Unlimited（补充 / 零散）

- 视频与文章笔记：信息论、RNN 门控、神经网络对称性、曲线拟合、IoU、双线性插值、量化 等；AI 代码评审、AI 学习系统、LLM Wiki、Shannon 创造性思维已并入 Sight
- 笔记：[[Unlimited/Overview|Unlimited 主页]]

## 环境

- Python 3.11（`dl_env`）+ PyTorch 2.11（CUDA 12.8）
- GPU：RTX 5060 8GB（WSL2）
