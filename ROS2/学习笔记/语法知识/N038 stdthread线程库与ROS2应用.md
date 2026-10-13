---
tags:
  - 语法知识
  - C++语法
  - 线程Thread
  - 并发Concurrency
  - Rate频率
  - 时间Time
  - 引用传递Reference
---

# std::thread 线程库与 ROS2 中的应用 · 语法知识 · N038

**时间:** 2026-10-07 17:15
**标签:** #语法知识 #C++语法 #线程Thread #并发Concurrency #Rate频率 #时间Time #引用传递Reference
**关联:** [[N023 main函数变厚 executor演进]] [[N006 stdbind与回调]] [[N035 动作服务端 create_server]]

## 疑惑点

turtle_patrol 服务端里 `handle_accepted` 用 `std::thread{...}.detach()` 起线程跑 execute。std::thread 到底怎么用？join / detach 啥区别？ROS2 里为什么非得这么写？

## 实际情况

### 一、std::thread 基础（C++）

1. **创建即启动**：`std::thread t(func, args...)` —— 构造的同时就开新线程跑 `func`，不会等它。

2. **join vs detach（关键抉择）**：

   | 写法 | 含义 |
   | ---- | ---- |
   | `t.join()` | 当前线程**阻塞等待**子线程跑完，再往下走（回收资源） |
   | `t.detach()` | **分离**：当前线程不等，子线程自己跑完自动回收；分离后不能再 join |

3. **线程函数三种写法**：

   ```cpp
   void task(int n) { ... }                       // ① 普通函数
   std::thread t1(task, 5);

   std::thread t2(                                // ② 成员函数（要 this）
     std::bind(&Cls::method, this, std::placeholders::_1), arg);

   std::thread t3([this]{ this->execute(); });    // ③ lambda
   ```

4. `std::this_thread::sleep_for(1s)` —— 让**当前线程**睡一段时间。

### 二、ROS2 应用：为什么 execute 丢进独立线程

1. execute 里有 `rate.sleep()` 阻塞循环，一跑就是几秒到几分钟；(这种阻塞函数(引起执行流停滞的函数)一般都涉及系统层面的调用(具有速度差), .sleep, .recv, .read等)
2. 若直接放 executor 线程，会卡死整个节点的其他回调（呼应 [[N023 main函数变厚 executor演进]] 的「回调串行」）；
3. 所以 `handle_accepted` 里 `std::thread{...}.detach()` 丢出去——**让阻塞长任务独占一个线程**：

   ```cpp
   void handle_accepted(shared_ptr<GoalHandlePatrol> gh) {
     std::thread{
       std::bind(&PatrolServer::execute, this, std::placeholders::_1),
       gh}.detach();   // ← std::thread 构造 + detach，executor 立刻返回
   }
   ```

4. **为什么 detach 而不是 join**：`handle_accepted` 本身跑在 executor 线程里，若 join 会阻塞 executor → 节点其他回调全卡死。detach 让 executor 马上返回、继续服务别的回调。

### 三、配套两件套：Rate + rclcpp::ok()

- `rclcpp::Rate rate(1.0)` + `rate.sleep()` —— 固定频率循环（每秒一次），sleep 会自动补齐到整周期；
- `rclcpp::ok()` —— 每圈检查 ROS 是否还活着（Ctrl+C 后返回 false，循环退出）：

   ```cpp
   rclcpp::Rate rate(1.0);
   while (rclcpp::ok() && elapsed < goal->duration) {   // ← rclcpp::ok() 是全局函数
     ...
     rate.sleep();
   }
   ```

- **Rate vs `std::this_thread::sleep_for`**：`rate.sleep()` 是「睡到**下一拍**」——按构造周期（如 10Hz=0.1s）往后补，循环体花了多久就少睡多久，**平均频率稳定**；`sleep_for(0.1s)` 是「睡死 0.1s」，循环体耗时会让实际周期变长（0.1s + 体耗时），频率会漂。

