---
tags:
  - 项目学习
  - turtlesim
  - Service服务
  - spawn
  - kill
  - set_pen
---

# 死亡重生 spawn/kill 参考 · 项目学习 · N051

**时间:** 2026-10-14 13:26
**标签:** #项目学习 #turtlesim #Service服务 #spawn #kill #set_pen
**关联:** [[N049 双龟追逐进阶任务参考与伪代码]] [[E004 运行时-Service客户端等响应的死锁与executor冲突]] [[N020 turtle_chase小海龟追击项目架构与代码拆解]]

## 背景

进阶任务要「B 被追到后原位消失、新随机位置重生」，这需要调用 turtlesim 自带的三个服务。写了个参考节点 `respawn_demo`（`~/ros2_course_ws/src/turtle_chase/src/respawn_demo.cpp`），完整走一圈出生→死亡→重生，给 game_controller 复用。

## 做了什么

```
随机位置 spawn B → set_pen 藏轨迹 → 停 3s → kill B → 停 1s → 新位置 respawn B → 重新 set_pen
```

## 三个服务（都是 turtlesim_msgs 自带）

| 服务 | 类型 | 请求字段 | 作用 |
| ---- | ---- | ---- | ---- |
| `/spawn` | `turtlesim_msgs::srv::Spawn` | `x, y, theta, name`（name 可空自动生成） | 生一只新海龟 |
| `/kill` | `turtlesim_msgs::srv::Kill` | `name` | 删掉一只海龟 |
| `/B/set_pen` | `turtlesim_msgs::srv::SetPen` | `r, g, b, width, off` | `off=1` 关画笔藏轨迹 |

注意：spawn/kill 是**全局**服务；set_pen 是**每只海龟一个**（命名空间 `/<名字>/set_pen`）。

## 两个关键点

1. **阻塞等响应放线程、spin 放主线程**（对应 [[E004]]）：`async_send_request(req).get()` 会阻塞，若写在回调里会把 executor 一起堵死；所以丢进 `std::thread`，主线程 `rclcpp::spin` 照常跑去收响应。
2. **kill + spawn 后画笔复位**：新生的海龟 pen 默认开，重生后要**重新** `set_pen(off=1)` 才不露轨迹。

## 怎么跑

```bash
ros2 run turtlesim turtlesim_node
ros2 run turtle_chase respawn_demo
```

## 总结

「死亡/重生」= `kill(name)` + `spawn(name, 新坐标)` 两次服务调用，再补一次 `set_pen(off=1)`；把阻塞等响应丢线程、executor 留在主线程，是避免死锁的正解。追击本身不重写，多出来的都是这三个服务的调用与编排（同 [[N049]] 的结论）。
