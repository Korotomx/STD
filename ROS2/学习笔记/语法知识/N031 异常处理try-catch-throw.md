---
tags:
  - 语法知识
  - C++语法
  - 异常Exception
  - 错误处理
---

# 异常处理 try / catch / throw · 语法知识 · N031

**时间:** 2026-10-06 22:07
**标签:** #语法知识 #C++语法 #异常Exception #错误处理
**关联:** [[N030 future机制异步结果的凭证]] [[N029 turtle_painter参数中转节点拆解]] [[N007 lambda表达式]]

## 疑惑点

`try / catch` 是干嘛的？`throw` 是什么？为什么 `turtle_painter` 里 `fut.get()` 外面要包一层 try/catch？

## 实际情况

### 一、为什么需要异常处理

程序运行时会出各种错（除零、越界、`fut.get()` 时任务已失败……）。若不管，错误要么让程序崩溃，要么带着错误值继续跑（更糟）。异常处理把「**检测到错误**」和「**处理错误**」分开：

- **throw 的地方**只负责报告「这里出错了」；
- **catch 的地方**负责决定「出错后怎么办」。

### 二、三个关键字

| 关键字 | 作用 |
|---|---|
| `throw` | **抛出**异常（报告错误，抛一个异常对象） |
| `try` | 圈出「**可能出错**」的代码块 |
| `catch` | **捕获**并处理异常 |

### 三、语法结构与执行流程

```cpp
try {
  // 可能出错的代码
  throw std::runtime_error("出错了");   // 一旦执行到 throw，立刻跳出 try 块
  // ... 这后面的代码不会再执行
}
catch (const std::exception & e) {
  // 出错后跳到这里处理
  std::cerr << e.what() << '\n';
}
// try-catch 之后：两种情况都会走到这里
```

- **正常时**：try 块跑完，跳过 catch，继续往下；
- **出错时**：try 块里某处 `throw` → 立刻跳出 try 剩余部分 → 跳进匹配的 catch → 处理完继续往下。

### 四、异常类型（一个继承体系）

`std::exception` 是所有标准异常的**基类**，常见子类：

| 类型 | 含义 |
|---|---|
| `std::exception` | 基类（兜底捕获） |
| `std::runtime_error` | 运行时错误 |
| `std::out_of_range` | 越界访问 |
| `std::invalid_argument` | 参数非法 |
| `std::logic_error` | 逻辑错误 |

`e.what()` 返回异常的描述（`const char*`），常用来打印。

### 五、多个 catch 与 catch(...)

```cpp
try { ... }
catch (const std::out_of_range & e) { ... }   // 先捕获「具体」类型
catch (const std::exception & e)     { ... }   // 再捕获「基类」兜底
catch (...)                          { ... }   // 捕获一切（拿不到异常对象）
```

> 顺序很关键：**具体类型在前、基类在后**。若基类在前，会先匹配走，后面的具体 catch 永远轮不到。

### 六、栈展开（throw 之后发生了什么）

`throw` 后程序沿**调用栈逐层向上**找最近的匹配 `catch`，沿途**正确析构局部对象**（RAII，不会泄漏）。一直没人 catch → 传播到 `main` 都没有 → `std::terminate()` → 程序崩溃。

### 七、回到 ROS2：为什么 `fut.get()` 要包 try/catch

`fut.get()` 可能抛异常（异步任务内部失败、future 状态不对）。若在回调里抛异常又没人接，可能导致节点异常终止。所以包住它，出错时**记日志、让节点继续活着**：

```cpp
try {
  auto results = fut.get();          // 可能抛异常
  // ... 正常处理
}
catch (const std::exception & e) {
  RCLCPP_ERROR(this->get_logger(), "设置背景色异常: %s", e.what());  // 记日志,不崩
}
```

> **Note（连接 / 深化）：**
> - 连接：这里 try/catch 保护的是 [[N030 future机制异步结果的凭证]] 里的 `fut.get()`——异步取结果可能失败，用异常机制兜底。
> - 深化：异常安全依赖 **RAII**（栈展开时局部对象自动析构），这也是为什么 ROS2 里句柄都用 `SharedPtr`（智能指针）——即使异常跳过某段代码，资源也不会泄漏。

## 思考

（留白 —— `throw` 一个异常对象后，try 块里 `throw` 之后的代码都不执行了；那如果那段代码里有需要「善后」的资源（已打开的文件、已 new 的内存），靠什么保证它被正确释放？）

## 总结

**本质：** `throw` 报告错误、`try` 圈出可能出错的代码、`catch` 处理错误；出错时立即跳出 try 块跳到匹配的 catch，沿途 RAII 保证资源不泄漏；ROS2 里用 try/catch 包住 `fut.get()` 等可能抛异常的操作，出错记日志、节点不崩。
**标签:** #语法知识 #C++语法 #异常Exception #错误处理
