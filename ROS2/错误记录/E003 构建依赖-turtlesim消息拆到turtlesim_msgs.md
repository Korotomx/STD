---
tags:
  - 构建
  - 依赖
  - turtlesim
  - turtlesim_msgs
  - lyrical
---

# E003 · 构建/依赖 — turtlesim 消息类型拆到了 turtlesim_msgs

**日期:** 2026-10-05
**标签:** #构建 #依赖 #turtlesim #turtlesim_msgs #lyrical

## 问题

编写 turtle_chase 时 `#include "turtlesim/msg/pose.hpp"` 报错：

```
fatal error: turtlesim/msg/pose.hpp: No such file or directory
```

## 原因

Lyrical 把 turtlesim 拆成了两个包：
- `turtlesim` —— 应用（跑 turtlesim_node），**不导出任何消息**
- `turtlesim_msgs` —— 消息接口（Pose / Color / Spawn / TeleportAbsolute / Kill / SetPen / RotateAbsolute）

消息类型在 `turtlesim_msgs` 里，不在 `turtlesim` 里。`find_package(turtlesim)` 拿不到 `${turtlesim_TARGETS}`（它的 `turtlesimConfig.cmake` 里 `_extras` 为空）。

## 解决方案

1. 头文件与类型：`#include "turtlesim_msgs/msg/pose.hpp"`，类型 `turtlesim_msgs::msg::Pose`
2. `package.xml`：`<depend>turtlesim_msgs</depend>`
3. `CMakeLists.txt`：`find_package(turtlesim_msgs REQUIRED)` + 链接 `${turtlesim_msgs_TARGETS}`

> **Note（关联）：** 接口包与应用包分离，见 [[N012 ROS2的库与职责]]；消息是接口（.msg/.srv），应用包不导出消息。
