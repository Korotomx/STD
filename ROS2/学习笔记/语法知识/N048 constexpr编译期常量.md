---
tags:
  - 语法知识
  - C++语法
  - 常量Constant
  - 编译期CompileTime
---

# constexpr 编译期常量 · 语法知识 · N048

**时间:** 2026-10-13 13:45
**标签:** #语法知识 #C++语法 #常量Constant #编译期CompileTime
**关联:** [[N025 参数的声明读写与命令行工具]] [[N041 栈和堆的底层实现与区别]]

## 疑惑点

画圆 / 画方节点要把「固定速度」写死，为什么用 `constexpr double v = 2.0;` 而不是直接 `double v = 2.0;`？它和 `const`、`#define` 又有什么区别？

## 实际情况

### 1. 是什么

`constexpr` = **编译期常量**。值在**编译时**就确定，编译后直接嵌进使用处，不占运行期变量。适合「写死就再也不变的量」——比如画圆固定的线速度 v、角速度 w：

```cpp
constexpr double v = 2.0;   // 编译期就定死，运行期不可改
```

### 2. const vs constexpr（最容易混）

| | `const` | `constexpr` |
|---|---|---|
| 含义 | 运行期「不可变」 | 编译期「可求值」 |
| 值何时确定 | 可以到运行期才知道 | 必须在编译期算出来 |
| 谁包含谁 | —— | constexpr 隐式是 const |

```cpp
const     int a = read_number();  // ✅ 运行期才确定，但之后不可改
constexpr int b = read_number();  // ❌ 编译期算不出 read_number()，报错
constexpr int c = 2 * 3;          // ✅ 编译期直接算出 6
```

一句话：`const` 管「之后不许改」，`constexpr` 管「编译时就能算」。constexpr 更强。

### 3. 为什么不用 #define

写死常量，老习惯是 `#define V 2.0`，但它是**纯文本替换**，三个毛病：

| | `constexpr` | `#define` |
|---|---|---|
| 类型检查 | 有（是 double） | 无（文本替换，类型不明确） |
| 作用域 | 有（能限定在类 / 命名空间里） | 无（全局污染） |
| 调试可见 | 是（带符号名） | 否（替换后符号消失） |

### 4. 还能用在函数上

`constexpr` 不只能修饰变量，还能修饰函数——编译期能算的就在编译期算：

```cpp
constexpr double square(double x) { return x * x; }
constexpr double area = square(2.0);   // 编译期直接算成 4.0
```

### 5. 回到画圆代码

```cpp
constexpr double v = 2.0;   // 线速度
constexpr double w = 2.0;   // 角速度
// ...
msg.linear.x = v;           // 编译后等价于 msg.linear.x = 2.0，零运行时开销
```

用 `constexpr` 表达「这是固定常量、不是会变的变量」，语义清晰，要改也只改顶部一处。

> **Note（连接 / 深化）：**
> - 连接：固定值用 constexpr；要运行时 `--ros-args -p` 覆盖才用 `declare_parameter`（见 [[N025 参数的声明读写与命令行工具]]）。两者是「写死 vs 可配置」的取舍。
> - 深化：数组大小 `int arr[N]`、模板参数这类**必须在编译期知道值**的地方，是 constexpr 的硬需求。

## 思考

（留白 —— `constexpr` 变量能指向运行期才知道的地址吗？为什么？）

## 总结

**本质：** `constexpr` 是「编译期常量」——值编译时定死、运行期不可改；比 `#define` 有类型 / 作用域，比 `const` 更进一步（值必须编译期可求值）。写死固定速度这类「永远不变的量」用它最合适，语义清晰、零运行时开销。
**标签:** #语法知识 #C++语法 #常量Constant #编译期CompileTime
