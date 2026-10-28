`rclcpp::spin()` 内部是一个 Executor 事件循环：等事件、排队、调回调。由此派生出回调串行、快进快出、异步回调、长任务丢线程等一整套调度规则；本篇把这些规则和同步/异步、future、std::thread 串在一起。

## Executor 在做什么

```cpp
while (rclcpp::ok()) {
  ① 等：直到有消息到达或定时器到期
  ② 把对应回调收集、排队
  ③ 按顺序逐个调用
}
```

这是回调驱动模型：程序没有显式 `while(true)` 业务循环，而是「事件发生 → 排队 → 回调被调 → 回调里改状态/发消息 → 回到等待」。

三条铁律：

1. **回调串行**：单线程 executor 同一时刻只执行一个回调，`pose_callback` 跑到一半 `timer_callback` 不会插进来。共享成员变量无需加锁。
2. **回调快进快出**：回调里 sleep 1 秒，其他回调全在排队，消息积压、定时器延迟。耗时操作不能放进回调。
3. **状态靠成员变量传递**：回调之间不互相调用，通过读写成员共享状态。

`rclcpp::spin(node)` 等价于：

```cpp
rclcpp::executors::SingleThreadedExecutor exec;
exec.add_node(node);
exec.spin();
```

## spin 怎么退出

优雅终止（spin 正常返回、走 shutdown 清理）：

- **SIGINT**（Ctrl+C，signal 2）
- **SIGTERM**（`kill <pid>`、`timeout` 默认）
- 代码里主动 `rclcpp::shutdown()`

非优雅终止：**SIGKILL**（`kill -9`），不可捕获、不清理。

rclcpp 默认注册 SIGINT / SIGTERM 处理器，收到后触发全局关闭，`rclcpp::ok()` 变 false，spin 返回。

## main 为什么变厚

### 纯发布节点：可以没有 spin

spin / executor 处理的是「进」——订阅、服务/动作服务端、定时器回调。纯发布节点只往外 `publish`，publish 是同步写进 DDS，不依赖 executor，所以可以直接调方法：

```cpp
int main(int argc, char ** argv) {
  rclcpp::init(argc, argv);
  auto node = std::make_shared<DrawCircle>();
  node->draw_circle();      // 内部 while (rclcpp::ok()) + rate.sleep()
  rclcpp::shutdown();
  return 0;
}
```

**spin 管「进」，publish 管「出」。** 只要节点要「收」东西，就必须 spin，否则回调永远不触发。`rclcpp::init()` 装的 SIGINT handler 不依赖 spin，Ctrl-C 仍能让 `ok()` 变 false。

三种周期发送写法：

| 写法 | 阻塞 | 适合 |
|---|---|---|
| main 直接调方法（while + rate.sleep） | 阻塞 main | 纯发布、跑一段就结束 |
| `create_wall_timer` | 不阻塞 | 节点还要干别的 |
| `rclcpp::spin(node)` | 阻塞等回调 | 有订阅/服务/动作/定时器 |

### 手动 executor：多节点、多线程

```cpp
// 阶段 1：单节点单线程
rclcpp::spin(std::make_shared<Talker>());

// 阶段 2：单节点多线程
auto node = std::make_shared<Talker>();
rclcpp::executors::MultiThreadedExecutor executor;
executor.add_node(node);
executor.spin();

// 阶段 3：一个进程两个节点
auto target = std::make_shared<TargetTurtle>();
auto chaser = std::make_shared<ChaserTurtle>();
rclcpp::executors::MultiThreadedExecutor executor;
executor.add_node(target);
executor.add_node(chaser);
executor.spin();
```

| | `rclcpp::spin(node)` | 手动 executor |
|---|---|---|
| 节点数 | 1 | 任意多 |
| 线程数 | 1（串行） | 可多线程（并行） |
| 适用 | 简单 demo | 真实项目 |

进程与线程：进程有独立内存；线程是进程内执行流，共享进程内存。单线程 executor = 回调串行；多线程 executor = 多个线程各取一个回调并行执行。

多线程的代价是**数据竞争**：两个回调同时读写同一成员（如 `pose_callback` 写 `m_current_x`、服务回调读它），可能读到写了一半的值。解法是 `std::mutex` 保护共享状态：

