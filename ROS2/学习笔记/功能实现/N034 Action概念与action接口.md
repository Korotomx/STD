---
tags:
  - 功能实现
  - Action动作
  - 接口Interface
  - Server服务端
  - Client客户端
  - 错误Error
---

# Action 动作通信全解（概念 / 服务端 / 客户端 / 三段结构）· 功能实现 · N034

**时间:** 2026-10-07 16:31 首次记录 · 2026-10-20 合并 N035/N036/N054（服务端 / 客户端 / 三段硬性结构）
**标签:** #功能实现 #Action动作 #接口Interface #Server服务端 #Client客户端 #错误Error
**关联:** [[N017 Service概念与srv接口]] [[N024 参数概念与四大通信机制全景]] [[N052 双龟追逐三节点Action实现]]

## 疑惑点

Service 一问一答只能应付短任务；碰上「旋转 90°」「巡逻 5 秒」这种要跑几秒到几分钟的耗时任务，客户端不能干等、想知道进度、想中途停，怎么办？动作服务端 / 客户端分别怎么写？`.action` 三段结构能不能偷懒删掉 feedback 段？

## 实际情况

### 1. 概念：Action = 长任务版 Service（原 N034）

1. **Action = 长任务版 Service（带反馈 + 可取消）**。补全四大机制全景：

   | 机制 | 本质 | 场景 |
   | ---- | ---- | ---- |
   | 话题 Topic | 持续数据流 1→N | 传感器数据、状态广播 |
   | 服务 Service | 一次请求→一次应答 1→1 | 短任务：查位置、算个和 |
   | **动作 Action** | 发目标→持续反馈→交结果，可取消 | 导航、旋转、巡逻 |
   | 参数 Parameter | 配置键值对 | 改背景色、调阈值 |

2. **`.action` 三段结构**（对比 `.srv` 两段）：

   ```
   .srv    两段: request / response       （一个 --- 分隔）
   .action 三段: goal / result / feedback  （两个 --- 分隔）
   ```

   以自定义 `Patrol.action` 为例：

   ```yaml
   float32 duration       # goal   目标：巡逻时长
   ---
   bool completed         # result 结果：是否完成
   string message         #        说明
   ---
   float32 elapsed        # feedback 反馈：已执行时长
   ```

   三段各司其职：`goal` 发什么 → `feedback` 过程中持续回报 → `result` 最后交差。

3. **底层本质 = Service + Topic**。Action 不是新机制，每个动作底层自动展开成：goal（服务）+ result（服务）+ cancel（服务）+ feedback（话题）。`ros2 action list` 看到的每个动作，底下都挂着这一组。所以 Action 是站在 Service 和 Topic 肩膀上搭的「长任务协议」。三段里只有 `feedback` 是「持续、多对多」的，所以用话题；goal/result/cancel 都是「一次、一对一」的，所以用服务。

### 2. 服务端：create_server 三回调 + execute 四件套（原 N035）

1. **create_server 一次性绑定 3 个回调**，各管生命周期的一段：

   ```cpp
   action_server_ = rclcpp_action::create_server<Patrol>(
     this, "patrol",
     handle_goal,      // ① 收到目标 → 接受 or 拒绝
     handle_cancel,    // ② 收到取消 → 同意 or 拒绝
     handle_accepted); // ③ 目标被接受 → 开跑
   ```

2. **① handle_goal**：返回 `GoalResponse`，决定接不接这个目标（可做校验）：

   ```cpp
   rclcpp_action::GoalResponse handle_goal(const GoalUUID &, shared_ptr<const Goal> goal) {
     if (goal->duration <= 0.0f) return rclcpp_action::GoalResponse::REJECT;
     return rclcpp_action::GoalResponse::ACCEPT_AND_EXECUTE;
   }
   ```

3. **② handle_cancel**：返回 `CancelResponse`，决定同不同意取消。

4. **③ handle_accepted → 起独立线程 execute**。为什么要线程？execute 里要 `rate.sleep()` 阻塞循环，若直接放 executor 线程会卡死整个节点的其他回调：

   ```cpp
   void handle_accepted(shared_ptr<GoalHandlePatrol> gh) {
     std::thread{std::bind(&PatrolServer::execute, this, _1), gh}.detach();
   }
   ```

5. **execute 里三个「回报」方法 + 一个「看取消」**：

   ```cpp
   goal_handle->publish_feedback(feedback);  // 持续回报进度（← ServerGoalHandle 方法，继承）
   goal_handle->is_canceling();              // 每圈查是否被请求取消（← ServerGoalHandle 方法，继承）
   goal_handle->canceled(result);            // 告知客户端：已取消（← ServerGoalHandle 方法，继承）
   goal_handle->succeed(result);             // 告知客户端：成功（← ServerGoalHandle 方法，继承）
   ```

   四件套对应 Action 的「反馈 / 取消 / 取消结果 / 成功结果」。

### 3. 客户端：create_client 两回调（原 N036）

