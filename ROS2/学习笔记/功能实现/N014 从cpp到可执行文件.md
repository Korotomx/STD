---
tags:
  - 功能实现
  - 构建Build
  - 编译
  - 链接
  - 包Package
  - ament
  - colcon
  - export
---

# 从 .cpp 到可执行文件（编译/链接/安装 + 构建体系）· 功能实现 · N014

**时间:** 2026-10-04 17:19 首次记录 · 2026-10-05 17:29 合并 N016（构建体系三角色）
**标签:** #功能实现 #构建Build #编译 #链接 #包Package #ament #colcon #export
**关联:** [[N004 工作空间vs包]] · [[N012 ROS2的库与职责]] · [[N005 CMake注释是井号]] · [[N003 source的作用]]

## 疑惑点

有了 my_node.cpp 和 listener.cpp 两个源文件，可执行文件是怎么生成的？构建体系里 colcon / ament / export 分别是什么？

## 实际情况

### 三样东西接力

`package.xml`(声明要什么) + `CMakeLists.txt`(声明怎么构建) + `colcon build`(执行)。

**① package.xml —— 依赖清单：** `<depend>rclcpp</depend>` `<depend>std_msgs</depend>`，告诉构建系统要用哪些库，不参与编译本身。

**② CMakeLists.txt —— 构建规则：**

| 行 | 作用 |
|----|------|
| find_package(rclcpp/std_msgs REQUIRED) | 找到头文件 + 库文件位置 |
| add_executable(my_node src/my_node.cpp) | 声明把某 .cpp 编成可执行文件 |
| target_link_libraries(my_node ${rclcpp_TARGETS} ...) | 链接依赖库 |
| install(TARGETS ... DESTINATION lib/project1) | 装到 install 目录 |

一个 .cpp 对应一个可执行文件（两个 add_executable → 两个可执行文件）。

**③ 编译四步：** 预处理(#include 展开) → 编译(源码→汇编) → 汇编(→ .o 机器码,函数地址空着) → 链接(.o + 库 → 可执行文件,填地址)。

**核心区分 —— 头文件 vs 库：**
- 头文件给「声明」，让**编译**通过；
- 库给「实现」，让**链接**通过。
- 缺头文件 → 编译报错；缺库 → 链接报错。

`${rclcpp_TARGETS}`(Lyrical 写法，= `rclcpp::rclcpp`)同时携带头文件路径 + 链接库，所以一行 `target_link_libraries` 同时搞定两者（旧 `ament_target_dependencies` 已移除）。

### 构建体系三角色（合并自原 N016）

1. **colcon = 构建工具（指挥官）**：`colcon build` 本身不编译代码，只做调度——扫 `src/` 下所有包 → 读 `package.xml` 确定构建类型与依赖 → 按依赖顺序构建 → 装进 `install/`。生成 `build/`（中间文件）、`install/`（最终产物）、`log/`（日志）三个目录。
2. **ament = 构建系统（执行者）**：`ament_cmake` 是 ROS 2 基于 CMake 的构建系统。`CMakeLists.txt` 里 `find_package(ament_cmake)` 引入规则，末尾 `ament_package()` 收尾——`ament_package()` 在 `install/<包>/share/ament_index/resource/` 下生成包元数据，让 `ros2 pkg` / `ros2 run` 能发现这个包、其他包能 `find_package()` 到它。对应还有 `ament_python`（纯 Python 包用）。
3. **export = 包的「自述」（package.xml 的 `<export>` 标签）**：最关键一项是 `<build_type>ament_cmake</build_type>`，告诉 colcon「这个包用 ament_cmake 构建」。（注意：和 shell 的 `export` 命令是两码事。）

**关系（一条流水线）：**

```
colcon build
  → 读 package.xml 的 <export><build_type>ament_cmake</build_type>
  → 确定用 ament_cmake 构建
  → 执行 CMakeLists.txt：find_package(ament_cmake) → 编译/链接 → ament_package()
  → 产物装进 install/ + 生成 ament index 元数据
  → source install/setup.bash 后，ros2 run 靠元数据找到包
```

一句话：colcon 决定「谁来做」，ament 决定「怎么做」，export 是「告诉 colcon 用 ament 做」。

### 产物与运行

编译产物在 build/，install 复制到 `install/project1/lib/project1/`；`source install/setup.bash` 写入环境变量；`ros2 run project1 my_node` 靠环境变量定位并执行。

> **Note（连接 / 深化）：**
> - 连接：build/install/log 是工作空间级别，见 [[N004 工作空间vs包]]；rclcpp/std_msgs 库的职责见 [[N012 ROS2的库与职责]]；install/setup.bash 靠 ament index 找包，见 [[N003 source的作用]]。
> - 深化：`colcon build --packages-select project1` 只构建指定包；改代码后要重新 build 才能生效（`--symlink-install` 可让 install 软链到源码，改动即时生效）；`ament_package()` 生成的元数据就是 `install/<包>/share/ament_index/resource/` 下的文件。

## 思考

（留白 —— 试着用 g++ 手动编译一次 my_node.cpp 并链接 rclcpp，体会头文件路径和库路径分别从哪来；或 `ls install/project1/share/ament_index/resource/` 看 ament_package 生成了什么）

## 总结

**本质：** `.cpp → 可执行文件` = 预处理/编译/汇编/链接四步；package.xml 声明依赖、CMakeLists.txt 用 find_package/add_executable/target_link_libraries/install 声明构建规则；colcon（工具）读 package.xml 的 export 选 ament（系统）执行，ament_package() 生成 ament index 元数据供 ros2 发现。
**标签:** #功能实现 #构建Build #编译 #链接 #包Package #ament #colcon