```cpp
std::mutex m_mutex;

void pose_callback(const Pose::SharedPtr msg) {
  std::lock_guard<std::mutex> lock(m_mutex);
  m_current_x = msg->x;
  m_current_y = msg->y;
}
```

`lock_guard` 构造加锁、析构解锁，异常也能正确释放，比手写 `lock()/unlock()` 安全。

回调组决定哪些回调可以并行。默认 `MutuallyExclusive` 组内串行；`Reentrant` 组内可并行：

```cpp
auto group = this->create_callback_group(rclcpp::CallbackGroupType::Reentrant);
rclcpp::SubscriptionOptions opts;
opts.callback_group = group;
m_sub = this->create_subscription<Pose>("pose", 10, pose_callback, opts);
```

## 回调调度：同步/异步 × 阻塞/非阻塞

两对概念是两个正交维度：

| 对 | 问的是 |
|---|---|
| 同步 / 异步 | 结果怎么回到你手上：当场给 vs 回头通知 |
| 阻塞 / 非阻塞 | 等待期间线程在干嘛：挂起 vs 继续跑 |

| | 阻塞 | 非阻塞 |
|---|---|---|
| **同步** | `fut.get()` 原地等，线程挂起 | `fut.wait_for(0)` 轮询，空转烧 CPU |
| **异步** | 注册回调又 get 卡住（设计矛盾） | 注册回调，事件到了自动触发（ROS 正统） |

异步为什么总配回调：异步函数一调用就先 `return` 了，结果还没算出来，不能从 `return` 值拿；只能约定回调，结果好了回头调它、把结果塞进回调参数。**同步 = 结果从 `return` 回来，异步 = 结果从 callback 参数回来。**

## future：异步结果的凭证

future 是「取餐号」：发起异步操作时结果没好，先给凭证，好了凭 `get()` 取。

| 方法 | 作用 |
|---|---|
| `get()` | 等结果 + 取走（普通 future 只能取一次） |
| `wait()` | 只等，不取 |
| `wait_for(时长)` | 等一段，返回 timeout / ready |
| `valid()` | 是否还能 get |

`std::future` 只能 get 一次；`std::shared_future` 可拷贝、可多次 get（返回 const 引用）。ROS 回调里的 `SharedFuture` 是后者。

future 的三种来源：`std::async`、`std::promise`（手动 `set_value`）、`std::packaged_task`（打包可调用对象）。ROS 2 内部本质是 promise 那一套。

```cpp
// ① std::async：开线程/延后执行，返回 future
auto fut1 = std::async(std::launch::async, [] { return 42; });
int v1 = fut1.get();

// ② std::promise：手动在别处塞结果
std::promise<int> p;
auto fut2 = p.get_future();
std::thread t([&p] { p.set_value(42); });
t.join();
int v2 = fut2.get();

// ③ std::packaged_task：把可调用对象打包
std::packaged_task<int()> task([]{ return 42; });
auto fut3 = task.get_future();
task();                              // 执行后 fut3 就绪
int v3 = fut3.get();
```

`std::launch::async` 强制新线程立即跑；`std::launch::deferred` 延迟到 `get()` 才在当前线程跑。

ROS 2 的固定套路：

```cpp
client_->async_send_request(request,
  [this](rclcpp::Client<T>::SharedFuture future) {
    auto response = future.get();          // 结果已就绪，秒取
    this->move_towards(response->x, response->y);
  });
```

① 发起异步请求并约定回调 → ② 结果好了 ROS 调回调、递 future → ③ 回调里 `get()`。

**为什么回调里 get() 安全、主流程 get() 死锁**：回调被调起时结果已就绪，`get()` 秒取；主流程 `get()` 阻塞当前线程，而「处理结果」要靠 executor 线程，executor 被自己堵住 → 响应永远处理不了。详见 [[ROS2/Errors/Errors]] E004。

## 异步结果怎么回到主流程

`main` 里没有 executor 接管节点时，用 `spin_until_future_complete` 临时转一圈：

```cpp
auto future = client->async_send_request(request);
if (rclcpp::spin_until_future_complete(node, future) ==
    rclcpp::FutureReturnCode::SUCCESS) {
  auto response = future.get();
}
```

它本质仍是异步：请求先发出，函数内部转 executor 直到 future 就绪，所以不会像 `future.get()` 那样把「处理响应」的线程堵死。但节点已经被 `spin` 接管时不能再调用，否则报 `Node has already been added to an executor`。

