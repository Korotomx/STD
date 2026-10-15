---
tags:
  - 功能实现
  - Action动作
  - 接口Interface
---

# action 三段硬性结构与 feedback 留空 · 功能实现 · N054

**时间:** 2026-10-15
**标签:** #功能实现 #Action动作 #接口Interface #错误Error
**关联:** [[N034 Action概念与action接口]] [[N052 双龟追逐三节点Action实现]]

## 疑惑点

不想要 feedback 日志,想把 `.action` 的 feedback 段整个删掉,只留 goal + result 两段:

```
geometry_msgs/Pose target_pose
---
bool caught
```

结果编译直接报错:

```
rosidl_adapter.parser.InvalidActionSpecification:
  Number of '---' separators nonconformant with action definition
```

## 实际情况

ROS 2 的 `.action` 文件是**硬性三段**:goal → result → feedback,中间**恰好两个 `---`**。feedback 段不能删,只能**留空**(第二个 `---` 后什么都不写):

```
geometry_msgs/Pose target_pose
---
bool caught
---
```

## 原理

rosidl_adapter 解析 `.action` 时先按 `---` 把文件劈成三份,数量不是 2 就直接抛 `InvalidActionSpecification`。三段各自是一条消息定义,空段 = 空消息(仍会生成一个空的 `Feedback` 类型)。所以「不用 feedback」的最简做法是留空,不是删段。

## 总结

想静默(不打日志)但保留 Action 三段的技术含量,做法是:保留 feedback 字段 + 服务端照常 `publish_feedback` + 客户端挂一个**空** `feedback_callback`:

```cpp
options.feedback_callback =
  [](GoalHandleChaseTurtle::SharedPtr,
     const std::shared_ptr<const ChaseTurtle::Feedback>) {
    // 不打印
  };
```

匿名参数(避免 unused 警告)+ 空函数体:既走通反馈机制,又零日志。
