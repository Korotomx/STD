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
