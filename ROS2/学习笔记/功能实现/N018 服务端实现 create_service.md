---
tags:
  - 功能实现
  - Service服务
  - Server服务端
  - Callback回调
---

# 服务端实现 create_service · 功能实现 · N018

**时间:** 2026-10-05 14:19
**标签:** #功能实现 #Service服务 #Server服务端 #Callback回调
**关联:** [[N010 订阅者与回调参数]] [[N017 Service概念与srv接口]]

## 疑惑点

Service 服务端怎么写？

## 实际情况

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
4. **同步处理**：默认单线程 executor，处理完一个请求才轮到下一个。

> **Note（连接 / 深化）：**
> - 连接：回调机制、`std::bind` 见 [[N010 订阅者与回调参数]]。
> - 深化：服务回调是「同步」的——一个请求没处理完，后续请求只能排队（若服务耗时会影响响应延迟）。

## 思考

（留白 —— 如果服务回调里 `sleep` 10 秒，连续调两次会怎样？）

## 总结

**本质：** 服务端 = `create_service` + 双参数回调（请求/响应）；读 request、写 response，返回即回复。
**标签:** #功能实现 #Service服务 #Server服务端
