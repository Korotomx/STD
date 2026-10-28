launch 用一条命令拉起多个节点、统一退出。它是一个 Python 脚本：`generate_launch_description()` 返回动作列表，不跑业务逻辑，只负责调度。本篇从文件写法讲到 launch 库的两层结构。

## 文件骨架

```bash
ros2 launch turtle_status turtle_status.launch.py
```

```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():          # 固定入口
    return LaunchDescription([              # 动作列表
        Node(package='turtlesim', executable='turtlesim_node', name='turtlesim'),
        Node(package='turtle_status', executable='status_reporter', name='status_reporter'),
    ])
```

`Node(package=, executable=, name=, output=)`：`package` + `executable` 定位可执行文件，`name` 是运行时节点名（可和 executable 不同）。

## 五个核心机制

### 声明与引用参数

```python
turtle_name = LaunchConfiguration('turtle_name')                # 引用：占位符
DeclareLaunchArgument('turtle_name', default_value='turtle1')   # 声明：挖坑 + 默认值
```

`LaunchConfiguration` 返回的是占位符，真正的值启动时才确定（命令行传了就用，否则用默认）。引用一个没声明的参数会报错。

### 命令行覆盖

```bash
ros2 launch turtle_status turtle_status.launch.py turtle_name:=turtle2 use_gui:=false
```

`--show-args` 列出所有可调参数。同一份文件，启动时改配置，不改代码。

### remap：不改源码改话题名

```python
remappings=[
    ('/turtle1/pose',   ['/', turtle_name, '/pose']),
    ('/turtle1/status', ['/', turtle_name, '/status']),
],
```

左边是源码写死的名字，右边是运行时实际用的名字。`['/', turtle_name, '/pose']` 是 substitution 列表，启动时拼成一个字符串（`turtle2` → `/turtle2/pose`）。节点以为自己还在用 `/turtle1/...`，实际数据走 `/turtle2/...`——改通信拓扑，不改 C++。

### 条件启动

```python
condition=IfCondition(use_gui),   # 'false' 时整个节点跳过
```

`use_gui` 是字符串 `'true'` / `'false'`，launch 在启动时解释。

### 参数文件 + 内联覆盖

```python
parameters=[
    os.path.join(get_package_share_directory('turtle_status'), 'config', 'params.yaml'),
    {'turtle_name': turtle_name},
],
```

`parameters` 是列表，后面的覆盖前面的。完整优先级：`命令行 :=` > `内联参数` > `YAML 文件` > `代码 declare_parameter 默认值`。

## launch 库的两层结构

和 ROS 2 本体一样分层：核心 `launch` 是纯 Python、不依赖 ROS 的进程调度框架；`launch_ros` 在它之上加 ROS 语义（节点、参数、命名空间）。

**核心 `launch`**

| 子模块 | 装什么 | 常见成员 |
|---|---|---|
| `launch` | 框架入口 + 运行时 | `LaunchDescription`、`LaunchService`、`LaunchContext` |
| `launch.actions` | 要做什么 | `ExecuteProcess`、`DeclareLaunchArgument`、`IncludeLaunchDescription`、`GroupAction`、`TimerAction`、`LogInfo`、`OpaqueFunction`、`EmitEvent`、`RegisterEventHandler`、`SetLaunchConfiguration` |
| `launch.conditions` | 要不要执行 | `IfCondition`、`UnlessCondition`、`LaunchConfigurationEquals` |
| `launch.substitutions` | 启动时才求值的占位符 | `LaunchConfiguration`、`TextSubstitution`、`EnvironmentVariable`、`PythonExpression`、`PathJoinSubstitution`、`Command`、`ThisLaunchFileDir`、`FindExecutable`、`AnonName` |
| `launch.events` | 发生了什么 | `ProcessStarted`、`ProcessExited`、`ProcessIO`、`Shutdown` |
| `launch.event_handlers` | 发生了 → 做什么 | `OnProcessStart`、`OnProcessExit`、`OnProcessIO`、`OnShutdown` |
| `launch.frontend` | XML/YAML 格式解析 | 内部用 |

**事件 vs 事件处理器**是两个不同子模块：

- `launch.events` 描述「发生了什么」（名词）：进程退出了、要关机了。
- `launch.event_handlers` 描述「当某事件发生做什么」（动作/回调），命名都以 `On` 开头。

```python
from launch.actions import RegisterEventHandler, LogInfo
from launch.event_handlers import OnProcessExit

RegisterEventHandler(
    OnProcessExit(
        target_action=turtlesim_node,
        on_exit=[LogInfo(msg='turtlesim 已退出')],
    ),
)
```

**`launch_ros` 特化层**

| 子模块 | 常见成员 |
|---|---|
| `launch_ros.actions` | `Node`、`LifecycleNode`、`LoadComposableNodes`、`SetParameter`、`SetParametersFromFile`、`PushRosNamespace` |
| `launch_ros.substitutions` | `FindPackageShare`、`ExecutableInPackage` |
| `launch_ros.descriptions` | `ParameterFile`、`ComposableNode` |
| `launch_ros.event_handlers` | `OnStateTransition` |

心智模型：

```
动作 Action ──触发──▶ 事件 Event ──被监听──▶ 事件处理器 EventHandler ──再发出──▶ 新动作
（要做什么）        （发生了什么）        （发生了→做什么）              （循环）
动作里的参数、话题名，凡是启动时才确定的，都是 Substitution。
```

- Action：要做什么
- Condition：Action 要不要执行
- Substitution：启动时才求值的占位符
- Event / EventHandler：事件 + 响应

## 工具链

```bash
ros2 launch <pkg> <file> --show-args    # 查可调参数
ros2 run <pkg> <executable>             # 单节点（launch 的底层）
ros2 node list / info                   # 节点、某节点 pub/sub 全景
ros2 param list / get / set             # 参数
ros2 topic list / echo / info           # 话题
```

launch 支持 Python（主流）/ XML / YAML 三种格式。

## 坑

- `LaunchConfiguration` 是占位符不是值，直接拿来做字符串拼接会出错，用 `PathJoinSubstitution` 等。
- 参数文件顶层节点名和 launch 里的 `name=` 不一致，参数静默不生效。
- remap 的左边必须和源码里的名字逐字一致。
- 事件处理器 `On*` 只监听一次还是每次，取决于处理器类型；循环触发要看清语义。

> PS：`TimerAction` 和 `OnProcessExit` 都能「先起 A 再起 B」：前者按时间，后者按事件。

launch 是「动作列表 + 占位符 + 条件 + 事件」的声明式调度；核心 `launch` 管进程，`launch_ros` 加节点语义；最实用的四件事是声明参数、命令行覆盖、remap、参数文件优先级。