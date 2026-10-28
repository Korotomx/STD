Action 是带反馈、可取消的长任务版 Service。`.action` 是硬性三段 goal / result / feedback；服务端 `create_server` 绑三个回调 + execute 线程，客户端 `create_client` 挂反馈与结果两个回调。

## 概念

Service 一问一答只能应付短任务；「旋转 90°」「巡逻 5 秒」要跑一段时间，客户端想知进度、想中途停，就用 Action。

| 机制 | 本质 | 场景 |
|---|---|---|
| Topic | 持续数据流 1→N | 传感器数据、状态广播 |
| Service | 一次请求→一次应答 1→1 | 查位置、算个和 |
| Action | 发目标→持续反馈→交结果，可取消 | 导航、旋转、巡逻 |
| Parameter | 配置键值对 | 改阈值 |

`.action` 三段，两个 `---`：

```yaml
float32 duration       # goal：巡逻时长
---
bool completed         # result：是否完成
string message
---
float32 elapsed        # feedback：已执行时长
```

底层 = Service + Topic：goal / result / cancel 各是一个服务，feedback 是话题。只有 feedback 持续、多对多，所以用话题；其余一次、一对一，所以用服务。

## 服务端：三回调 + execute 四件套

```cpp
m_server = rclcpp_action::create_server<Patrol>(
  this, "patrol",
  handle_goal,       // ① 收到目标 → 接受或拒绝
  handle_cancel,     // ② 收到取消 → 同意或拒绝
  handle_accepted);  // ③ 目标被接受 → 开跑

rclcpp_action::GoalResponse handle_goal(
    const rclcpp_action::GoalUUID &, std::shared_ptr<const Patrol::Goal> goal) {
  if (goal->duration <= 0.0f) return rclcpp_action::GoalResponse::REJECT;
  return rclcpp_action::GoalResponse::ACCEPT_AND_EXECUTE;
}

void handle_accepted(std::shared_ptr<GoalHandlePatrol> gh) {
  std::thread{std::bind(&PatrolServer::execute, this, std::placeholders::_1), gh}.detach();
}
```

execute 必须起独立线程：里面有 `rate.sleep()` 阻塞循环，直接放 executor 线程会卡死其他回调。

execute 中三个回报方法 + 一个查取消（均为 `ServerGoalHandle` 方法，继承）：

```cpp
gh->publish_feedback(feedback);   // 持续回报
gh->is_canceling();               // 每圈查取消
gh->canceled(result);             // 告知已取消
gh->succeed(result);              // 告知成功
```

## 客户端：两回调

```cpp
m_client = rclcpp_action::create_client<Patrol>(this, "patrol");
if (m_client->wait_for_action_server(5s)) send_goal();

auto options = rclcpp_action::Client<Patrol>::SendGoalOptions();
options.feedback_callback = ...;   // 过程中持续触发
options.result_callback   = ...;   // 结束后触发一次
m_client->async_send_goal(goal, options);
```

```cpp
options.feedback_callback =
  [this](GoalHandlePatrol::SharedPtr, std::shared_ptr<const Patrol::Feedback> fb) {
    RCLCPP_INFO(this->get_logger(), "已巡逻 %.0f 秒", fb->elapsed);
  };

options.result_callback =
  [this](const GoalHandlePatrol::WrappedResult & result) {
    switch (result.code) {
      case rclcpp_action::ResultCode::SUCCEEDED: break;
      case rclcpp_action::ResultCode::ABORTED:   break;
      case rclcpp_action::ResultCode::CANCELED:  break;
    }
  };
```

对比 Service：`async_send_request` 只有一个响应回调；Action 拆成「反馈回调 + 结果回调」，因为长任务有中间进度和最终结局两种信息。

三个易混点：

- `rclcpp_action::create_client` / `create_server` 是**自由函数**，不是 Node 方法；`create_publisher` 才是 Node 方法。
- `SendGoalOptions` 是选项结构体，把两个回调打包后再交给 `async_send_goal`。
- `WrappedResult` 里 `result.code` 是怎么结束的（枚举），`result.result` 是结果内容（`.action` result 段字段）。

## feedback 只能留空，不能删段

只留 goal + result 两段会编译报错：

```
rosidl_adapter.parser.InvalidActionSpecification:
  Number of '---' separators nonconformant with action definition
```

`.action` 硬性三段，中间恰好两个 `---`。feedback 不用时留空：

```
geometry_msgs/Pose target_pose
---
bool caught
---
```

空段 = 空消息，仍会生成一个空的 `Feedback` 类型。

想静默但保留机制：保留 feedback 字段、服务端照常 publish、客户端挂空回调：

```cpp
options.feedback_callback =
  [](GoalHandleChaseTurtle::SharedPtr,
     const std::shared_ptr<const ChaseTurtle::Feedback>) {
    // 不打印
  };
```

## 坑

- execute 不放独立线程 → 阻塞 executor。
- `.action` 删 feedback 段 → 编译失败，只能留空。
- `result.code` 与 `result.result` 混用。
- 客户端不 `wait_for_action_server` 就发目标 → 失败。
- goal_handle 用完要 `reset()` 清空，否则分不清是否空闲。

> PS：Action 服务端与客户端必须成对；goal 里引用其他消息（如 `geometry_msgs/Pose`）时 CMake 要 `DEPENDENCIES`。

Action = Service（goal/result/cancel）+ Topic（feedback）；服务端三回调 + execute 四件套，客户端 feedback/result 两回调；三段结构硬性，feedback 只能留空。