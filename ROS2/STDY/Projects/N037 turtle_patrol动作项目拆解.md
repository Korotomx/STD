`turtle_patrol` 把「巡逻」抽象成 Action：客户端发时长目标，服务端驱动海龟并每秒回报进度，结束交结果。一条 Action 链路 + 一条 Topic 链路，是 Action 三段结构的最小项目。

## 结构

```
turtle_patrol/
├── action/Patrol.action   # goal / result / feedback
├── src/patrol_server.cpp  # 收目标、驱动海龟、发反馈
├── src/patrol_client.cpp  # 发目标、收反馈/结果
├── CMakeLists.txt         # rosidl 生成 .action
└── package.xml            # rclcpp、rclcpp_action、geometry_msgs
```

## 通信与生命周期

```
client ══Action /patrol══> server ══Topic /turtle1/cmd_vel══> turtlesim
  goal "巡逻5秒"              收目标 → 驱动 + feedback        收速度 → 运动
  ← feedback / result
```

```
① client 发 goal（duration=5）
② server handle_goal 接受 → handle_accepted 起线程
③ execute 每秒 publish_feedback（elapsed=1,2,3...）
④ 结束 succeed(result)；中途取消 → canceled(result)
```

## 角色

- **patrol_server**：动作服务端 + 话题发布者，一个节点身兼两种通信角色。
- **patrol_client**：纯动作客户端，只发目标、收回报。

execute 跑在 detach 的独立线程，发 feedback 不被 executor 阻塞，这是「一边执行一边回报」的关键，见 [[N009 Executor事件循环]]。

> PS：结构与 [[turtle_chase_game_项目总结]] 的 chaser 相同，区别是巡逻定速直走、追击闭环。

Action 管长任务生命周期，Topic 管实际运动。