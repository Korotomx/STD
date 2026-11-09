有限状态机把「已经收到什么」记成一个状态，用带标签的有向边表示下一个输入如何改变状态。

## 探针：正则语义

> [!question] (AB)* 定义的语言是下面哪一个集合？
> - A：至少一个 AB，以及任意多个 AB 串联成的串
> - B：A 和 B 任意排列组成的串
> - C：空串，以及任意多个 AB 串联成的串
> - D：我不知道

> [!failure] ✗ 不对
> 正解是 C。`*` 是「重复 0 次或多次」，0 次就是空串，所以空串必须在语言里。A 描述的是 `+`——「重复 1 次或多次」。两者只差空串这一个元素。

> [!question] 下面哪个串属于 A* 但不属于 A+？
> - A：A
> - B：空串
> - C：AA
> - D：我不知道

> [!success] ✓ 正确
> `A*` 允许 0 次重复，`A+` 不允许，所以唯一的差集就是空串。

> [!question] (A|B)* 定义的语言是下面哪一个集合？
> - A：只由 A 和 B 交替组成的串，包括空串
> - B：单个 A 或单个 B，以及空串
> - C：由 A、B 组成的任意串，包括空串
> - D：我不知道

> [!failure] ✗ 不对
> 正解是 C。`(A|B)` 每一步都可以重新选，前一步选了什么不影响下一步，所以 AAB、ABBA 都合法。交替是额外约束，要靠「记住上一位」实现——状态机要多带信息。

> [!question] 下面哪个串属于 A(BC)*？
> - A：ACB
> - B：ABC
> - C：ABCB
> - D：我不知道

> [!success] ✓ 正确
> `A(BC)*` 只允许 A 后面跟若干个完整的 BC 块；ACB 少了 B，ABCB 末尾多了一个 B。

> [!question] (A|B)* 与 (A*B*)* 定义的语言相同吗？
> - A：不相同，后者少了某些串
> - B：不相同，后者多了某些串
> - C：相同
> - D：我不知道

> [!failure] ✗ 不对
> 正解是 C。`(A*B*)*` 的每一轮都可以重新先读 A 再读 B，所以 ABAB 可以拆成 (AB)(AB)。两个表达式生成的是同一个语言：{A, B} 上所有串。你选的 A 相当于认为「只能经历一次 A→B」——但外层 `*` 允许反复进入 A*。

> [!question] 逐位读入一个二进制串，要判断 1 的个数是奇数还是偶数，最少需要几个状态？
> - A：1
> - B：2
> - C：4
> - D：我不知道

> [!success] ✓ 正确
> 只需要「奇数」「偶数」两个状态：读入 0 状态不变，读入 1 在两个状态间翻转。状态数由「需要记住的历史有多少种」决定，不由历史长度决定。

## 1. 状态：把历史压成有限种情况

判定一个串是否属于某个语言，要求只从左到右读一遍、内存有限——不可能把整条历史都记住，只能压缩。

- 压缩的判据：两个不同的历史，只要**对之后任何输入的处理结果都相同**，就没有理由分开，可以合并成一个状态。
- 这就是状态机的核心约束：下一状态只由 $\delta(\text{当前状态},\ \text{当前输入})$ 决定，过去的影响全部藏在当前状态里。
- 奇偶例子：前缀 `101` 和 `1` 都含奇数个 1，之后无论接什么，最终奇偶都一致——它们是同一个状态。历史条数无限，状态数只要 2。

> [!success] ✓ 正确
> 合并的判据只看未来：对任意后续输入，两个历史的接受结果必须完全一致。长度、1 的个数都只是表面特征，不构成合并的理由。

## 2. 五元组与图表示

把「状态 + 输入决定下一步」写成可计算的对象，只需要五样东西：

$$
M = (Q,\ \Sigma,\ \delta,\ q_0,\ F)
$$

- $Q$：有限状态集合
- $\Sigma$：输入字母表
- $\delta: Q \times \Sigma \to Q$：转移函数，给「当前状态 + 当前输入」返回下一状态
- $q_0 \in Q$：初态，只有一个
- $F \subseteq Q$：终态集合，可以多个，也可以是空集

图的画法：顶点是状态，边是转移、标签是输入符号；初态用一根没有起点的入箭头标出，终态画双圈。

**接受的定义**：读完整条输入串后，停在 $F$ 里的状态就接受，否则拒绝。注意判据是「读完时的状态」，不是「途中经过过终态」。

