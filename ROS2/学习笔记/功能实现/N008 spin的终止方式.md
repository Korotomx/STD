---
tags:
  - 功能实现
  - Spin
  - Signal信号
  - Node节点
---

# spin 的终止方式 · 功能实现 · N008

**时间:** 2026-10-03（原记录未记时分）
**标签:** #功能实现 #Spin #Signal信号 #Node节点
**关联:** [[N009 Executor事件循环]] · [[N001 节点基础书写骨架]]

## 疑惑点

除了 Ctrl+C，还有什么方法会导致 spin 终止？

## 实际情况

**优雅终止（spin 正常返回、走 shutdown 清理）：**

1. **SIGINT**（Ctrl+C，signal 2）—— 终端按 Ctrl+C
2. **SIGTERM**（signal 15）—— `kill <pid>`、`timeout` 命令默认发这个
3. **`rclcpp::shutdown()`** —— 代码里主动调用（回调里、另一线程里），触发全局关闭

**非优雅终止（进程直接死、不清理）：**

- **SIGKILL**（`kill -9`）—— 强制杀，无法被捕获

**重点：** rclcpp 默认注册 SIGINT 和 SIGTERM 两个信号处理器，收到后触发全局关闭，spin 返回。

> **Note（连接 / 深化）：**
> - 连接：spin 的「正常返回」对应 Executor 的退出，见 [[N009 Executor事件循环]]。
> - 深化：工程上常用「在回调里调 `rclcpp::shutdown()`」让节点满足条件时自己优雅退出。

## 思考

（留白 —— 试试在回调里调 rclcpp::shutdown()，让节点满足某条件时自己退出）

## 总结

**本质：** spin 通过信号/主动 shutdown 退出；SIGINT、SIGTERM、`rclcpp::shutdown()` 是优雅终止（会清理），SIGKILL 是强制杀、不清理。
**标签:** #功能实现 #Spin #Signal信号 #Node节点
