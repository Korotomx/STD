---
tags:
  - 运行时
  - API
  - Service
  - 客户端
  - 死锁
---

# E004 · 运行时/API — Service 客户端等响应的死锁与 executor 冲突

**日期:** 2026-10-05
**标签:** #运行时 #API #Service #客户端 #死锁

## 问题

在节点（已被 spin 接管）的回调里调 Service 客户端，连续踩两个坑：
1. `future.wait_for(1s)` → 服务端明明返回了，客户端却超时（死锁）
2. 改用 `spin_until_future_complete` → 抛 `Node already been added to an executor`

## 原因

1. **死锁**：`chase()` 回调在单线程 executor 里跑，`future.wait_for()` 阻塞了这条线程；响应到达后需要 executor 派发「响应就绪」回调才能让 future 就绪，但 executor 被堵住 → 响应回不来 → 超时。
2. **executor 冲突**：`spin_until_future_complete` 会把节点加进新 executor，但节点已经被 `rclcpp::spin()` 接管 → 冲突。

## 解决方案

用**异步回调**——节点在 spin 时调服务的正统姿势：

```cpp
client_->async_send_request(request,
  [this](Client<GetTargetPose>::SharedFuture future) {
    auto response = future.get();
    this->move_towards(response->x, response->y);
  });
```

响应到了自动回调，不阻塞、不额外 spin。

> **Note（关联）：** executor 单线程串行见 [[N009 Executor事件循环]]；三种等响应方式的使用场景见 [[N019 客户端实现 create_client]]；死锁本质是「同步阻塞」（主流程 `get()` 卡死 executor），见 [[N042 同步异步与阻塞非阻塞]]。
