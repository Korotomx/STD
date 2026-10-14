---
tags:
  - API
  - C++语法
  - auto
  - 成员变量
---

# E007 · API — 非静态成员变量不能用 auto 推断类型

**日期:** 2026-10-14
**标签:** #API #C++语法 #auto #成员变量

## 问题

`colcon build` 编译报错：

```
error: non-static data member declared with placeholder 'auto'
```

代码里这样写成员变量：

```cpp
auto m_period = 500ms;   // ❌ 非静态成员不能用 auto
```

## 原因

C++ 规定 **`auto` 类型占位符不能用于非静态成员变量**。非静态成员属于「类里声明、构造时才初始化」，编译器在声明处没有初始值可推断；`auto` 只能用在「声明处直接带初始化器」的地方——局部变量、`static` 成员、函数返回类型等。

**潜伏原因：** 这段代码放在一个「不是包」的目录（`project0`，无 CMakeLists/package.xml）里，从没被 `colcon build` 编译过，所以一直没爆；一搬进能编译的包就现形。

## 解决方案

给成员显式类型，`500ms` 字面量照旧保留：

```cpp
std::chrono::milliseconds m_period = 500ms;   // ✅
```

> **Note（关联）：** 固定值成员的正解是「显式类型 / `constexpr`」，不是 `auto`；见 [[N048 constexpr编译期常量]]。

## 补充：auto 的正解用法（局部变量）

反过来想，`auto` 到底该用在哪？——**局部变量**（它最常见的用法，不是「只能用在 static」）：

```cpp
// chaser_turtle.cpp 的回调里
auto response = future.get();   // ✅ 局部变量，auto 合法
```

- `response` 是**局部变量**（声明在 lambda 的 `{}` 函数体里，每次回调在栈上创建），**不是成员、更不是静态对象**。
- 它带初始化器 `future.get()`，类型能从初始化器推断，所以 `auto` 完全合法。
- 完整类型是 `turtle_chase::srv::GetTargetPose::Response::SharedPtr`（= `std::shared_ptr<turtle_chase::srv::GetTargetPose::Response>`），三段限定名 + 智能指针，太长，用 `auto` 更省事。

**一句话记规则**：`auto` 能不能用，只看「声明处有没有初始化器可推断」——
- ✅ 局部变量（带 `=` 初始化）、`static` 成员、函数返回类型
- ❌ 非静态成员（类里只有声明、没有初始值，没法推断）

「非静态成员不能用 auto」只是这条规则的**一个特例**，别理解成「auto 只能用在 static」。
