Service 是请求-响应的一对一通信：客户端发请求，服务端处理并返回响应，一次性完成。`.srv` 两段编译出 Request / Response；服务端用 `create_service`，客户端用 `create_client` + `async_send_request`，等响应有三种方式。

## 概念

| | Topic | Service |
|---|---|---|
| 方向 | 单向发布→订阅 | 双向请求→响应 |
| 关系 | 多对多 | 一对一 |
| 持续性 | 持续 | 一次性 |
| 接口 | `.msg` | `.srv` |
| 用途 | 数据流 | 命令 / 查询 |

Service 是「拉」（客户端主动问），Topic 是「推」（发布者主动发）。

`.srv` 两段，`---` 分隔：

```
---
float64 x
float64 y
```

编译生成 `<包名>::srv::<服务名>`，含 `.Request` 和 `.Response`；`float64` 对应 C++ `double`。

## 服务端 create_service

```cpp
m_service = this->create_service<GetTargetPose>(
  "get_target_pose",
  std::bind(&TargetTurtle::handle_get_pose, this, _1, _2));

void handle_get_pose(const GetTargetPose::Request::SharedPtr request,
                     GetTargetPose::Response::SharedPtr response) {
  (void)request;              // 请求为空
  response->x = m_current_x;
  response->y = m_current_y;
}                             // 返回后响应自动发回
```

- 回调两个参数：读 `request`、写 `response`。
- 默认单线程 executor，处理完一个请求才轮到下一个。

## 客户端 create_client

核心 API 一个 `async_send_request`，两种重载：

```cpp
auto future = client->async_send_request(request);                // ① 返回 future
client->async_send_request(request, [](SharedFuture f) { ... });  // ② 带回调
```

**请求差异不在「怎么发」，而在「拿到 future 后怎么等」。**

### 方式 A：异步 + 回调（节点正在 spin）推荐

```cpp
m_client->async_send_request(request,
  [this](rclcpp::Client<T>::SharedFuture future) {
    auto response = future.get();
    this->move_towards(response->x, response->y);
  });
```

用于节点回调（定时器/订阅/服务回调）里调服务；完全不阻塞，响应到了 executor 自动调回调。

### 方式 B：spin_until_future_complete（main 里）

```cpp
auto future = m_client->async_send_request(request);
if (rclcpp::spin_until_future_complete(node, future, 1s) ==
    rclcpp::FutureReturnCode::SUCCESS) {
  auto response = future.get();
}
```

用于 `main` 里、节点未被 spin 接管、一次性调用；看似同步实为异步，不死锁。官方 add_two_ints 客户端标准写法。

### 方式 C：future.wait_for（独立线程）

```cpp
auto future = m_client->async_send_request(request);
if (future.wait_for(1s) == std::future_status::ready) {
  auto response = future.get();
}
```

用于自己 `std::thread` 起的线程；真阻塞、最简单。**在 executor 回调里用 = 死锁。**

### 决策树

```
我在 executor 线程里（节点被 spin 接管）？
├─ 是（在回调里）→ A：异步 + 回调
└─ 否（main / 独立线程）
   ├─ main 一次性调用 → B：spin_until_future_complete
   └─ 独立线程、想简单阻塞 → C：wait_for
```

三个坑：`wait_for` 在回调里阻塞 executor → 死锁；`spin_until_future_complete` 对已 spin 节点报 `already added to an executor`；节点正在 spin 时只能异步回调。详见 [[ROS2/Errors/Errors]] E004。

## 完整例子（方式 B）

```cpp
int main(int argc, char ** argv) {
  rclcpp::init(argc, argv);
  auto node = rclcpp::Node::make_shared("add_two_ints_client");
  auto client = node->create_client<example_interfaces::srv::AddTwoInts>("add_two_ints");
  client->wait_for_service();                    // 服务端没上线会一直等

  auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
  request->a = 3; request->b = 4;
  auto future = client->async_send_request(request);
  if (rclcpp::spin_until_future_complete(node, future) ==
      rclcpp::FutureReturnCode::SUCCESS)
    RCLCPP_INFO(node->get_logger(), "3 + 4 = %ld", future.get()->sum);

  rclcpp::shutdown();
}
```

## 坑

- 服务端没上线就发请求会失败，先 `wait_for_service`。
- 回调里用同步等待 = 死锁，见上。
- 服务端回调里做重活会拖慢后续请求。
- `.srv` 改了要重新构建，生成类才更新。

> PS：需要进度反馈或可取消，说明它是长任务，应该用 Action，见 [[N034 Action概念与action接口]]。

Service 是「推/拉」里的拉；服务端双参数回调读写 Request/Response，客户端发请求后按「是否在 executor 线程」选择异步回调、spin_until_future_complete 或 wait_for。