- **实际用法（画圆 / 画方节点）**：`rclcpp::Rate rate(10.0)` 起 10Hz 循环**持续重发** cmd_vel——这台 turtlesim 的海龟约 1s 收不到 cmd_vel 就会自动停下，不能「发一次就干等」，要每拍都发：

   ```cpp
   rclcpp::Rate rate(10.0);        // 10Hz = 每 0.1s 一拍
   while (rclcpp::ok()) {
     vel_pub_->publish(msg);        // 每拍都发一次
     rate.sleep();
   }
   ```

### 四、三种「并发」怎么选

| 方式 | 适合场景 |
| ---- | ---- |
| `create_wall_timer` | 周期触发的**快**回调，executor 统一调度 |
| `MultiThreadedExecutor` | 多个快回调并发（每个回调仍快进快出） |
| 手写 `std::thread` | **一个阻塞长任务**独占线程（Action 的 execute） |

> **Note（连接 / 深化）：**
> - 连接：`std::bind` 打包成员函数见 [[N006 stdbind与回调]]；多线程 / 串行 / 数据竞争见 [[N023 main函数变厚 executor演进]]；Action 服务端用线程见 [[N035 动作服务端 create_server]]。
> - 深化：detach 的线程里用了 `this`，前提是节点还在 spin、没被销毁；若节点可能提前析构，要小心悬空指针——这里靠 `rclcpp::ok()` 循环保证「ROS 还在就跑、ROS 停了就退」的时机。

### 五、publish_for：封装「持续发一段时长」（2026-10-14 深化）

「持续重发」可再封装成函数，一段命令发满 `duration` 秒就停。这里引出三个新点：

```cpp
void publish_for(rclcpp::Rate & rate, double duration) {    // ① rate 按引用传
  auto start = this->now();                                  // ② 取时间戳
  while (rclcpp::ok() && (this->now() - start).seconds() < duration) {
    auto msg = geometry_msgs::msg::Twist();
    msg.linear.x = v;        // v / w = 写死的 constexpr 常量（见 N048）
    msg.angular.z = w;
    m_pub_cmd_vel->publish(msg);
    rate.sleep();
  }
}
```

1. **`rclcpp::Rate & rate` 为什么加 `&`**：`Rate` 内部持有时钟节拍状态，**不可拷贝（拷贝构造被 delete）**——写成 `rclcpp::Rate rate` 传值会直接编译报错。要复用同一个 Rate、保持它的节拍，只能传引用 `&`（或指针）。

2. **`this->now()` 取时间戳**：`now()` **继承自 `rclcpp::Node`**（基类方法，非本文件声明），返回 `rclcpp::Time`——当前 ROS 时钟的时刻。

3. **`Time - Time = Duration`，`.seconds()` 转秒**：

   | 表达式 | 类型 | 含义 |
   | ---- | ---- | ---- |
   | `start` / `this->now()` | `rclcpp::Time` | 时刻点 |
   | `this->now() - start` | `rclcpp::Duration` | 时刻相减 → 时长 |
   | `.seconds()` | `double` | 时长转成秒数 |

   `start` 记下进循环那一刻，每圈 `(now - start).seconds()` 算「已过多久」，小于 `duration` 就继续 → 实现「发满 duration 秒」。

> **Note（连接 / 深化）：**
> - 连接：`rclcpp::ok()` + `rate.sleep()` 见本页「三」；固定速度写死 `constexpr` 见 [[N048 constexpr编译期常量]]。
> - 深化：`now()` 默认系统时钟，可配合 `rclcpp::Clock` 用仿真时钟（sim time）；`Duration` 还有 `.nanoseconds()` 等。

## 思考

（留白 —— detach 之后，如果节点先析构了，子线程里访问 `this` 会发生什么？）

## 总结

**本质：** std::thread 用来「把一个阻塞的长任务丢到独立线程」，join=等、detach=不等；ROS2 里 Action 的 execute 正是「阻塞循环 + detach」——executor 负责快回调，独立线程负责长任务，两者分工。
**标签:** #语法知识 #C++语法 #线程Thread #并发Concurrency #时间Time #引用传递Reference
