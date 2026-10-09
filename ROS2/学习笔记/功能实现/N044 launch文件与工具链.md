---
tags:
  - 功能实现
  - launch启动
  - 工具
  - 命令行CLI
---

# launch 文件与工具链 · 功能实现 · N044

**时间:** 2026-10-09 21:26
**标签:** #功能实现 #launch启动 #工具 #命令行CLI
**关联:** [[N033 YAML参数文件与配置分离]] [[N013 占位符与消息流入回调]] [[N025 参数的声明读写与命令行工具]]

## 疑惑点

要跑一个 demo 得开好几个终端、逐个 `ros2 run`、退出还要一个个 Ctrl+C，太麻烦。有没有办法一个文件、一条命令把多个节点一次拉起来？launch 文件到底怎么写、能控制哪些东西？

## 实际情况

1. **launch 是什么。** 把「开一堆终端逐个 ros2 run」变成「一个 Python 脚本 + 一条命令」，统一启动、统一退出。它不跑业务逻辑，只负责**调度**：描述要起哪些节点、给什么参数。

   ```bash
   ros2 launch turtle_status turtle_status.launch.py
   ```

2. **文件骨架：一个入口函数 + 一个动作列表。**

   ```python
   from launch import LaunchDescription
   from launch_ros.actions import Node

   def generate_launch_description():       # ← 固定入口
       return LaunchDescription([           # ← 动作列表
           Node(package='turtlesim', executable='turtlesim_node', name='turtlesim'),
           Node(package='turtle_status', executable='status_reporter', name='status_reporter'),
       ])
   ```

   `Node(package=, executable=, name=, output=)` 描述一个节点：`package`+`executable` 定位可执行文件，`name` 是运行时节点名（可和 executable 不同）。

3. **① 声明参数 vs 引用参数（最易绕）。** 两个动作各管一件事：

   ```python
   turtle_name = LaunchConfiguration('turtle_name')   # 引用：拿到「占位符」不是值
   DeclareLaunchArgument('turtle_name', default_value='turtle1')  # 声明：挖坑+默认值
   ```

   `LaunchConfiguration('turtle_name')` 返回的是**占位符**——真正的值要等启动时才确定（命令行传了什么、还是用默认值）。这和 [[N013 占位符与消息流入回调]] 里 `_1` 的占位思路同源：**先声明（挖坑）、再引用（占坑）**。引用一个没声明的参数会报错。

4. **② 命令行覆盖 `:=`。** 启动时把值塞进那个坑，覆盖 default_value：

   ```bash
   ros2 launch turtle_status turtle_status.launch.py turtle_name:=turtle2 use_gui:=false
   ```

   `--show-args` 列出所有可调参数。这是 launch 最实用的能力：**同一份文件，启动时改配置，不改代码**。

5. **③ 重映射 remap：不碰源码改话题名。** 源码里话题写死，launch 里 remap 直接替换：

   ```python
   remappings=[
       ('/turtle1/pose',   ['/', turtle_name, '/pose']),   # 旧名 → 新名
       ('/turtle1/status', ['/', turtle_name, '/status']),
   ],
   ```

   左边是**源码写死的名字**，右边是**运行时实际用的名字**。右边 `['/', turtle_name, '/pose']` 是 substitution 列表，启动时拼接成一个字符串（turtle2 时拼成 `/turtle2/pose`）。效果：节点以为自己还在用 `/turtle1/...`，实际数据已走 `/turtle2/...`——**改通信拓扑，不改 C++**。

6. **④ 条件启动 IfCondition。** 用一个开关决定节点要不要起：

   ```python
   condition=IfCondition(use_gui),   # use_gui 是 'true'/'false' 字符串，'false' 时整个节点跳过
   ```

7. **⑤ 参数文件 + 内联覆盖（优先级链）。** `parameters` 是列表，**后面的覆盖前面的**（接 [[N033 YAML参数文件与配置分离]]）：

   ```python
   parameters=[
       os.path.join(get_package_share_directory('turtle_status'), 'config', 'params.yaml'),  # 先加载文件
       {'turtle_name': turtle_name},   # 再内联覆盖
   ],
   ```

   完整优先级：`命令行 :=` > `内联参数` > `YAML 文件` > `代码 declare_parameter 默认值`。

8. **工具链（配套命令）。**

   ```bash
   ros2 launch <pkg> <file> --show-args    # 查可调参数
   ros2 run <pkg> <executable>             # 单节点（launch 的底层）
   ros2 node list / info                   # 看节点、某节点 pub/sub 全景
   ros2 param list / get / set             # 参数三件套
   ros2 topic list / echo / info           # 话题三件套
   ```

   launch 支持三种格式：**Python（主流、最强）** / XML / YAML。记 Python 版即可。

## 思考

（留白 —— remap 和参数都能「改话题名」，什么场景该用 remap、什么场景该用参数？IfCondition 的 `'true'` 是字符串，launch 是怎么把它当布尔用的？）

## 总结

**本质：** launch 是一个 Python 脚本，用 `generate_launch_description()` 返回一个动作列表 `LaunchDescription([...])`，声明式描述「起哪些节点、给什么参数」。五个核心机制：声明参数（挖坑）/ 引用参数（占位符）/ 命令行 `:=` 覆盖 / remap 重映射（改通信拓扑不改代码）/ 条件启动（IfCondition），再叠加参数文件的优先级链。它是「工具链」的一环，配套 ros2 node/param/topic 命令使用。
**标签:** #功能实现 #launch启动 #工具 #命令行CLI
