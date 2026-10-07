---
tags:
  - 功能实现
  - Service服务
  - Client客户端
  - Callback回调
  - 异步async
---

# 客户端实现 create_client · 功能实现 · N019

**时间:** 2026-10-05 14:19 首次记录 · 2026-10-05 17:14 合并三种写法
**标签:** #功能实现 #Service服务 #Client客户端 #Callback回调 #异步async
**关联:** [[N009 Executor事件循环]] [[N017 Service概念与srv接口]] [[E004 运行时-Service客户端等响应的死锁与executor冲突]]

## 疑惑点

Service 客户端怎么写？发请求有哪些方式、各适用什么场景？

## 实际情况

### 1. 核心 API：一个 `async_send_request`，两种重载

```cpp
// ① 无回调 → 返回 future（自己想办法等）
auto future = client->async_send_request(request);   // std::future<Response>

// ② 带回调 → 响应到了自动调回调
client->async_send_request(request, [](SharedFuture f) { ... });
```

**「请求种类」的差异不在「怎么发」，而在「拿到 future 后怎么等」。**

### 2. 三种等响应的方式

**方式 A：异步 + 回调（节点正在 spin 时）✅ 推荐**

```cpp
client_->async_send_request(request,
  [this](Client<T>::SharedFuture future) {
    auto response = future.get();
    this->move_towards(response->x, response->y);
  });
```

- 场景：在**节点的回调里**（定时器 / 订阅 / 服务回调）调服务
- 特点：完全不阻塞，响应到了 executor 自动调回调

**方式 B：`spin_until_future_complete`（节点未 spin、main 里）**

```cpp
auto future = client->async_send_request(request);
if (rclcpp::spin_until_future_complete(node, future, 1s) ==
    rclcpp::FutureReturnCode::SUCCESS) {
  auto response = future.get();
}
```

- 场景：`main` 里、节点**未被 spin 接管**、一次性调用
- 特点：等待期间持续 spin，不会死锁；看似同步、实为异步
- **官方 add_two_ints 客户端标准写法**

**方式 C：`future.wait_for` / `wait`（独立线程）**

```cpp
auto future = client->async_send_request(request);
if (future.wait_for(1s) == std::future_status::ready) {
  auto response = future.get();
}
```

- 场景：**独立线程**（自己 `std::thread` 起的）
- 特点：真阻塞，最简单
- ⚠️ 在 executor 回调里用 = **死锁**

### 3. 决策树

```
我在 executor 线程里（节点被 spin 接管了）？
├─ 是（在回调里）→ 方式 A：异步 + 回调
└─ 否（main / 独立线程）
   ├─ main 里一次性调用 → 方式 B：spin_until_future_complete
   └─ 独立线程、想简单阻塞 → 方式 C：wait_for
```

### 4. 完整例子（add_two_ints 客户端，方式 B）

```cpp
#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"

int main(int argc, char ** argv) {
  rclcpp::init(argc, argv);
  auto node = rclcpp::Node::make_shared("add_two_ints_client");
  auto client = node->create_client<example_interfaces::srv::AddTwoInts>("add_two_ints");

  while (!client->wait_for_service(1s)) {        // 等服务上线
    if (!rclcpp::ok()) return 0;
    RCLCPP_INFO(node->get_logger(), "服务未上线，等待...");
  }

  auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
  request->a = 3;
  request->b = 4;

  auto future = client->async_send_request(request);
  if (rclcpp::spin_until_future_complete(node, future) ==
      rclcpp::FutureReturnCode::SUCCESS) {
    RCLCPP_INFO(node->get_logger(), "3 + 4 = %ld", future.get()->sum);
  }

  rclcpp::shutdown();
  return 0;
}
```

### 5. 三个坑（为什么方式 A 是「正统」）

- `future.wait_for()` 在回调里会**死锁**（阻塞 executor，响应回不来）
- `spin_until_future_complete()` 用于已 spin 节点报 `already added to an executor`
- 节点正在 spin（回调里）→ 只能**异步回调**

详见 [[E004 运行时-Service客户端等响应的死锁与executor冲突]]。

> **Note（连接 / 深化）：**
> - 连接：executor 单线程串行是死锁的根因，见 [[N009 Executor事件循环]]；多线程 executor 是另一条路，见 [[N023 main函数变厚 executor演进]]。
> - 深化：`wait_for_service` 处理「服务还没上线」的时序问题；服务端/客户端启动顺序无关，靠 DDS 发现自动对上。

## 思考

（留白 —— 若客户端先于服务端启动，`wait_for_service` 返回 false 时会怎样？我们的代码是「下个周期再试」）

## 总结

**本质：** 客户端 = `create_client` + `async_send_request`；等响应分三种——异步回调（spin 中）、`spin_until_future_complete`（main 里）、`wait_for`（独立线程），选哪种看「在不在 executor 线程里」。
**标签:** #功能实现 #Service服务 #Client客户端 #异步async