1. **create_client + 等服务端上线**：

   ```cpp
   client_ = rclcpp_action::create_client<Patrol>(this, "patrol");
   if (client_->wait_for_action_server(5s)) send_goal();   // ← Client 方法（继承）
   ```

2. **async_send_goal 发目标，options 里挂两个回调**：

   ```cpp
   auto options = rclcpp_action::Client<Patrol>::SendGoalOptions();
   options.feedback_callback = ...;   // 过程中持续触发
   options.result_callback   = ...;   // 结束后触发
   client_->async_send_goal(goal, options);   // ← Client 方法（继承）
   ```

3. **feedback_callback 收反馈**（服务端每 publish_feedback 一次就触发一次）：

   ```cpp
   [this](GoalHandlePatrol::SharedPtr, shared_ptr<const Patrol::Feedback> fb) {
     RCLCPP_INFO(..., "已巡逻 %.0f 秒", fb->elapsed);
   }
   ```

4. **result_callback 收最终结果**，用 `result.code` 区分三种结局：

   ```cpp
   [this](const GoalHandlePatrol::WrappedResult & result) {
     switch (result.code) {
       case ResultCode::SUCCEEDED: ...; break;   // 成功
       case ResultCode::ABORTED:   ...; break;   // 中止
       case ResultCode::CANCELED:  ...; break;   // 取消
     }
   }
   ```

5. **对比 Service 客户端**：Service 的 `async_send_request` 只有一个「响应回调」；Action 拆成「反馈回调 + 结果回调」两个，因为长任务有「中间进度」和「最终结局」两种信息。

6. **三个易混点**：
   - `create_client` 是 `rclcpp_action` 的**自由函数**（不是 Node 方法），看前缀 `rclcpp_action::` 就知来源；这点和 `create_publisher`（Node 方法）不同。
   - `SendGoalOptions` 是「选项结构体」：动作要挂**两个**回调（反馈 + 结果），所以打包进 options 再交给 async_send_goal，和话题/服务直接传回调不同。
   - `WrappedResult` 里包了两样，名字只差一个词，别混：`result.code` = 怎么结束的（`ResultCode` 枚举），`result.result` = 结果内容（.action result 段的字段，如 `result.result->message`）。

### 4. 三段硬性结构与 feedback 留空（原 N054）

不想要 feedback 日志，想把 `.action` 的 feedback 段整个删掉，只留 goal + result 两段：

```
geometry_msgs/Pose target_pose
---
bool caught
```

结果编译直接报错：

```
rosidl_adapter.parser.InvalidActionSpecification:
  Number of '---' separators nonconformant with action definition
```

**原因**：ROS 2 的 `.action` 文件是**硬性三段**：goal → result → feedback，中间**恰好两个 `---`**。feedback 段不能删，只能**留空**（第二个 `---` 后什么都不写）：

```
geometry_msgs/Pose target_pose
---
bool caught
---
```

rosidl_adapter 解析 `.action` 时先按 `---` 把文件劈成三份，数量不是 2 就直接抛 `InvalidActionSpecification`。三段各自是一条消息定义，空段 = 空消息（仍会生成一个空的 `Feedback` 类型）。所以「不用 feedback」的最简做法是留空，不是删段。

想静默（不打日志）但保留 Action 三段，做法是：保留 feedback 字段 + 服务端照常 `publish_feedback` + 客户端挂一个**空** `feedback_callback`：

```cpp
options.feedback_callback =
  [](GoalHandleChaseTurtle::SharedPtr,
     const std::shared_ptr<const ChaseTurtle::Feedback>) {
    // 不打印
  };
```

匿名参数（避免 unused 警告）+ 空函数体：既走通反馈机制，又零日志。

> **Note（连接 / 深化）：**
> - 连接：Action 的 goal/result 服务就是 [[N017 Service概念与srv接口]] 那套服务的封装；`async_send_goal` 和 Service 的 `async_send_request` 同是异步回调姿势（呼应 [[E004 运行时-Service客户端等响应的死锁与executor冲突]] 的教训）。
> - 深化：`result.code` 就是「这个目标最后怎么结束的」——成功 / 服务端主动中止 / 被取消，客户端据此决定后续动作。

## 思考

（留白 —— `feedback_callback` 和 `result_callback` 各触发几次？）

## 总结

**本质：** Action = 带反馈、可取消的长任务版 Service；`.action` 三段 goal/result/feedback 是**硬性三段**（feedback 只能留空不能删），底层由 Service（goal/result/cancel）+ Topic（feedback）拼成。服务端 = `create_server` 绑 3 回调（goal/cancel/accepted）+ execute 线程四件套（publish_feedback / is_canceling / canceled / succeed）；客户端 = `create_client` + `async_send_goal` 挂两个回调（feedback 收进度 / result 收结局，用 result.code 区分成功/中止/取消）。
**标签:** #功能实现 #Action动作 #接口Interface #Server服务端 #Client客户端 #错误Error
