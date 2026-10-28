乌龟的名字是一个自由字符串，同时充当命名空间前缀、spawn 的入参、kill 的定位键。`turtle1` 是启动自带的默认龟，`turtle2` 是自动生成名，`A/B` 是自己起的语义名，结构上没有区别。追到后的「消失 + 重生」就是 kill + spawn 两次服务调用。

## 名字决定接口前缀

| 接口 | 名字叫 `B` 时 |
|---|---|
| 话题 | `/B/cmd_vel`、`/B/pose` |
| 服务 | `/B/set_pen`、`/B/teleport_absolute`、`/B/teleport_relative`、`/B/rotate_absolute` |

`turtlesim_node` 启动会自动 spawn 一只 `turtle1`，教程里满屏 `/turtle1/...` 只是因为它「自带」，不是保留字。

## spawn / kill

`/spawn`（`turtlesim_msgs/srv/Spawn`）：

```
float32 x
float32 y
float32 theta
string name        # 空则自动生成唯一名
---
string name        # 返回实际名字
```

`name` 是自由字符串，叫 `turtle2`、`B`、`alice` 都行；留空时自动生成 `turtle2`、`turtle3`… 并在响应里返回。

`/kill`（`turtlesim_msgs/srv/Kill`）请求 `string name`，按名字删龟；删掉后 `/名字/...` 所有接口当场消失。

| 名字 | 来源 |
|---|---|
| `turtle1` | 启动自动 spawn |
| `turtle2`、`turtle3`… | spawn 时 name 留空，自动生成 |
| `A`、`B` | 自己 spawn 时手动指定 |

「1、2」是默认/自动命名，「A、B」是课程设计里直接编码角色（chaser=A、runner=B）。两者都是字符串，唯一差别是名字本身，而名字会变成话题前缀。

## 名字是把三者串起来的键

```
spawn(name="B", x, y)   → 生出乌龟 B → /B/cmd_vel、/B/pose 出现
发 /B/cmd_vel           → 控制乌龟 B
kill(name="B")          → 删掉 B → /B/... 全部消失
```

重生两连击：

```bash
/kill(name="B")                    # 消失
/spawn(name="B", x=随机, y=随机)    # 新位置重生
```

kill + spawn 后画笔状态重置，所以要重新 `/B/set_pen`(off=1) 藏轨迹，见 [[turtle_chase_game_项目总结]]。

## 三个服务

| 服务 | 类型 | 请求 | 作用 |
|---|---|---|---|
| `/spawn` | `Spawn` | `x, y, theta, name` | 生一只新龟 |
| `/kill` | `Kill` | `name` | 删掉一只龟 |
| `/B/set_pen` | `SetPen` | `r, g, b, width, off` | `off=1` 关画笔 |

spawn / kill 是**全局**服务（名字在请求里）；set_pen 是**每只龟一个**（`/<名字>/set_pen`）。

## 参考节点 respawn_demo

流程：随机位置 spawn B → set_pen 藏轨迹 → 停 3s → kill B → 停 1s → 新位置 respawn → 重新 set_pen。

```bash
ros2 run turtlesim turtlesim_node
ros2 run turtle_chase respawn_demo
```

关键点：`async_send_request(req).get()` 会阻塞，若写在回调里会把 executor 堵死；参考节点把它丢进 `std::thread`，主线程照常 `rclcpp::spin` 收响应。最终版改用异步回调链，见 [[turtle_chase_game_项目总结]]。

## 三层名字别混

| 层级 | 例子 | 是什么 | 谁显示 |
|---|---|---|---|
| 节点名 | `Node("wandering_turtle")` | 自己程序/进程的身份 | `ros2 node list` |
| 乌龟名 | `B` / `turtle1` | turtlesim 进程里的一只龟 | spawn 的 `name` |
| 话题/服务名 | `/B/cmd_vel` | 乌龟名 + 固定接口名 | `ros2 topic list` |

在 `wandering_turtle.cpp` 里：节点叫 `wandering_turtle`，它控制的乌龟叫 `B`，两者靠 `/B/cmd_vel`、`/B/pose` 连起来。

```cpp
auto node = rclcpp::Node::make_shared("wandering_turtle");   // 节点名
spawn_request->name = "B";                                    // 乌龟名
```

两者互不相关：可以同名，也可以不同名，字符串相同也不代表同一个东西。

## 坑

- kill 掉的龟，其话题/服务立即消失，客户端要重新等待。
- spawn 同名龟可能失败或覆盖，重生前先 kill。
- `turtle1` 若不用，可以 kill 掉，或直接把其中一只复用成 `turtle1`。
- 节点名与乌龟名混用，`ros2 node list` 里找不到乌龟。

> PS：需要「瞬移」而非重生时用 `/B/teleport_absolute`，无空窗、不用重设 pen。

名字 = 命名空间前缀 + spawn 入参 + kill 定位键三合一；重生 = kill + spawn + 重设 set_pen，节点名与乌龟名是两套独立的名字。