---
tags:
  - 功能实现
  - Service服务
  - Topic话题
  - 接口Interface
  - Server服务端
  - Client客户端
  - Callback回调
  - 异步async
---

# Service 通信全解（概念 / 服务端 / 客户端）· 功能实现 · N017

**时间:** 2026-10-05 14:19 首次记录 · 2026-10-20 合并 N018/N019（服务端 / 客户端）
**标签:** #功能实现 #Service服务 #Topic话题 #接口Interface #Server服务端 #Client客户端 #Callback回调 #异步async
**关联:** [[N001 节点基础书写骨架]] [[N009 Executor事件循环]] [[N010 订阅者与回调参数]] [[N011 ROS2分层架构]] [[E004 运行时-Service客户端等响应的死锁与executor冲突]]

## 疑惑点

Service 是什么、和 Topic 有啥区别？服务端 / 客户端分别怎么写？客户端发请求有哪些方式、各适用什么场景？

## 实际情况

### 1. 概念：Service = 请求-响应（原 N017）

1. **Service = 请求-响应**：客户端发请求，服务端处理返回响应，一来一回、一对一、一次性。
2. **vs Topic**：

   | | Topic | Service |
   |---|---|---|
   | 方向 | 单向(发布→订阅) | 双向(请求→响应) |
   | 关系 | 多对多 | 一对一 |
   | 持续性 | 持续 | 一次性 |
   | 接口 | .msg | .srv |
   | 用途 | 数据流 | 命令/查询 |

3. **类比**：Topic = 广播电台（一直播谁爱听谁听）；Service = 打电话（拨号→应答→挂断）。
4. **.srv 格式**：两段，请求 `---` 响应：

   ```
   # 请求（可为空）
   ---
   float64 x
   float64 y
   ```

5. **编译生成**：`<包名>::srv::<服务名>` 类型，含 `.Request` 和 `.Response` 两个子结构；`float64` → C++ `double`。

### 2. 服务端：create_service（原 N018）

1. **创建**：`create_service<类型>("服务名", callback)` —— 类似 `create_subscription`。
2. **回调两个参数**（和订阅回调一个参数不同）：

   ```cpp
   void callback(const Request::SharedPtr  request,   // 读请求
                 Response::SharedPtr       response)  // 写响应
   {
     (void)request;             // 本项目请求为空，暂不用
     response->x = current_x_;  // 填充响应
     response->y = current_y_;
   }
   ```

3. **读请求、写响应**：回调返回后，响应**自动发回**客户端。
4. **同步处理**：默认单线程 executor，处理完一个请求才轮到下一个（若服务耗时会影响响应延迟）。

### 3. 客户端：create_client + 三种等响应（原 N019）

核心 API 一个 `async_send_request`、两种重载：

```cpp
auto future = client->async_send_request(request);                     // ① 无回调 → 返回 future
client->async_send_request(request, [](SharedFuture f) { ... });       // ② 带回调
```

**「请求种类的差异不在「怎么发」，而在「拿到 future 后怎么等」。**

- **方式 A：异步 + 回调（节点正在 spin 时）✅ 推荐**

  ```cpp
  client_->async_send_request(request,
    [this](Client<T>::SharedFuture future) {
      auto response = future.get();
      this->move_towards(response->x, response->y);
    });
  ```
  场景：在节点的回调里（定时器 / 订阅 / 服务回调）调服务；完全不阻塞，响应到了 executor 自动调回调。

- **方式 B：`spin_until_future_complete`（节点未 spin、main 里）**

  ```cpp
  auto future = client->async_send_request(request);
  if (rclcpp::spin_until_future_complete(node, future, 1s) ==
      rclcpp::FutureReturnCode::SUCCESS) {
    auto response = future.get();
  }
  ```
  场景：`main` 里、节点未被 spin 接管、一次性调用；看似同步、实为异步，不会死锁；官方 add_two_ints 客户端标准写法。

- **方式 C：`future.wait_for` / `wait`（独立线程）**

  ```cpp
  auto future = client->async_send_request(request);
  if (future.wait_for(1s) == std::future_status::ready) {
    auto response = future.get();
  }
  ```
  场景：独立线程（自己 `std::thread` 起的），真阻塞、最简单；⚠️ 在 executor 回调里用 = **死锁**。

**决策树**：

```
我在 executor 线程里（节点被 spin 接管了）？
├─ 是（在回调里）→ 方式 A：异步 + 回调
└─ 否（main / 独立线程）
   ├─ main 里一次性调用 → 方式 B：spin_until_future_complete
   └─ 独立线程、想简单阻塞 → 方式 C：wait_for
```

**三个坑**（为什么方式 A 是「正统」）：
- `future.wait_for()` 在回调里会**死锁**（阻塞 executor，响应回不来）
- `spin_until_future_complete()` 用于已 spin 节点报 `already added to an executor`
- 节点正在 spin（回调里）→ 只能**异步回调**

详见 [[E004 运行时-Service客户端等响应的死锁与executor冲突]]。

### 4. 完整例子（add_two_ints 客户端，方式 B，原 N019）

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

> **Note（连接 / 深化）：**
> - 连接：接口类型由 rosidl 生成，见 [[N011 ROS2分层架构]]、[[N014 从cpp到可执行文件]]；回调机制 `std::bind` 见 [[N010 订阅者与回调参数]]；executor 单线程串行是死锁根因，见 [[N009 Executor事件循环]]、[[N023 main函数变厚 executor演进]]（多线程 executor 是另一条路）。
> - 深化：Service 是「拉」（客户端主动调），Topic 是「推」（发布者主动发）；`wait_for_service` 处理「服务还没上线」的时序问题，靠 DDS 发现自动对上。

## 思考

（留白 —— 「周期性查位置」用 Service 是轮询，若改 Topic 就是推送，两者实时性取舍？）

## 总结

**本质：** Service 是请求-响应的双向通信，`.srv` 两段编译出 Request/Response。服务端 = `create_service` + 双参数回调（读 request / 写 response）；客户端 = `create_client` + `async_send_request`，等响应分三种——异步回调（spin 中）、`spin_until_future_complete`（main 里）、`wait_for`（独立线程），选哪种看「在不在 executor 线程里」。
**标签:** #功能实现 #Service服务 #Topic话题 #接口Interface #Server服务端 #Client客户端 #异步async
