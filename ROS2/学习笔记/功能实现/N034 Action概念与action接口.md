---
tags:
  - 功能实现
  - Action动作
  - 接口Interface
---

# Action 概念与 .action 接口 · 功能实现 · N034

**时间:** 2026-10-07 16:31
**标签:** #功能实现 #Action动作 #接口Interface
**关联:** [[N017 Service概念与srv接口]] [[N024 参数概念与四大通信机制全景]]

## 疑惑点

Service 一问一答只能应付短任务；碰上「旋转 90°」「巡逻 5 秒」这种要跑几秒到几分钟的耗时任务，客户端不能干等、想知道进度、想中途停，Service 的 request/response 装不下，怎么办？

## 实际情况

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

3. **底层本质 = Service + Topic**。Action 不是新机制，每个动作底层自动展开成：goal（服务）+ result（服务）+ cancel（服务）+ feedback（话题）。`ros2 action list` 看到的每个动作，底下都挂着这一组。所以 Action 是站在 Service 和 Topic 肩膀上搭的「长任务协议」。

> **Note（连接 / 深化）：**
> - 连接：Action 的 goal/result 服务和 [[N017 Service概念与srv接口]] 的服务是同一套东西，只是被 rclcpp_action 封装成了更高级的「长任务」接口。
> - 深化：三段里只有 `feedback` 是「持续、多对多」的，所以底层用话题；goal/result/cancel 都是「一次、一对一」的，所以用服务。

## 思考

（留白 —— 为什么 feedback 用话题、goal/result 用服务，而不是反过来？）

## 总结

**本质：** Action = 带反馈、可取消的长任务版 Service；`.action` 三段 goal/result/feedback 分别对应「发什么 / 交什么 / 过程中回报什么」；底层由 Service（goal/result/cancel）+ Topic（feedback）拼成。
**标签:** #功能实现 #Action动作 #接口Interface
