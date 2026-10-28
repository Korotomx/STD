`constexpr` 是编译期常量：值在编译时就确定，编译后直接嵌进使用处，不占运行期变量。写死的速度、阈值、π 用它最合适。

## const vs constexpr

| | `const` | `constexpr` |
|---|---|---|
| 含义 | 运行期不可变 | 编译期可求值 |
| 值何时确定 | 可以到运行期 | 必须编译期算出来 |
| 关系 | —— | constexpr 隐式是 const |

```cpp
const     int a = read_number();   // ✅ 运行期确定，之后不可改
constexpr int b = read_number();   // ❌ 编译期算不出，报错
constexpr int c = 2 * 3;           // ✅ 编译期算出 6
```

`const` 管「之后不许改」，`constexpr` 管「编译时就能算」。

## 为什么不用 #define

| | `constexpr` | `#define` |
|---|---|---|
| 类型检查 | 有 | 无，纯文本替换 |
| 作用域 | 有 | 无，全局污染 |
| 调试可见 | 有符号名 | 替换后符号消失 |

## 修饰函数

编译期能算的就在编译期算：

```cpp
constexpr double square(double x) { return x * x; }
constexpr double area = square(2.0);   // 编译期算成 4.0
```

## 在画圆代码里

```cpp
constexpr double kV = 2.0;
constexpr double kW = 2.0;

msg.linear.x  = kV;    // 编译后等价于 2.0，零运行时开销
msg.angular.z = kW;
```

## 与参数的分工

固定不变 → `constexpr`；要运行时 `--ros-args -p` 覆盖 → `declare_parameter`，见 [[N024 参数概念与四大通信机制全景]]。这是「写死 vs 可配置」的取舍。

## 坑

- `constexpr` 变量的初始值必须编译期可求值，不能用运行期输入。
- 数组大小、模板参数这类必须在编译期知道值的地方，是 constexpr 的硬需求。
- `constexpr` 函数在运行期调用也合法，只是失去编译期求值。

> PS：C++20 起 `constexpr` 可用于更多场景（虚函数、动态分配），但常用范围仍是常量表达式。

constexpr = 编译期常量，比 const 更强（必须编译期可算）、比 #define 更安全（有类型与作用域）；固定值用它，可配置值用参数。