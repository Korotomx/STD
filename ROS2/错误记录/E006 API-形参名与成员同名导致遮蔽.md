---
tags:
  - API
  - C++语法
  - 形参实参
  - 遮蔽Shadowing
---

# E006 · API — 形参名与成员同名导致遮蔽

**日期:** 2026-10-14
**标签:** #API #C++语法 #形参实参 #遮蔽Shadowing

## 问题

写 `publish_cmd_vel` 时形参用了 `m_v` / `m_w`——和类的成员变量同名。代码能编译，但「函数里用的 `m_v`」到底是成员还是形参分不清，语义混乱，还破坏了 `m_` 前缀「成员专属」的可读性。

## 原因

C++ 里**形参优先**：函数体内 `m_v` 指向形参（局部），成员 `m_v` 被「遮蔽（shadowing）」。名字撞了之后，读代码的人会误以为在操作成员，实际操作的是形参。

## 解决方案

形参别用 `m_` 前缀，用普通名（`linear` / `angular` / `v`）；`m_` 前缀只留给成员。一眼分清「这个变量是谁的」：

```cpp
// 改前：形参名撞成员名，遮蔽
void publish_cmd_vel(rclcpp::Rate & rate, double duration, double m_v, double m_w)

// 改后：形参用普通名
void publish_cmd_vel(rclcpp::Rate & rate, double duration, double linear, double angular)
```

## 参数注意事项（写函数参数时的坑）

1. **形参名别和成员撞**：撞了会被遮蔽，还破坏 `m_` 前缀可读性。
2. **固定值别当参数传**：固定速度写死 `constexpr`（[[N048 constexpr编译期常量]]），参数只留给「每次会变」的量。
3. **按值传的形参是拷贝**：函数里改它，外面实参 / 成员不变——别指望改形参去改成员。
4. **不可拷贝对象只能传引用**：`rclcpp::Rate` 不可拷贝，必须 `rclcpp::Rate & rate`（[[N038 stdthread线程库与ROS2应用]]）。
5. **传值 vs 传引用**：`double v`（拷贝）、`double & v`（改原值）、`const double & v`（大对象只读、避免拷贝）。

> **Note（关联）：** 形参 = 占位名、实参 = 实际值，调用时实参拷进形参；成员 / 局部概念见 [[N040 实例instance是什么]]。
