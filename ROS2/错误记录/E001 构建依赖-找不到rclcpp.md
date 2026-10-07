---
tags:
  - 构建
  - 依赖
  - 环境
  - API
  - cmake
  - rclcpp
  - lyrical
---

# E001 · 构建/依赖 — include rclcpp 报错找不到

**日期:** 2026-10-03
**标签:** #构建 #依赖 #环境 #API #cmake #rclcpp #lyrical

## 问题

在 dev_ws 编写程序时，编译器提示找不到 rclcpp 库：

```
fatal error: rclcpp/rclcpp.hpp: No such file or directory
```

## 原因

1. 新建的包（my_package）还没声明 rclcpp 依赖，`package.xml` 和 `CMakeLists.txt` 里都没有。
2. **Lyrical 发行版移除了 `ament_target_dependencies()` 宏**，网上旧教程（Humble/Jazzy）的写法会报 `Unknown CMake command: ament_target_dependencies`。
3. VSCode 的 C++ 插件找不到库路径导致的红线——**并不影响正常编译**（本质是 IDE 提示，不是真实报错）。

## 解决方案

1. `package.xml` 加：

   ```xml
   <depend>rclcpp</depend>
   <depend>std_msgs</depend>
   ```

2. `CMakeLists.txt` 加：

   ```cmake
   find_package(rclcpp REQUIRED)
   find_package(std_msgs REQUIRED)
   target_link_libraries(my_node ${rclcpp_TARGETS} ${std_msgs_TARGETS})
   ```

3. 改完若构建产物没更新，先删 `build/<包名>` 和 `install/<包名>`，再 colcon build。

> **Note（关联）：** Lyrical 的构建 API 差异是后续所有包构建的共同前提，详见 [[N001 节点基础书写骨架]]。
