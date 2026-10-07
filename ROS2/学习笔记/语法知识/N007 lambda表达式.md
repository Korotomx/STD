---
tags:
  - 语法知识
  - C++语法
  - lambda表达式
---

# lambda 表达式 · 语法知识 · N007

**时间:** 2026-10-03（原记录未记时分，2026-10-06 深化）
**标签:** #语法知识 #C++语法 #lambda表达式
**关联:** [[N006 stdbind与回调]] · [[N001 节点基础书写骨架]] · [[N029 turtle_painter参数中转节点拆解]] · [[N030 future机制异步结果的凭证]]

## 疑惑点

lambda 表达式到底怎么写？各种捕获列表 `[]`、`[this]`、`[=]`、`[&]` 分别是什么意思？

## 实际情况

lambda 是 C++11 的「匿名函数」，可替代 `std::bind`，写法更直观：

```cpp
// bind 写法（老）
std::bind(&Talker::timer_callback, this)

// lambda 写法（等价）
[this]() { this->timer_callback(); }
```

**完整语法：**

```cpp
[捕获列表](参数列表) -> 返回类型 { 函数体 }
```

- `-> 返回类型` 可省略，编译器自动推导。

**捕获列表常见形式：**

| 写法 | 含义 |
|------|------|
| `[]` | 不捕获任何外部变量 |
| `[this]` | 捕获 this，可访问成员 |
| `[=]` | 按值捕获所有用到的变量（拷贝）|
| `[&]` | 按引用捕获所有用到的变量 |
| `[x]` | 按值捕获变量 x |
| `[&x]` | 按引用捕获变量 x |

### 深化：lambda 作为回调（结合 turtle_painter）

**① lambda 整体就是「那个函数」，不是「多写了个函数」**

```cpp
timer_ = this->create_wall_timer(2s, [this]() {
  apply_color();
  timer_->cancel();
});
```

`create_wall_timer` 的第二个参数要一个「回调函数」，整个 `[this](){...}` 就是这个回调——它是**即写即用的匿名函数**，被传进去，到点后由 ROS 调用。

**② `[this]` 是「捕获」不是「返回」**

`[this]` 的意思是「把当前对象的 this 借进函数体」，于是函数体里能直接写 `apply_color()`、`timer_`（它们其实是 `this->apply_color()`、`this->timer_`）。没有 `[this]`，函数体就用不了这些成员。

它等价于写了一个成员函数：

```cpp
// [this]() { apply_color(); timer_->cancel(); }
//   等价于 ↓
void 某函数名() { this->apply_color(); this->timer_->cancel(); }
```

**③ lambda 也能带参数：参数由「调用方」塞进来**

```cpp
param_client_->set_parameters({...},
  [this](std::shared_future<...> fut) {   // 有参数 fut
    auto results = fut.get();
  });
```

- 定时器回调是 `[this]()`（无参）；异步回调是 `[this](fut)`（有参）——**参数不是你自己填的，是 ROS 在调用回调时塞给你的**；
- 这里的 `fut` 就是 [[N030 future机制异步结果的凭证]] 里的「取餐号」。

> **Note（连接 / 深化）：**
> - 连接：lambda 与 `std::bind` 等价，见 [[N006 stdbind与回调]]；作为回调贯穿 [[N029 turtle_painter参数中转节点拆解]]。
> - 深化：`[=]` 拷贝捕获、`[&]` 引用捕获的差异；`[this]` 是「借 this 进函数体」而非「返回 this」；回调的「参数」由调用方（ROS）在触发时传入。

## 思考

（留白 —— 把 listener.cpp 里的 std::bind 改成 lambda，试试用 [this]）

## 总结

**本质：** lambda = 「匿名函数」，由 `[捕获](参数) -> 返回类型 { 体 }` 组成；捕获列表决定外部变量如何进入函数体，可替代 `std::bind` 直接作为回调。
**标签:** #语法知识 #C++语法 #lambda表达式
