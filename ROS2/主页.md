ROS 2 学习与开发笔记入口。几个主干并列，每个主干下是当前进度与笔记链接。

## 基础：节点与通信原语

- [[N001 节点基础书写骨架]] — 七部分骨架、发布/订阅、geometry_msgs、海龟控制（已完成）
- [[N002 QoS队列深度10]] — QoS 四维、端到端延迟、DDS/RTPS/UDP（已完成）
- [[N050 海龟命名与spawn-kill关系]] — 名字、spawn/kill、重生（已完成）
- 语法补充：[[ROS2/STDY/Syntax/Syntax|Syntax]] — C++ / CMake 索引

## 通信：四大机制

- [[N017 Service概念与srv接口]] — 请求-响应、服务端/客户端、三种等响应（已完成）
- [[N024 参数概念与四大通信机制全景]] — 参数容器、参数服务与回调、YAML 配置分离（已完成）
- [[N034 Action概念与action接口]] — 三段结构、服务端三回调、客户端两回调（已完成）
- [[N043 自定义消息msg与发布订阅闭环]] — `.msg` 生成与命名、发布订阅闭环（已完成）
- [[N044 launch文件与工具链]] — launch 写法与库结构（已完成）
- [[四大通信机制语法速查表]] — 四机制最小语法骨架

## 构建与架构

- [[N004 工作空间vs包]] — workspace / source / 从 .cpp 到可执行 / colcon-ament-export（已完成）
- [[N011 ROS2分层架构]] — rclcpp / rcl / rmw / DDS 与库职责（已完成）

## Executor 与回调

- [[N009 Executor事件循环]] — 事件循环、spin 退出、手动 executor、异步与 future、std::thread（已完成）
- [[N006 stdbind与回调]] — bind、占位符、lambda（已完成）

## 项目

- [[turtle_draw_项目总结]] — 画方画圆 + 参数中转（基础任务，已完成）
- [[turtle_chase_game_项目总结]] — 三节点 Action 双龟追逐（进阶任务，已完成；躲墙为可选扩展）
- [[N037 turtle_patrol动作项目拆解]] — Action 最小项目（已完成）

## Errors

- [[ROS2/Errors/Errors]] — E001~E007 错误日志与索引

## 学习状态

- 基础通信、四大机制、构建体系、Executor 已学完。
- 课程设计基础任务与进阶任务均已实现并提交。
- 待办：导航、仿真。

## 环境

- ROS 2 Lyrical，RMW 为 CycloneDDS
- 工作空间：`~/dev_ws`、`~/ros2_course_ws`
