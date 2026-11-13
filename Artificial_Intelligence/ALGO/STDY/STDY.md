ALGO 笔记索引。原始材料在 [[ALGO/Ref/Ref|Ref]]，只读；每篇笔记在正文里链回材料。

## 数据结构与算法

- [[A01 最低公共祖先 LCA]] — LCA → RMQ 欧拉归约、稀疏表、分块 + 父数组、±1 块类共享查表；目标是 $O(n)$ 预处理 / $O(1)$ 查询，第 10 节是复杂度账本。
- [[A02 有限状态机 FSM]] — 五元组与状态图、正则六种基本构造、DFA 转移表、以太网帧头检测、Kleene 定理与子集构造、Myhill–Nerode 最小状态数。
- [[A03 PNG 无损压缩与 QOI]] — 霍夫曼、游程、LZ77、Filtering、Deflate 两道工序，以及 QOI 用更简单规则换速度的取舍。
- [[A04 辗转相除法 GCD LCM]] — 带余除法恒等式、复杂度 $O(\log\min(a,b))$、`std::gcd`/`std::lcm`、防溢出与扩展欧几里得。
- [[A05 进制转换与数位分解]] — 位置记数法、除基取余、Horner 还原、`std::to_chars`/`std::from_chars`、补码与任意进制。

## 待整理材料

- [[Every Data Structure Simply Explained in 25 Minutes!]] — 常见数据结构速览，尚未成篇。
- [[The Most Ambiguous Concept in Computer Science]] — 概念辨析，尚未成篇。