> [!success] ✓ 正确
> 空串读完不需要任何转移，停在 $q_0$；既然 $q_0 \in F$，空串就被接受。除此之外还可能接受别的串（比如自环回 $q_0$ 的那些），所以是「至少」。

## 3. 正则的基本形式 → 机器

正则描述一组串，机器判定一个串是否属于这组串。Kleene 的构造是：先给每个算子一台最小机器，再按表达式结构拼装。

| 正则 | 机器 |
|---|---|
| $\varepsilon$ | 一个状态，既是初态也是终态 |
| $a$ | 初态 $\xrightarrow{a}$ 终态 |
| $RS$ | 把 $R$ 的终态接到 $S$ 的初态 |
| $R \mid S$ | 初态分出两条路，分别走 $R$、$S$ |
| $R^*$ | 初态同时是终态；终态加一条回初态的边 |
| $R^+$ | 同星号，但初态**不是**终态 |

### 六种基本构造的图

```mermaid
%%{init: {'theme':'base','themeCSS':'.nodeLabel{color:#E5E7EB!important;fill:#E5E7EB!important}.edgeLabel p{background-color:#131312!important}.edgeLabel{color:#E5E7EB!important}svg{background:transparent!important}','themeVariables':{'primaryColor':'#1E1E2E','primaryTextColor':'#E5E7EB','primaryBorderColor':'#A78BFA','lineColor':'#9CA3AF','mainBkg':'#1E1E2E','nodeBorder':'#A78BFA','clusterBkg':'#131312','clusterBorder':'#3A3A4A','edgeLabelBackground':'#131312','noteBkgColor':'#1E1E2E','noteBorderColor':'#A78BFA','stateBkg':'#1E1E2E','stateBorder':'#A78BFA','fontFamily':'Noto Sans CJK SC, sans-serif'}}}%%
graph LR
  subgraph E[空串 ε]
    e0(((e0 初·终)))
  end
  subgraph C[单字符 a]
    a0((a0 初)) -->|a| a1(((a1 终)))
  end
  subgraph CAT[串联：以 AB 为例]
    c0((c0 初)) -->|A| c1((c1)) -->|B| c2(((c2 终)))
  end
  subgraph UNI[并：以 A 或 B 为例]
    u0((u0 初)) -->|A| u1(((u1 终)))
    u0 -->|B| u2(((u2 终)))
  end
  subgraph STAR[星：以 A* 为例]
    s0(((s0 初·终))) -->|A| s0
  end
  subgraph PLUS[加：以 A+ 为例]
    p0((p0 初)) -->|A| p1(((p1 终)))
    p1 -->|A| p1
  end
  e0 ~~~ a0 ~~~ c0 ~~~ u0 ~~~ s0 ~~~ p0
classDef default fill:#1E1E2E,stroke:#A78BFA,stroke-width:1.5px,color:#E5E7EB
linkStyle default stroke:#9CA3AF
```

星号和加号的机器只差一处：初态是不是终态。回边负责「重复」，初态是否终态负责「零次」。这也解释了探针第一题：`(AB)*` 的空串来自「一步都不走就停在初态」。

> [!success] ✓ 正确
> 回边提供重复，初态不在 $F$ 保证至少走一次。两者合起来就是「一个或更多」。

## 4. 复合正则：外层星是「回到入口」

探针里把 `(A*B*)*` 读成「只能走一遍 A→B」，问题出在外层 `*` 的机器长什么样。

- 内层 `A*B*`：$q_0$ 接受若干 A，$q_0 \xrightarrow{B} q_1$ 接受若干 B；$q_0$、$q_1$ 都是终态（B 可以是 0 个）。
- 外层 `*`：在每个终态上加一条回到 $q_0$ 的边。于是每读完一轮，机器可以回到 $q_0$——**A 又被允许了**。
- 读 `ABAB`：$q_0 \xrightarrow{A} q_0 \xrightarrow{B} q_1$，经回边回到 $q_0$，再 A、再 B。所以 ABAB 属于。
- 两边相等：每个 $A^*B^*$ 块都是 $\{A,B\}$ 上的串，拼起来仍在 $(A|B)^*$ 里；反过来任何 $\{A,B\}$ 串都能按 A 段 / B 段切开，每段正好是 $A^*B^*$ 的一轮。两个表达式都等于 $\Sigma^*$。

