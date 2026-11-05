来源：Claude Shannon 1952 年在贝尔实验室内部讲座 *Creative Thinking*（[[Raw/Creative Thinking]]）。核心：创造性研究需要三个条件，而“怎么想”本身也可以拆成几种可练习的思考工具。

## 三个必要条件

Shannon 认为，做科学研究、发明、数学或物理，至少需要三样东西：

1. **训练与经验（training and experience）**：再有天赋的律师，也不可能凭空给出新的物理理论。
2. **智力与才能（intelligence and talent）**：需要高于平均水平的智力；Shannon 说这是遗传/环境的一部分。
3. **动机（motivation）**：这是把普通聪明人变成 Newton、Einstein 的那一项。没有想追问“为什么”的驱动力，训练和智力都发挥不出来。

他把动机拆成几种可观察的倾向：

- **好奇心（curiosity）**：想知道事物怎么运转，看到现象就想提问。
- **建设性的不满足（constructive dissatisfaction）**：不是悲观抱怨，而是“这已经不错，但也许能做得更漂亮、更简单”。
- **对结果本身的快乐**：证出一个定理、设计出一个巧妙电路，会得到很大的满足感。

用他的比喻：如果一个人对答案的渴望强到不在乎是不是下午五点，愿意通宵、愿意牺牲周末，那才更像研究者的动机。

## 大脑的“临界质量”

Shannon 引用 Turing 的比喻：大脑像一块铀。

- 低于临界质量：射入一个中子，产生不到一个新中子，链式反应无法维持；
- 高于临界质量：一个想法进去，能产生不止一个新想法，反应自我放大。

他把这画成一条“ideas in → ideas out”的曲线：

- 曲线低于 \(y=x\)：输入一个想法，只产出半个想法；
- 曲线高于 \(y=x\)：输入一个想法，产出两个甚至更多；
- 交叉点就是所谓的 **knee of the curve**（曲线拐点）。

Shannon 说自己不认为自己超过了这个拐点，也不认识活着的人里谁超过了；但他认为 Newton 显然在曲线很高的位置——25 岁就做出了二项式定理、微积分、万有引力、运动定律、白光分解等足够让十几个人出名的成果。

![[S04_knee_curve.png]]
*想法输入与想法输出的关系：曲线低于 \(y=x\) 时，一个想法进来只能产出不到一个；越过拐点后，想法开始自我放大。*

## 六种思考工具

Shannon 说，好的研究者往往**无意识地**在用这些方法；如果把它们显式化，遇到合适的问题时主动调用，通常能更快找到答案。

### 1. 简化（simplification）

把问题里所有非本质的东西先剥掉，只留下核心。

- 现实问题通常被大量无关数据包裹；
- 简化后可能已经“不像原问题”了，但先把简化版解出来，再逐步加回细节；
- 这比一开始就硬啃完整问题容易得多。

### 2. 寻找相似的已知问题（seeking similar known problems）

如果问题 \(P\) 很难，找一个已经解决过的相似问题 \(P'\)，以及它的解 \(S'\)。然后建立两条类比：

$$
P \longrightarrow P',\qquad S' \longrightarrow S.
$$

也就是：先把新问题映射到旧问题，解完再映射回来。

```mermaid
%%{init: {'theme':'base','themeCSS':'.nodeLabel{color:#E5E7EB!important;fill:#E5E7EB!important}.edgeLabel p{background-color:#131312!important}.edgeLabel{color:#E5E7EB!important}svg{background:transparent!important}','themeVariables':{'primaryColor':'#1E1E2E','primaryTextColor':'#E5E7EB','primaryBorderColor':'#A78BFA','secondaryColor':'#1E1E2E','tertiaryColor':'#1E1E2E','lineColor':'#9CA3AF','textColor':'#E5E7EB','mainBkg':'#1E1E2E','nodeBorder':'#A78BFA','clusterBkg':'#131312','clusterBorder':'#3A3A4A','edgeLabelBackground':'#131312','actorBkg':'#1E1E2E','actorBorder':'#A78BFA','actorTextColor':'#E5E7EB','actorLineColor':'#9CA3AF','signalColor':'#9CA3AF','signalTextColor':'#E5E7EB','labelBoxBkgColor':'#1E1E2E','labelBoxBorderColor':'#A78BFA','labelTextColor':'#E5E7EB','loopTextColor':'#E5E7EB','noteBkgColor':'#1E1E2E','noteBorderColor':'#A78BFA','noteTextColor':'#E5E7EB','stateBkg':'#1E1E2E','stateBorder':'#A78BFA','stateTextColor':'#E5E7EB','transitionColor':'#9CA3AF','transitionLabelColor':'#E5E7EB','fontFamily':'Noto Sans CJK SC, sans-serif','fontSize':'16px'}}}%%
flowchart LR
    P["新问题 P"] -->|"类比"| Pp["已知问题 P'"]
    Pp --> Sp["已知解 S'"]
    Sp -->|"类比映射回来"| S["新解 S"]
classDef default fill:#1E1E2E,stroke:#A78BFA,stroke-width:1.5px,color:#E5E7EB
linkStyle default stroke:#9CA3AF
```

