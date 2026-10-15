---
tags:
  - 项目学习
  - turtlesim
  - Action动作
  - 架构Architecture
  - 异步async
---

# 双龟追逐三节点 Action 实现 · 项目学习 · N052

**时间:** 2026-10-14 23:30
**标签:** #项目学习 #turtlesim #Action动作 #架构Architecture #异步async
**关联:** [[N049 双龟追逐进阶任务参考与伪代码]] [[N051 死亡重生spawn-kill参考]] [[N020 turtle_chase小海龟追击项目架构与代码拆解]] [[N053 角度归一化atan2-sin-cos]]

## 背景

[[N049]] 定了「Action 三节点」架构、出了伪代码，[[N051]] 补了 spawn/kill 的服务写法。最终完整实现落在 `~/ros2_course_ws/src/turtle_chase_game`（包名 `turtle_chase_game`）。

## 文件与三节点

| 文件 | 节点 | 角色 |
| ---- | ---- | ---- |
| `action/ChaseTurtle.action` | — | goal=`geometry_msgs/Pose target_pose`；result=`caught`+`final_pose`；feedback=`distance`+`angle_error` |
| `src/runner.cpp` | B 龟 | 随机游走，只发 `/B/cmd_vel` |
| `src/chaser.cpp` | A 龟(turtle1) | Action **服务端**，追 B，发 `/turtle1/cmd_vel` |
| `src/chasing_control.cpp` | 裁判 | Action **客户端**，spawn/kill B + 发 goal 编排整场 |
| `launch/` | — | 一键拉起 turtlesim + 三节点 |

追击算法直接复用 [[N020]] 的「角度差比例控制」：`角速度 = K × 角度误差`，其中角度误差做了归一化（见 [[N053]]）。

## 关键新设计一：异步回调链编排（核心）

裁判要跑一个**循环**：`spawn B → 发 goal → 追到 → kill B → 再 spawn → …`

- [[N051]] 的 respawn_demo 用「单独线程 + 阻塞 `.get()`」串这串服务调用；
- 本节点改用**异步回调链**：每个 `async_send_request` 的回调里调下一步，`spawn → set_pen → send_goal → result → kill → spawn → …`，像链条首尾相接。

为什么要这样：客户端要「追到后自动重生再追」，是个持续过程；用回调串起来，`executor` 始终在主线程 `rclcpp::spin` 里跑、永不阻塞，自然避开 [[E004 运行时-Service客户端等响应的死锁与executor冲突]] 的「回调里阻塞等响应 → executor 被堵死」死锁。

## 关键新设计二：service_is_ready 轮询启动

`chasing_control` 用一个 1s 定时器 `try_start()` 反复查 `service_is_ready()` 和 `action_server_is_ready()`，等 turtlesim 的 `/spawn` 服务和 chaser 的 `chase_turtle` 动作都上线了才真正开始。对比 `wait_for_service()`（阻塞等，没上线就一直卡），轮询不阻塞、随时可退出。

## 思考

（留白）

## 总结

进阶任务 = 在 [[N020]] 的追击闭环上，用 **Action 三节点**把「B 的生命周期（spawn/kill 重生）」和「追击编排」拆到裁判节点，再用**异步回调链**把整场游戏串成一个不阻塞的循环。追击本身没变，多出来的是：action 接口 + 服务调用编排 + 异步链。
