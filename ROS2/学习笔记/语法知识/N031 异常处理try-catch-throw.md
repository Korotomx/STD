异常处理把「检测到错误」和「处理错误」分开：`throw` 报告错误，`try` 圈出可能出错的代码，`catch` 决定怎么办。`throw` 后沿调用栈向上找匹配的 catch，沿途 RAII 保证局部对象正确析构。

## 语法与流程

```cpp
try {
  throw std::runtime_error("出错了");   // 立即跳出 try，后面的代码不执行
}
catch (const std::exception & e) {
  std::cerr << e.what() << '\n';
}
// 正常和出错两种情况都会走到这里
```

- 正常：try 跑完，跳过 catch，继续往下。
- 出错：跳到匹配的 catch，处理完继续往下。

## 异常类型

`std::exception` 是所有标准异常的基类：

| 类型 | 含义 |
|---|---|
| `std::exception` | 基类，兜底 |
| `std::runtime_error` | 运行时错误 |
| `std::out_of_range` | 越界 |
| `std::invalid_argument` | 参数非法 |
| `std::logic_error` | 逻辑错误 |

`e.what()` 返回描述（`const char*`）。

多个 catch 时**具体类型在前、基类在后**，否则基类先匹配，后面的具体 catch 永远轮不到。`catch (...)` 捕获一切但拿不到对象：

```cpp
catch (const std::out_of_range & e) { ... }
catch (const std::exception & e)     { ... }
catch (...)                          { ... }
```

## 栈展开

`throw` 后程序沿调用栈逐层向上找最近的 catch，沿途局部对象自动析构（RAII，不泄漏）。一直没人接 → 传播到 `main` → `std::terminate()` → 程序崩溃。

## ROS 2 里的用法

`fut.get()` 可能抛异常（异步任务失败、future 状态不对）。回调里抛异常没人接会导致节点终止，所以包住它、记日志、让节点继续活：

```cpp
try {
  auto results = fut.get();
  // 正常处理
}
catch (const std::exception & e) {
  RCLCPP_ERROR(this->get_logger(), "设置背景色异常: %s", e.what());
}
```

异常安全依赖 RAII；ROS 2 里句柄都用 `SharedPtr`，即使异常跳过某段代码，资源也不会泄漏。

## 坑

- catch 按值捕获会切片，且多一次拷贝；用 `const &`。
- catch 顺序写反（基类在前）会让具体处理失效。
- 析构函数里不要抛异常，否则栈展开中再次抛出会 terminate。
- 不要用异常做正常控制流。

> PS：工程上在节点边界统一 catch，内部逻辑尽量不吞异常；错误码适合可预期的失败，异常适合「不该发生但发生了」。

throw 报告、try 圈范围、catch 处理；栈展开 + RAII 保证资源释放；ROS 2 里用来兜住异步 `get()` 等可能抛错的操作。