一般原则：**星号不是「重复同一段」，而是「随时可以回到这台子机器的入口」**。

### 四台机器

```mermaid
%%{init: {'theme':'base','themeCSS':'.nodeLabel{color:#E5E7EB!important;fill:#E5E7EB!important}.edgeLabel p{background-color:#131312!important}.edgeLabel{color:#E5E7EB!important}svg{background:transparent!important}','themeVariables':{'primaryColor':'#1E1E2E','primaryTextColor':'#E5E7EB','primaryBorderColor':'#A78BFA','lineColor':'#9CA3AF','mainBkg':'#1E1E2E','nodeBorder':'#A78BFA','clusterBkg':'#131312','clusterBorder':'#3A3A4A','edgeLabelBackground':'#131312','noteBkgColor':'#1E1E2E','noteBorderColor':'#A78BFA','stateBkg':'#1E1E2E','stateBorder':'#A78BFA','fontFamily':'Noto Sans CJK SC, sans-serif'}}}%%
graph LR
  subgraph M1["(AB)*"]
    a0(((q0 初·终))) -->|A| a1((q1))
    a1 -->|B| a0
  end
  subgraph M2["(A|B)*"]
    b0(((q0 初·终)))
    b0 -->|A| b0
    b0 -->|B| b0
  end
  subgraph M3["(A*B*)*"]
    c0(((q0 初·终)))
    c0 -->|A| c0
    c0 -->|B| c1(((q1 终)))
    c1 -->|B| c1
    c1 -->|A| c0
  end
  subgraph M4["(AB|BA)*"]
    d0(((q0 初·终)))
    d0 -->|A| dA((qA))
    d0 -->|B| dB((qB))
    dA -->|B| d0
    dB -->|A| d0
  end
  a0 ~~~ b0 ~~~ c0 ~~~ d0
classDef default fill:#1E1E2E,stroke:#A78BFA,stroke-width:1.5px,color:#E5E7EB
linkStyle default stroke:#9CA3AF
```

- `(AB)*`：每轮必须 A 后跟 B；空串合法。
- `(A|B)*`：一个状态，A、B 都是自环，所以是任意串。
- `(A*B*)*`：`q0` 收 A 段，`q0 --B--> q1` 收 B 段；`q1 --A--> q0` 就是外层星的「回到入口」，A 又重新被允许。
- `(AB|BA)*`：`qA` 是「已看到 A，等 B」，`qB` 是「已看到 B，等 A」。

读 `ABBA`：

- `(AB|BA)*`：`q0 -A→ qA -B→ q0 -B→ qB -A→ q0`，最后停在终态，属于。
- `(A*B*)*`：`q0 -A→ q0 -B→ q1 -B→ q1 -A→ q0`，回到终态，属于。
- `(AB)*`：`q0 -A→ q1 -B→ q0`，第二个 `B` 在 `q0` 没有出边，卡死——不属于。

> [!question] 在 `(A*B*)*` 的机器上逐位读 `ABBA`，最后停在哪个状态？
> - A：q1
> - B：q0
> - C：中途卡死
> - D：我不知道

> [!success] ✓ 正确
> A 段停在 `q0`，`B` 到 `q1`，第二个 `B` 自环留在 `q1`，最后的 `A` 走 `q1 --A--> q0` 回入口。停在 `q0`，是终态——这条回边就是外层星。

## 5. 转移表与确定性

状态图给人看，转移表给机器算。行是状态，列是输入符号，格子里写 $\delta(q,a)$。以 `(A*B*)*` 为例：

| $\delta$ | $A$ | $B$ |
|---|---|---|
| $q_0$（初·终） | $q_0$ | $q_1$ |
| $q_1$（终） | $q_0$ | $q_1$ |

**确定性**：每个「状态 × 符号」的格子**恰好一个**状态——不能空，也不能写两个。

- 图上的表现：同一状态出发、同一标签只有一条边。
- 两条同标签出边 → 非确定（NFA）；一条都没有 → 不完整。拒绝靠「读完停在非终态」，不靠「查不到表」。
- 确定性的好处：执行就是查表循环，读一位查一次，不需要记住备选路径，也不需要回溯。

术语：**DFA** = deterministic finite automaton，确定有限自动机，就是上面这种「每个格子恰好一个状态」的机器；**NFA** = nondeterministic finite automaton，非确定有限自动机，允许同一状态同一符号有多个目标，或允许 $\varepsilon$ 边（不读输入也能跳）。
