---
tags:
  - 功能实现
  - Executor执行器
  - Spin
  - Node节点
  - 多线程
  - Publisher发布者
---

# main 函数变厚 · executor 演进 · 功能实现 · N023

**时间:** 2026-10-05 16:03（2026-10-06 深化）
**标签:** #功能实现 #Executor执行器 #Spin #Node节点 #多线程 #Publisher发布者
**关联:** [[N009 Executor事件循环]] [[N015 话题通信的端到端延迟]] [[N001 节点基础书写骨架]] · [[N029 turtle_painter参数中转节点拆解]]

## 疑惑点

`rclcpp::spin(node)` 那么简洁，为什么真实项目里 main 会写得很「厚」？

## 实际情况

### 0. 纯发布节点：连 spin 都可以省（2026-10-14 深化）

`spin` / executor 处理的是「**进**」——订阅回调、服务 / 动作服务端、定时器回调。**纯发布节点**只往外 `publish`，不订阅、不提供服务、不用定时器；`publish` 是同步写进 DDS，**不依赖 executor**，所以 main 里可以**直接调方法**跑逻辑，根本不用 spin：

```cpp
int main(int argc, char ** argv) {
  rclcpp::init(argc, argv);
  auto node = std::make_shared<DrawCircle>();
  node->draw_circle();   // 方法内 while (rclcpp::ok()) + rate.sleep() 持续发
  rclcpp::shutdown();
  return 0;
}
```

要点：

- **spin 管「进」，publish 管「出」**：出不依赖 spin。只要节点要「收」东西（订阅 pose、起服务端、写定时器回调），就必须 spin，否则回调永远不触发。
- **Ctrl-C 仍有效**：`rclcpp::init()` 装的 SIGINT handler 不依赖 spin，`rclcpp::ok()` 照样在 Ctrl-C 变 false，while 循环能退出。
- **三种「周期发」写法**：

| 写法 | 阻塞? | 适合 |
| ---- | ---- | ---- |
| main 直接调方法（while + rate.sleep） | 阻塞 main | 纯发布、跑一段就完 / 死循环，最简 |
| 定时器 `create_wall_timer` | 不阻塞（回调里发） | 更 ROS 风格，节点还要干别的 |
| `rclcpp::spin(node)` | 阻塞、等回调 | 有订阅 / 服务 / 动作 / 定时器时 |

> **Note（连接 / 深化）：** 画圆 / 画方节点就是「纯发布」，main 里直接 `node->draw_*()` 就够；进阶任务一旦要订阅 `/B/pose` 追目标，就必须改回 spin / executor（见本页「1~3」）。

### 1. spin 是「单节点单线程」的快捷方式

`rclcpp::spin(node)` 内部等价于：

```cpp
rclcpp::executors::SingleThreadedExecutor exec;
exec.add_node(node);
exec.spin();
```

当项目复杂，两个需求会逼你**手动写 executor**：
1. 一个进程放**多个节点**
2. 回调要**并行处理**（单线程串行 = 一个慢回调堵死所有回调，即 [[N015 话题通信的端到端延迟]] 里说的「延迟最大变量」）

### 2. 演进三阶段

**阶段 1 — 最简（单节点单线程）**：

```cpp
rclcpp::init(argc, argv);
rclcpp::spin(std::make_shared<Talker>());
rclcpp::shutdown();
```

**阶段 2 — 单节点 + 多线程**：

```cpp
auto node = std::make_shared<Talker>();
rclcpp::executors::MultiThreadedExecutor executor;
executor.add_node(node);
executor.spin();   // 回调并行处理
```

**阶段 3 — 多节点（一个进程管两个节点）**：

```cpp
auto target = std::make_shared<TargetTurtle>();
auto chaser = std::make_shared<ChaserTurtle>();
rclcpp::executors::MultiThreadedExecutor executor;
executor.add_node(target);
executor.add_node(chaser);
executor.spin();   // 一个进程同时跑两个节点
```

### 3. 对比

| | `rclcpp::spin(node)` | 手动 executor |
|---|---|---|
| 节点数 | 1 | 任意多个 |
| 线程数 | 1（串行） | 可多线程（并行） |
| 适用 | 简单 demo | 真实项目 |

### 4. 线程与进程（底层概念）

- **进程** = 一个独立运行的程序，有自己**独立的内存空间**（类比：一栋独立的房子）；
- **线程** = 进程内部的「执行流」，多个线程**共享**同一进程的内存（类比：房子里的多个工人，共享房间里的东西）；
- 一个进程可以开多个线程。

executor 的线程模型：

```
单线程 executor：  回调队列 ──► 线程1（一个个串行处理）
多线程 executor：  回调队列 ──► 线程1、线程2（并行各处理一个）
```

- 单线程 = **串行**：前一个回调没执行完，后一个只能排队等；
- 多线程 = **并发**：多个线程同时各取一个回调执行，互不等待。

### 5. 为什么 turtle_painter 开 2 个线程

[[N029 turtle_painter参数中转节点拆解]] 里同时有多个回调待命：

1. 定时器回调（2s 后 `apply_color`）
2. 参数回调（`on_param_change`）
3. 异步结果回调（`set_parameters` 的 lambda，等 turtlesim 回复）

若单线程，这些回调**串行排队**，一个没执行完下一个只能等——尤其异步结果回调要等 turtlesim 回复，多线程能让它**及时**被处理、不被别的回调卡住。所以 main 里显式开 **2 个线程**。

### 6. 数据竞争（多线程的代价）

多线程下，若两个回调**同时读写同一个成员变量**，会发生**数据竞争**：例如 [[N020 turtle_chase小海龟追击项目架构与代码拆解]] 里 `pose_callback` 写 `current_x_` 的同时 `handle_get_pose` 读它（假设跑在多线程 executor 上）——可能读到「写了一半」的值，结果不可预测。

解法：用 `std::mutex` 加锁，保证同一时刻只有一个线程访问该变量。

> **Note（连接 / 深化）：**
> - 连接：单线程串行的机制见 [[N009 Executor事件循环]]；串行是延迟根源见 [[N015 话题通信的端到端延迟]]。
> - 深化：多线程 executor 里回调会**并行**跑，多个回调读写同一成员变量（如 `current_x_`）会**数据竞争**，需要加锁（`std::mutex`）——这是「变厚」带来的新代价。

## 思考

（留白 —— 多线程 executor 下，若 `pose_callback` 写 `current_x_` 的同时 `handle_get_pose` 读它，会发生什么？如何用 `std::mutex` 保护？）

## 总结

**本质：** `spin(node)` 是单节点单线程的快捷方式；项目复杂后要手动 executor（`add_node` 多节点、`MultiThreadedExecutor` 多线程），main 因此变厚；多线程带来并行能力，也带来数据竞争代价。
**标签:** #功能实现 #Executor执行器 #多线程 #Publisher发布者
