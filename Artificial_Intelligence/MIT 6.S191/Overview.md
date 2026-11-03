MIT 6.S191 Introduction to Deep Learning（2026 Edition）课程入口。

## STDY

- [[L1 深度学习基础]] — 感知机 / 损失 / 梯度下降 / 反向传播 / 正则化
- [[L2 循环神经网络与Transformer]] — RNN / 注意力 / Transformer
- [[L3 卷积神经网络]] — 卷积 / feature map / 池化 / 检测分割
- [[L4 深度生成模型]] — 自编码器 / VAE / GAN / CycleGAN
- [[L5 强化学习]] — Q 函数 / DQN / 策略梯度
- [[L6 语言模型与新前沿]] — 泛化失败模式 / 扩散模型 / LLM
- [[L8 AI for Science]] — emulator / no free lunch / DFT / 蛋白动力学
- [[L9 大规模并行训练]] — 显存账本 / 数据·张量·流水线·专家并行 / ZeRO·FSDP·Megatron / 5D 组合


## 进度

L1~L6 笔记全部完成；客座 L8「AI for Science」已完成（L7 暂未见材料）；L9「大规模并行训练」已完成（视频描述标 Lecture 8，按上游序列记为 L9）。

## 掌握度

状态词：待自测 / 能复述 / 能做对 / 易错。自测 = 不看笔记口述 3 个核心概念，或跑对应 lab。

| 讲 | 笔记 | 掌握 |
| --- | --- | --- |
| L1 深度学习基础 | 完成 | 待自测 |
| L2 RNN 与 Transformer | 完成 | 待自测 |
| L3 CNN | 完成 | 待自测 |
| L4 深度生成模型 | 完成 | 待自测 |
| L5 强化学习 | 完成 | 待自测 |
| L6 语言模型与新前沿 | 完成 | 待自测 |
| L8 AI for Science | 完成 | 待自测 |
| L9 大规模并行训练 | 完成 | 待自测 |

## Captures

`Captures/` 存视频截图与字幕转写，是原始材料，保持原样。

- [[MIT Introduction to Deep Learning  6.S191|L1 Foundations]]
- [[MIT 6.S191 Recurrent Neural Networks, Transformers, and Attention|L2 RNN / Transformer]]
- [[MIT 6.S191 Convolutional Neural Networks|L3 CNN]]
- [[MIT 6.S191 Deep Generative Modeling|L4 生成模型]]
- [[MIT 6.S191 Reinforcement Learning|L5 强化学习]]
- [[MIT 6.S191 Language Models and New Frontiers|L6 语言模型]] — 原文在 `CUDA/Ref/`
- [[MIT 6.S191 AI for Science|L8 AI for Science]]
- [[MIT 6.S191 Secrets of Massively Parallel Training|L9 大规模并行训练]]

## 命题速查

一条命题一行，`→` 是推理方向，末尾是落点；复习只看这张纸，卡住再点进去。

- 深度学习 = 感知机加非线性堆叠；没有非线性，多层塌成一层。[[L1 深度学习基础]]
- 训练 = 定损失 → 反向传播求梯度 → 梯度下降更新。[[L1 深度学习基础]]
- 训练误差低、测试误差高 = 过拟合，用正则化、更多数据或更小模型。[[L1 深度学习基础]]
- RNN 用隐状态携带记忆；长依赖会梯度消失。[[L2 循环神经网络与Transformer]]
- 注意力 `softmax(QKᵀ/√d)V`；Transformer 无递归，可整句并行。[[L2 循环神经网络与Transformer]]
- 卷积 = 局部连接 + 权值共享 → 参数量与图像尺寸无关，天然平移等变。[[L3 卷积神经网络]]
- 输出尺寸 `(H-K+2P)/S+1`；池化降采样、扩大感受野。[[L3 卷积神经网络]]
- 自编码器用重建目标学表示；VAE 加 KL 约束让潜空间可采样。[[L4 深度生成模型]]
- GAN 靠判别器提供信号；没有配对数据时用 CycleGAN 的循环一致性。[[L4 深度生成模型]]
- RL 没有标签只有延迟奖励：Q 函数满足 Bellman 方程。[[L5 强化学习]]
- DQN = Q 学习 + 经验回放 + 目标网络，治不稳定。[[L5 强化学习]]
- 连续动作或需要随机策略 → 策略梯度，而不是对 Q 取 argmax。[[L5 强化学习]]
- 万能逼近定理只管「能不能表示」，不管「能不能泛化」。[[L6 语言模型与新前沿]]
- 扩散模型 = 前向加噪 + 反向逐步去噪。[[L6 语言模型与新前沿]]
- LLM 本质是下一 token 预测加规模；幻觉是概率建模的副产品。[[L6 语言模型与新前沿]]
- 科学数据稀缺但方程已知 → emulator：离线用模拟器生成合成数据，训练一个前向网络替代求解。[[L8 AI for Science]]
- no free lunch 要先验，bitter lesson 说数据最终赢；用方程生成数据 = 把先验变成数据。[[L8 AI for Science]]
- DFT 把波函数（指数成本）换成电子密度（立方成本），剩下未知的交换关联泛函可用 ML 学。[[L8 AI for Science]]
- MD 的瓶颈是飞秒步长 × 毫秒事件的串行步数；emulator 把每步求解换成一次前向。[[L8 AI for Science]]
- 训练显存 ≈ 参数 + 梯度 + 优化器状态 + 激活；1B 参数约 28 GB，70B 约 2 TB。[[L9 大规模并行训练]]
- 数据并行切 batch、只做一次 all-reduce，最省通信；有效 batch 太大会伤泛化。[[L9 大规模并行训练]]
- ZeRO 分片优化器状态/梯度/参数；stage 3 让单卡放不下的大模型也能训练。[[L9 大规模并行训练]]
- 流水线按深度切、张量按层内矩阵切、序列按 token 切、专家按 MoE 切；通信密集的 TP 留在节点内。[[L9 大规模并行训练]]
- 实际训练是 5D 并行组合：DP × TP × PP × EP × CP，让通信层级匹配集群拓扑。[[L9 大规模并行训练]]
