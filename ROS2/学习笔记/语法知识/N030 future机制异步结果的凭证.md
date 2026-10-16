---
tags:
  - 语法知识
  - C++语法
  - future
  - 异步async
  - 回调Callback
---

# future 机制：异步结果的凭证 · 语法知识 · N030

**时间:** 2026-10-06 22:00
**标签:** #语法知识 #C++语法 #future #异步async #回调Callback
**关联:** [[N019 客户端实现 create_client]] [[E004 运行时-Service客户端等响应的死锁与executor冲突]] [[N029 turtle_painter参数中转节点拆解]] [[N007 lambda表达式]] [[N042 同步异步与阻塞非阻塞]]

## 疑惑点

future 到底是什么？为什么异步操作总是返回 future？`get()` 和 `wait()` 有什么区别？为什么在回调里 `get()` 安全、在主流程里 `get()` 会死锁？

## 实际情况

### 一、future 是什么

future = 异步操作的「结果占位符 / 取餐号」。发起异步操作时结果还没好，先给你一张凭证（future），结果好了凭它取结果。

- 同步：`int x = compute();` —— 结果立即到手，`x` 就是结果；
- 异步：`auto fut = async_compute();` —— 结果还没好，先拿凭证，以后 `fut.get()` 取。

### 二、future 的 API

| 方法 | 作用 |
|---|---|
| `get()` | **等结果 + 取走结果**（结果没好会阻塞；`future` 只能 get 一次） |
| `wait()` | 只等结果就绪，**不取走** |
| `valid()` | 检查 future 是否还有效（还能不能 get） |
| `wait_for(时长)` | 等一段时间，返回 `timeout` / `ready` |
| `wait_until(时刻)` | 等到某个时间点 |

### 三、future vs shared_future

- `std::future`：结果**只能 get 一次**（get 后失效）；
- std::future::get() 是「把结果取走」——它用 move 语义把值搬出来,取完盒子就空了。所以普通 std::future 只能 .get() 一次,第二次没有东西可取(行为未定义)。
- `std::shared_future`：**可多次 get、可拷贝共享**。
- std::shared_future::get() 是「看一眼结果」——它返回 const 引用,不搬走,所以可以反复 .get()。

ROS2 回调里见到的 `SharedFuture` 就是后者——回调可能被多处访问，要能反复取。

### 四、future 从哪来（C++ 三种产生方式）

1. **`std::async`** —— 启动一个异步任务，返回 future：

   ```cpp
   auto fut = std::async(std::launch::async, 慢函数, 参数...);
   auto result = fut.get();   // 这里会阻塞到函数跑完
   ```

2. **`std::promise`** —— 手动往 future 里塞结果：

   ```cpp
   std::promise<int> p;
   auto fut = p.get_future();
   // 另一个线程:
   p.set_value(42);        // 塞结果 → fut.get() 立刻能取到 42
   ```

3. **`std::packaged_task`** —— 把一个可调用对象打包成 future：

   ```cpp
   std::packaged_task<int()> task(f);   // 打包函数 f
   auto fut = task.get_future();
   task();                   // 执行 → fut 拿到结果
   ```

> 三者的共同点：**先拿到 future 凭证，之后某处产出结果，再通过 `get()` 取**。ROS2 内部本质上就是 `promise` 那一套。

### 五、ROS2 里的固定套路（你反复看到的那个）

所有异步请求都是同一个形状——**发请求 + 留回调，结果好了调回调、future 作为参数递进来，回调里 `get()`**：

```cpp
// 例 1：Service 客户端（turtle_chase）
client_->async_send_request(request,
  [this](rclcpp::Client<...>::SharedFuture future) {
    auto response = future.get();          // 结果已就绪，秒取
    this->move_towards(response->x, response->y);
  });

// 例 2：参数客户端（turtle_painter）
param_client_->set_parameters({...},
  [this](std::shared_future<std::vector<...>> fut) {
    auto results = fut.get();              // 结果已就绪，秒取
  });
```

三步：**① 发起异步请求（同时约定回调）→ ② 结果好了 ROS 调回调、递 future → ③ 回调里 `get()` 取结果。**

### 六、为什么「回调里 get() 安全、主流程 get() 死锁」

- **回调里 `get()` 安全**：回调被调起时，结果**已经就绪**（ROS 是先等结果好、再调回调），所以 `get()` 是秒取、不阻塞。
- **主流程 `get()` 死锁**：`get()`/`wait()` 会阻塞当前线程；而「处理结果」这件事又要靠 executor 线程去做。若 executor 线程自己跑去 `get()` 傻等，就**自己堵死自己**——结果永远处理不了 → 死锁。这就是 [[E004 运行时-Service客户端等响应的死锁与executor冲突]]。

> **一句话结论：future 的 `get()` 只能在「结果已就绪的地方」用（回调里）；绝不能在主流程 `get()` 傻等。**

### 七、出现场景总结

| 场景 | future 出现的地方 |
|---|---|
| Service 客户端 `async_send_request` | 回调参数 `SharedFuture` |
| 参数客户端 `set_parameters` | 回调参数 `std::shared_future<std::vector<...>>` |
| Action 客户端 | 同样返回 future |
| E004 死锁 | `future.wait_for(...)` 在回调外傻等（反面教材） |

> **Note（连接 / 深化）：**
> - 连接：future 是「异步」的载体，和 [[N007 lambda表达式]] 的回调、[[N019 客户端实现 create_client]] 的异步请求是一套东西。
> - 深化：`get()` 语义上是「阻塞取结果」，所以它的**安全前提**永远是「结果已就绪」；判断不了就绪与否时，优先用回调（让 ROS 在就绪时叫你），而不是自己 `wait`。
> - 深化（本质）：**异步为什么总配回调**——因为异步函数一调用就**先 return 了**，此刻结果还没算出来、`return` 值拿不出结果；结果只能换个出口：约定回调，等结果好了回头调它、把结果塞进回调参数返回。future 就是这条「回头通知」链上的凭证。套两根轴（见 [[N042 同步异步与阻塞非阻塞]]）：`get()` = **同步阻塞**（原地等、线程挂起）、`wait_for(0)` 轮询 = **同步非阻塞**（反复查、空转）、回调 = **异步非阻塞**（事件到了才调你，ROS 的正统姿势）。

## 思考

（留白 —— `std::shared_future` 能多次 `get()`，那「多次 get 拿到的是同一份结果」这件事，在多线程里意味着什么？和 `std::future` 只能取一次相比，各适合什么场景？）

## 总结

**本质：** future 是异步操作的「结果凭证」——异步发起时结果没好，先给凭证，结果好了凭 `get()` 取；ROS2 的固定套路是「异步请求 + 回调（future 作参数）+ 回调里 `get()`」，因为回调时结果已就绪，而主流程 `get()` 会阻塞导致死锁（E004）。
**标签:** #语法知识 #C++语法 #future #异步async #回调Callback
