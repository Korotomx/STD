---
tags:
  - 项目学习
  - Action动作
---

# turtle_patrol 动作项目拆解 · 项目学习 · N037

**时间:** 2026-10-07 16:31
**标签:** #项目学习 #Action动作
**关联:** [[N034 Action概念与action接口]] [[N035 动作服务端 create_server]] [[N036 动作客户端 create_client]]

## 项目结构

```
dev_ws/src/turtle_patrol/
├── action/Patrol.action       # 自定义动作（goal/result/feedback 三段）
├── src/patrol_server.cpp      # 动作服务端：接收目标，驱动海龟巡逻
├── src/patrol_client.cpp      # 动作客户端：发目标，收反馈/结果
├── CMakeLists.txt             # rosidl 生成 .action + 编译两个节点
└── package.xml                # 依赖 rclcpp / rclcpp_action / geometry_msgs
```

## 通信关系（节点图）

```
(patrol_client) ══Action /patrol══> (patrol_server) ══Topic /turtle1/cmd_vel══> (turtlesim)
  发 goal "巡逻5秒"                   收目标→驱动+发反馈              收速度→海龟动
  ← 收 feedback/result                （回报沿原路返回给客户端）
```

- **patrol_client → patrol_server**：Action（`/patrol`），客户端发 goal、收 feedback/result；
- **patrol_server → turtlesim**：Topic（`/turtle1/cmd_vel`），服务端发速度让海龟前进。

## 完整生命周期

```
① client 发 goal（duration=5）
② server handle_goal 接受 → handle_accepted 起线程
③ execute 循环：每秒 publish_feedback（elapsed=1,2,3...）
④ 循环结束 → succeed(result) → client result_callback 收到 SUCCEEDED
   （若中途取消：is_canceling 命中 → canceled(result) → client 收到 CANCELED）
```

## 各节点角色

- **patrol_server**：既当「动作服务端」（对外提供 /patrol），又当「话题发布者」（对内发 cmd_vel）——一个节点身兼两种通信角色。
- **patrol_client**：纯动作客户端，只发目标、收回报，自己不碰海龟。

> **Note（连接 / 深化）：**
> - 连接：这个项目和 [[N020 turtle_chase小海龟追击项目架构与代码拆解]] 结构类似：都是「一个节点用 Topic 驱动海龟 + 另一个节点用更高层机制交互」，只是这次高层机制是 Action 而非 Service。
> - 深化：服务端的 execute 跑在独立线程（detach），所以发 feedback 时不会被节点的 executor 阻塞——这是 Action 服务端「一边执行一边回报」的关键。

## 总结

**本质：** turtle_patrol 把「巡逻」抽象成一个 Action：客户端发时长目标 → 服务端驱动海龟 + 每秒回报进度 → 结束交结果；一条 Action 链路 + 一条 Topic 链路，把「长任务的完整生命周期」演示清楚。
**标签:** #项目学习 #Action动作
