---
tags:
  - 语法知识
  - CMake语法
---

# CMake 注释是 # · 语法知识 · N005

**时间:** 2026-10-03（原记录未记时分）
**标签:** #语法知识 #CMake语法
**关联:** [[E001 构建依赖-找不到rclcpp]]

## 疑惑点

在 CMakeLists 里用 `//` 写注释，为什么会报 `Parse error ... "//"`？

## 实际情况

1. CMake 的注释符号是 `#`（`//` 是 C/C++ 的注释，CMake 不认）。
2. 写 `find_package(rclcpp REQUIRED) // 注释` 会报 `Parse error`。
3. 正确写法：`find_package(rclcpp REQUIRED)  # 注释`。

> **Note（连接 / 深化）：**
> - 连接：CMakeLists 的错误常和依赖配置相关，见 [[E001 构建依赖-找不到rclcpp]]。
> - 深化：注意区分各文件的注释符号——CMake/`package.xml` 用 `#`（XML 里是 `<!-- -->`），C/C++ 用 `//` 或 `/* */`。

## 思考

（留白 —— 留意 CMake 文件里 `#` 和 C++ 文件里 `//` 的区别）

## 总结

**本质：** CMake 用 `#` 注释，`//` 在 CMake 里不是注释符号，混用会导致 Parse error。
**标签:** #语法知识 #CMake语法
