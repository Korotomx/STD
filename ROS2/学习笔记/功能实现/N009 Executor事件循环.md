---
tags:
  - 功能实现
  - Executor执行器
  - Callback回调
  - Spin
---

# Executor 事件循环 · 功能实现 · N009

**时间:** 2026-10-03（原记录未记时分）
**标签:** #功能实现 #Executor执行器 #Callback回调 #Spin
**关联:** [[N001 节点基础书写骨架]] · [[N008 spin的终止方式]] · [[N006 stdbind与回调]]

## 疑惑点

main 里的 `rclcpp::spin()` 到底在干嘛？程序没有 `while(true)`，那些回调函数（`timer_callback` / `pose_callback`）是怎么被自动触发的？为什么它们能「自己跑起来」？

## 实际情况

`rclcpp::spin(node)` 内部藏着一个**单线程 Executor**，它是整个程序的发动机。它就是一个循环，反复干三件事：

```
while (还没 shutdown) {
    ① 等 —— 直到「有消息到达」或「有定时器到期」；
    ② 把这些事件对应的回调收集起来、排队；
    ③ 按顺序逐个调用回调；  ← pose_callback / timer_callback 在这里被调
}
```

这就是**回调驱动模型**：你的程序没有显式循环、没有「先 A 再 B 再 C」的顺序，而是「事件发生 → executor 排队 → 回调被调 → 回调里改状态/发消息 → 回到等待」。

**三个必须记住的事实：**

1. **回调是串行的** —— 单线程 executor 下，同一时刻只执行一个回调。`pose_callback` 跑到一半时 `timer_callback` 绝不会插进来抢。所以共享成员变量（如 `pose_count_`）不用加锁。
2. **回调要快进快出** —— 回调里若 sleep 1 秒，期间其他回调全在排队干等，导致消息积压、定时器延迟。耗时操作绝不能放进回调。
3. **状态靠成员变量传递** —— 回调之间不互相调用，而是通过读写成员变量（如 `pose_count_`）共享状态。

> **Note（连接 / 深化）：**
> - 连接：回调被谁调、如何绑定，见 [[N006 stdbind与回调]]；spin 如何退出见 [[N008 spin的终止方式]]。
> - 深化：还有**多线程 Executor**（`MultiThreadedExecutor`）可并发执行回调，但此时共享状态就需要加锁；`spin_some` / `spin_until_future_complete` 是不同调度方式。

## 思考

（留白 —— 如果往 timer_callback 里加一句 sleep(500ms)，预测会发生什么，再动手验证）

## 总结

**本质：** `spin` = 单线程 Executor 的「等事件 → 排队 → 调回调」循环；由此派生三条铁律——回调串行、快进快出、状态靠成员变量传递。
**标签:** #功能实现 #Executor执行器 #Callback回调 #Spin
