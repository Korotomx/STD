---
tags:
  - 功能实现
  - launch启动
  - 架构Architecture
  - Python
---

# Python launch 库的内部结构 · 功能实现 · N045

**时间:** 2026-10-09 21:26
**标签:** #功能实现 #launch启动 #架构Architecture #Python
**关联:** [[N044 launch文件与工具链]] [[N011 ROS2分层架构]] [[N012 ROS2的库与职责]]

## 疑惑点

launch 文件里 `from launch import ...`、`from launch.actions import ...`、`from launch_ros.actions import ...` 这么多 import，launch 这个 Python 库内部到底是怎么组织的？每个子模块装什么？`launch` 和 `launch_ros` 是什么关系？「事件」和「事件处理器」是不是一回事？

## 实际情况

1. **launch 是两层：核心 `launch` + ROS 特化 `launch_ros`。** 类似 ROS2 本体分 rclcpp/rcl/rmw 那样（[[N011 ROS2分层架构]]），launch 也分层——`launch` 是**纯 Python、不依赖 ROS** 的通用「进程调度框架」，`launch_ros` 在它之上加 ROS 语义（节点、参数、命名空间）。你写 launch 文件主要碰这两个包。

2. **核心 `launch` 包的子模块与成员：**

   | 子模块 | 装什么 | 常见成员 |
   |---|---|---|
   | `launch`（顶层） | 框架入口 + 运行时 | `LaunchDescription`（动作列表）、`LaunchService`（真正执行的后端/事件循环）、`LaunchContext`（上下文） |
   | `launch.actions` | 动作——「要做什么」 | `ExecuteProcess`（跑外部进程）、`DeclareLaunchArgument`、`IncludeLaunchDescription`（嵌套）、`GroupAction`（分组）、`TimerAction`（延时）、`LogInfo`（打日志）、`OpaqueFunction`（执行一段 Python）、`EmitEvent`（发事件）、`RegisterEventHandler`、`SetLaunchConfiguration` |
   | `launch.conditions` | 条件——「要不要执行」 | `IfCondition`、`UnlessCondition`、`LaunchConfigurationEquals` |
   | `launch.substitutions` | 替换/占位符——「启动时才求值」 | `LaunchConfiguration`（引用参数）、`TextSubstitution`、`EnvironmentVariable`（读环境变量）、`PythonExpression`、`PathJoinSubstitution`（拼路径）、`Command`、`ThisLaunchFileDir`、`FindExecutable`、`AnonName` |
   | `launch.events` | **事件（发生了什么）** | `ProcessStarted`、`ProcessExited`、`ProcessIO`、`Shutdown`、`IncludeLaunchDescription` 等 |
   | `launch.event_handlers` | **事件处理器（发生了 → 做什么）** | `OnProcessStart`、`OnProcessExit`、`OnProcessIO`、`OnShutdown`、`OnIncludeLaunchDescription` |
   | `launch.frontend` / `launch.launch_description_sources` | XML/YAML 格式 launch 的解析器 | （内部用，一般不直接碰） |

3. **最容易混淆：事件 events vs 事件处理器 event_handlers。** 这是两个不同子模块，别混：

   - **事件 `launch.events`**：描述「**发生了什么**」这件事本身（进程退出了、要关机了…），是个**名词**。
   - **事件处理器 `launch.event_handlers`**：描述「**当某事件发生，做什么**」，是个**动作/回调**。

   命名上有规律可记：**事件处理器都以 `On` 开头**（`OnProcessExit` = 在「进程退出」这件事上挂一个动作），它监听的事件名去掉 `On` 就是事件名（`ProcessExit` → `OnProcessExit`）。

   ```python
   from launch.actions import RegisterEventHandler, LogInfo
   from launch.event_handlers import OnProcessExit

   # 当 turtlesim 退出时，打一条日志（事件处理器挂在「进程退出」这个事件上）
   RegisterEventHandler(
       OnProcessExit(
           target_action=turtlesim_node,
           on_exit=[LogInfo(msg='turtlesim 已退出')],
       ),
   )
   ```

4. **`launch_ros` 特化层：** 给 launch 加上 ROS 概念，你天天用的 `Node` 就在这里：

   | 子模块 | 装什么 | 常见成员 |
   |---|---|---|
   | `launch_ros.actions` | ROS 动作 | `Node`（起一个 ROS 节点）、`LifecycleNode`（生命周期节点）、`LoadComposableNodes`、`SetParameter`、`SetParametersFromFile`、`PushRosNamespace`（命名空间） |
   | `launch_ros.substitutions` | ROS 相关替换 | `FindPackageShare`（找包的 share 目录，常配合 [[N033 YAML参数文件与配置分离]]）、`ExecutableInPackage` |
   | `launch_ros.descriptions` | 描述对象 | `ParameterFile`、`ComposableNode` |
   | `launch_ros.event_handlers` | ROS 事件处理器 | `OnStateTransition` |

5. **心智模型（记这个就够）。** launch 的一切都可以归到四个「角色」：

   ```text
   动作 Action ── 触发 ──▶ 事件 Event ── 被监听 ──▶ 事件处理器 EventHandler ── 再发出 ──▶ 新动作
      （要做什么）        （发生了什么）        （发生了→做什么）              （循环）
   动作里的「参数」「话题名」里，凡是启动时才确定的，都是 Substitution 占位符。
   ```

   - **Action** = 要做什么（起节点、声明参数…）
   - **Condition** = 决定 Action 要不要执行
   - **Substitution** = 启动时才求值的占位符
   - **Event / EventHandler** = 事件 + 对事件的响应

## 思考

（留白 —— `TimerAction`（延时）和 `OnProcessExit`（事件处理器）都能实现「先起 A 再起 B」，两者思路有什么不同？`OpaqueFunction` 为什么叫「不透明」函数？）

## 总结

**本质：** launch 库分两层——核心 `launch`（纯 Python 的进程调度框架）+ `launch_ros`（加 ROS 语义）。核心按「角色」分四个子模块：`actions`（要做什么）、`conditions`（要不要做）、`substitutions`（启动时才求值的占位符）、`events`/`event_handlers`（事件 + 对事件的响应）。其中最容易混的是**事件（名词，发生了什么）vs 事件处理器（On 开头，发生了→做什么）**。`LaunchDescription` 是动作列表，`LaunchService` 是真正执行的后端。
**标签:** #功能实现 #launch启动 #架构Architecture #Python