回调里只做内存操作和 `publish`，耗时控制在毫秒级；磁盘、网络、`sleep`、长计算都要移出。单线程下，一个回调的耗时就是后续所有回调的延迟。

## 长任务：std::thread

Action 的 `execute` 里有 `rate.sleep()` 阻塞循环，直接放 executor 线程会卡死其他回调，所以丢进独立线程：

```cpp
void handle_accepted(std::shared_ptr<GoalHandlePatrol> gh) {
  std::thread{std::bind(&PatrolServer::execute, this, std::placeholders::_1), gh}.detach();
}
```

- `std::thread t(func, args...)` 构造即启动。
- `join()`：当前线程阻塞等子线程结束；`detach()`：分离，子线程自己跑完回收。`handle_accepted` 本身在 executor 线程里，join 会卡死 executor，所以用 detach。
- 线程函数可写普通函数、`std::bind` 成员函数、lambda。

```cpp
void work(int n);                                      // ① 普通函数
std::thread t1(work, 5);

std::thread t2(                                        // ② 成员函数
  std::bind(&Cls::method, this, std::placeholders::_1), arg);

std::thread t3([this] { this->execute(); });           // ③ lambda
```

`std::this_thread::sleep_for(1s)` 让当前线程睡固定时长；它和 `rate.sleep()` 的区别见下。

配套两件套：

```cpp
rclcpp::Rate rate(1.0);
while (rclcpp::ok() && elapsed < goal->duration) {
  ...
  rate.sleep();
}
```

- `rclcpp::ok()` 每圈检查 ROS 是否还活着。
- `rate.sleep()` 是「睡到下一拍」，循环体耗时长就少睡，平均频率稳定；`sleep_for(0.1s)` 是睡死，实际周期会漂。

封装「持续发一段时长」：

```cpp
void publish_for(rclcpp::Rate & rate, double duration) {   // Rate 不可拷贝，必须传引用
  auto start = this->now();                                 // now() 继承自 rclcpp::Node
  while (rclcpp::ok() && (this->now() - start).seconds() < duration) {
    auto msg = geometry_msgs::msg::Twist();
    msg.linear.x = m_v;
    msg.angular.z = m_w;
    m_pub_cmd_vel->publish(msg);
    rate.sleep();
  }
}
```

`Time - Time = Duration`，`.seconds()` 转秒。

三种并发方式怎么选：

| 方式 | 适合 |
|---|---|
| `create_wall_timer` | 周期触发的快回调 |
| `MultiThreadedExecutor` | 多个快回调并发 |
| 手写 `std::thread` | 一个阻塞长任务独占线程（Action execute） |

## 死锁与线程配置

回调里「等」是死锁的共同来源：

| 写法 | 为什么死 | 正确做法 |
|---|---|---|
| 回调里 `future.get()` | executor 线程等自己处理响应 | 异步回调，结果到了再取 |
| 回调里 `wait_for_service()` | 服务发现/响应也要 executor 推进 | 定时器轮询 `service_is_ready()` |
| 回调里 `thread.join()` | 子线程可能也在等 executor | `detach()` 或给子线程独立 executor |
| spin 后构造 `SyncParametersClient` | 内部再次 `spin_until_future_complete` | 用 `AsyncParametersClient` |

线程数按并发回调数配，不是越多越好：

```cpp
rclcpp::executors::MultiThreadedExecutor executor(rclcpp::ExecutorOptions(), 2);
```

两个线程足够「一个跑业务回调、一个处理异步结果」；线程再多，共享状态照样要加锁，收益有限。

## 坑

- **回调里阻塞**是 ROS 2 最常见的死锁根源；长任务用异步或独立线程。
- 多线程 executor 下共享成员不加锁 = 数据竞争。
- detach 的线程里用了 `this`，节点必须活到线程结束；靠 `rclcpp::ok()` 循环保证退出时机。
- `Rate` 不可拷贝，传参必须 `rclcpp::Rate &`。
- 同一个 future 普通版只能 get 一次，第二次行为未定义。

> PS：真实项目优先用 callback group + MultiThreadedExecutor 做隔离，少手写线程；共享状态用 mutex 或原子量。

spin 是「等事件 → 排队 → 调回调」的单线程循环；要并发就换手动 executor，要长任务就 detach 独立线程；异步结果用 future 凭证 + 回调取，绝不在 executor 线程里阻塞等。