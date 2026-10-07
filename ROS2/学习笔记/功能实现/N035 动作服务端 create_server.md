---
tags:
  - 功能实现
  - Action动作
  - Server服务端
---

# 动作服务端 create_server · 功能实现 · N035

**时间:** 2026-10-07 16:31
**标签:** #功能实现 #Action动作 #Server服务端
**关联:** [[N034 Action概念与action接口]] [[N018 服务端实现 create_service]]

## 疑惑点

动作服务端怎么写？它比 Service 的 create_service 多出「反馈」和「取消」，代码结构长什么样？

## 实际情况

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

4. **③ handle_accepted → 起独立线程 execute**。为什么要线程？execute 里要 `rate.sleep()` 阻塞循环，若直接放 executor 线程会卡死整个节点的其他回调。

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

> **Note（连接 / 深化）：**
> - 连接：handle_goal/handle_cancel 就像 [[N018 服务端实现 create_service]] 里的服务回调——都是「别人请求、你响应」，只是 Action 把一个长任务拆成了多个「请求-响应」环节。
> - 深化：`publish_feedback` 底层就是往 feedback 话题发消息（呼应 N034 的「feedback 用话题」），所以它能「持续发、客户端持续收」。

## 思考

（留白 —— `handle_accepted` 里为什么用 `detach()` 而不是 `join()`？）

## 总结

**本质：** 动作服务端 = `create_server` 绑 3 回调（goal/cancel/accepted）+ execute 线程里的「四件套」（publish_feedback / is_canceling / canceled / succeed），把长任务拆成「接目标 → 持续反馈 → 交结果」的完整生命周期。
**标签:** #功能实现 #Action动作 #Server服务端
