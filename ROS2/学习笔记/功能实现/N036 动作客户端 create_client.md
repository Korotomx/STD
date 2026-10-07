---
tags:
  - 功能实现
  - Action动作
  - Client客户端
---

# 动作客户端 create_client · 功能实现 · N036

**时间:** 2026-10-07 16:31
**标签:** #功能实现 #Action动作 #Client客户端
**关联:** [[N034 Action概念与action接口]] [[N019 客户端实现 create_client]]

## 疑惑点

动作客户端怎么发目标？反馈和结果分别怎么收？和 Service 客户端有啥不同？

## 实际情况

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

> **Note（连接 / 深化）：**
> - 连接：`async_send_goal` 和 [[N019 客户端实现 create_client]] 的 `async_send_request` 同是异步回调姿势，都不阻塞（呼应 [[E004 运行时-Service客户端等响应的死锁与executor冲突]] 的教训）。
> - 深化：`result.code` 就是「这个目标最后怎么结束的」——成功 / 服务端主动中止 / 被取消，客户端据此决定后续动作。

## 思考

（留白 —— `feedback_callback` 和 `result_callback` 各触发几次？）

## 总结

**本质：** 动作客户端 = `create_client` + `async_send_goal` 挂两个回调：feedback_callback 收中间进度、result_callback 收最终结局（用 result.code 区分成功/中止/取消）。
**标签:** #功能实现 #Action动作 #Client客户端