Shannon 说，经验之所以重要，是因为老手脑子里存着成千上万个 \(P'\) 和 \(S'\)，很容易找到一个离当前问题足够近的旧问题。**两次小跳跃，通常比一次大跳跃容易。**

### 3. 换一种说法（restatement）

尽可能用不同形式重述问题：

- 换词；
- 换视角；
- 从多个角度看；
- 最后尝试同时从几个角度看。

目的是打破思维定势（ruts）。有时候一个刚接触问题的新人，反而能一眼看到答案，因为他没有被旧的看法困住。

### 4. 推广（generalization）

一旦解决了一个特殊结果，马上问：

- 能不能从二维推广到 \(n\) 维？
- 能不能从实数域推广到一般代数结构？
- 这个技巧能不能用来解决更大一类问题？

这在数学里尤其强大：先证一个特殊定理，再把它推广成更一般的陈述。

### 5. 结构分析（structural analysis）

如果从问题 \(P\) 到解 \(S\) 的跳跃太大，就把它拆成许多小跳跃：

- 先证明若干辅助命题/子定理；
- 再让这些子结论一步步推向目标；
- 找到解之后，回头删掉多余的步骤，做简化。

很多数学证明其实是“绕远路”找到的：先证明一堆看似无关的结果，最后从后门到达答案；找到之后，往往能把路径缩短。

### 6. 反演（inversion）

如果从前提 \(P\) 推到结论 \(S\) 很难，就假设 \(S\) 是已知条件，反过来求 \(P\)。

- 反向问题有时反而更直接；
- 找到反向路径后，再把步骤逐段反转，得到正向证明；
- 在工程/电路设计里也常用：从“期望的输出”倒推“需要什么输入”。

Shannon 举了自己设计 Nim 游戏机器的例子：正向计算需要大量继电器，很难；把问题反过来，从期望结果倒推输入，用反馈逐步逼近，设计反而简单得多。

![[S04_heuristics.png]]
*左：结构分析把一次大跳跃拆成多个小跳跃；右：反演把“从 P 到 S”的难题换成“从 S 到 P”的路径，再反转回来。*

## 对今天的学习意味着什么

- 创造性不是纯灵感，至少一部分是**可训练的策略**。
- 遇到卡壳时，可以按清单逐项试：能不能简化？有没有相似问题？能不能换个说法？能不能推广？能不能拆成小步？能不能反过来？
- 这些工具和“刻意练习”结合，就是把“想不出来”变成“有方向地试”。

## 词汇


- **influential** 有影响力的
- **proportion** 比例；部分
- **neutron** 中子
- **explosive** 爆炸性的；激增的
- **egotistical** 自负的；自我中心的
- **heredity** 遗传
- **temperament** 气质；性情
- **curiosity** 好奇心
- **dissatisfaction** 不满足；不满
- **constructive** 建设性的
- **irritation** 恼怒；刺激
- **gimmick** 花招；小技巧
- **catalogue** 编目；分类记录
- **extraneous** 无关的；外来的
- **refinement** 改进；精细化的部分
- **viewpoint** 观点；视角
- **rut** 车辙；思维定势
- **subsidiary** 辅助的；附属的
- **inversion** 反演；倒置
- **feedback** 反馈
- **axiom** 公理
- **theorem** 定理
- **roundabout** 绕远的；迂回的
- **insight** 洞察；洞见
