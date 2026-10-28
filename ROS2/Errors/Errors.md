开发中踩过的坑，按「现象 / 原因 / 解决 / 预防」记录；顶部是按类别索引。

## 索引

| 编号 | 类别 | 问题 |
|---|---|---|
| [[#E001 找不到 rclcpp\|E001]] | 构建/依赖 | include rclcpp 失败，Lyrical 移除 ament_target_dependencies |
| [[#E002 话题多发布者\|E002]] | 运行时 | 残留节点导致 listener 收到交叉消息 |
| [[#E003 turtlesim 消息拆包\|E003]] | 构建/依赖 | turtlesim 接口在 turtlesim_msgs |
| [[#E004 Service 客户端死锁\|E004]] | 运行时/API | 回调里同步等响应，executor 被堵死 |
| [[#E005 参数回调慢一拍\|E005]] | 运行时/API | on_set 读到旧值 |
| [[#E006 形参遮蔽成员\|E006]] | API | 形参用 m_ 前缀与成员同名 |
| [[#E007 非静态成员用 auto\|E007]] | API | 成员声明处无法推断类型 |

## E001 找不到 rclcpp

**现象**：编译报 `fatal error: rclcpp/rclcpp.hpp: No such file or directory`；用旧教程写法还报 `Unknown CMake command: ament_target_dependencies`。

**原因**：新包没有声明 rclcpp 依赖；Lyrical 移除了 `ament_target_dependencies()`，旧教程（Humble/Jazzy）写法失效。VSCode 的红线只是 IDE 找不到路径，不影响编译。

**解决**：

```xml
<depend>rclcpp</depend>
<depend>std_msgs</depend>
```

```cmake
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
target_link_libraries(my_node ${rclcpp_TARGETS} ${std_msgs_TARGETS})
```

**预防**：新建包时就把依赖写全；只用当前发行版文档；构建产物不更新时先删 `build/<包>` 与 `install/<包>` 再 build。

## E002 话题多发布者

**现象**：listener 收到的计数远超 talker 发出量（talker 到 130，listener 已 500+），数字乱跳。

**原因**：图上有两个同名 talker 同时发布（一个残留 + 一个新开），listener 两个都收；`count_` 是每进程独立计数，交错后看起来飞涨。残留来自 `ros2 run ... &` 后 `kill` 了 Python 壳，真正的节点子进程变成孤儿继续跑。

```bash
ros2 node list
# /listener /listener /talker /talker
ros2 topic info /topic
# Publisher count: 2
```

**解决**：杀真正的节点进程（可执行文件路径），不是 `ros2 run` 壳：

```bash
pkill -f "install/project1/lib/project1/my_node"
pkill -f "install/project1/lib/project1/listener"
```

**预防**：前台运行用 Ctrl+C（SIGINT 优雅退出）；后台运行记录真实 PID 或按可执行文件路径杀。

## E003 turtlesim 消息拆包

**现象**：`#include "turtlesim/msg/pose.hpp"` 报找不到文件。

**原因**：Lyrical 把 turtlesim 拆成 `turtlesim`（应用，不导出消息）和 `turtlesim_msgs`（Pose / Color / Spawn / Kill / SetPen / RotateAbsolute）。`find_package(turtlesim)` 拿不到 `${turtlesim_TARGETS}`。

**解决**：

```cpp
#include "turtlesim_msgs/msg/pose.hpp"
using turtlesim_msgs::msg::Pose;
```

```xml
<depend>turtlesim_msgs</depend>
```

```cmake
find_package(turtlesim_msgs REQUIRED)
target_link_libraries(my_node ${turtlesim_msgs_TARGETS})
```

**预防**：类型名拿不准先 `ros2 interface list | grep turtle` / `ros2 interface show`，别照旧教程。

## E004 Service 客户端死锁

**现象**：在已被 spin 的回调里调服务：

1. `future.wait_for(1s)` 服务端明明返回了，客户端却超时。
2. 改 `spin_until_future_complete` 后抛 `Node already been added to an executor`。

**原因**：`chase()` 回调跑在单线程 executor 里，`wait_for` 阻塞这条线程；响应到达后需要 executor 派发回调才能让 future 就绪，但 executor 被堵住 → 响应回不来 → 超时。`spin_until_future_complete` 会把节点加进新 executor，与已有的 `rclcpp::spin` 冲突。

**解决**：用异步回调：

```cpp
m_client->async_send_request(request,
  [this](rclcpp::Client<GetTargetPose>::SharedFuture future) {
    auto response = future.get();
    this->move_towards(response->x, response->y);
  });
```

**预防**：记住「回调里不能阻塞等」；等响应只有三种姿势，按是否在 executor 线程里选，见 [[N017 Service概念与srv接口]]。同步等待只放在 main 或独立线程。

## E005 参数回调慢一拍

**现象**：`ros2 param set` 改参数后，转发给 turtlesim 的颜色总是上一次的值；再改一次才变成上上次想要的。

**原因**：用的是 `add_on_set_parameters_callback`，它在参数写入容器**之前**触发，回调里 `get_parameter` 读到的还是旧值。新值在回调参数 `params` 里，还没进容器。

**解决**：改用 `add_post_set_parameters_callback`（写入之后触发），签名从返回 `SetParametersResult` 改为 `void`：

```cpp
m_cb_handle = this->add_post_set_parameters_callback(
  std::bind(&TurtlePainter::on_param_change, this, std::placeholders::_1));

void on_param_change(const std::vector<rclcpp::Parameter> & params) { ... }
```

**预防**：要「读新值做联动」用 post；要「校验并拒绝修改」用 on（返回 `successful = false`）；三种时机见 [[N024 参数概念与四大通信机制全景]]。

## E006 形参遮蔽成员

**现象**：`publish_cmd_vel` 的形参写成 `m_v` / `m_w`，和成员同名。能编译，但函数里的 `m_v` 到底指谁不清晰。

**原因**：C++ 形参优先，函数体内同名标识符指向形参，成员被遮蔽（shadowing）。读代码的人会误以为在操作成员。

**解决**：`m_` 前缀只留给成员，形参用普通名：

```cpp
// 改前
void publish_cmd_vel(rclcpp::Rate & rate, double duration, double m_v, double m_w)
// 改后
void publish_cmd_vel(rclcpp::Rate & rate, double duration, double linear, double angular)
```

**预防**：成员统一 `m_`，形参/局部不用该前缀；固定值别当参数传，写 `constexpr`；不可拷贝对象（如 `Rate`）只能传引用。

## E007 非静态成员用 auto

**现象**：`auto m_period = 500ms;` 编译报 `non-static data member declared with placeholder 'auto'`。

**原因**：C++ 不允许 `auto` 用于非静态成员变量。非静态成员在类里只有声明、构造时才初始化，声明处没有初始值可推断。`auto` 只能用于声明处带初始化器的地方：局部变量、static 成员、函数返回类型。

这段代码原先放在没有 CMakeLists/package.xml 的目录里，从没被编译过，搬进能构建的包才现形。

**解决**：显式类型：

```cpp
std::chrono::milliseconds m_period = 500ms;
```

**预防**：`auto` 合法性的判断标准是「声明处有没有初始化器可推断」；非静态成员写显式类型或 `constexpr`。局部变量 `auto response = future.get();` 完全合法。
