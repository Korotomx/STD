---
tags:
  - 功能实现
  - turtlesim
  - Service服务
  - 命名Naming
  - spawn
  - kill
---

# 海龟命名与 spawn/kill · 功能实现 · N050

**时间:** 2026-10-14 12:33
**标签:** #功能实现 #turtlesim #Service服务 #命名Naming #spawn #kill
**关联:** [[N021 控制海龟运动]] [[N049 双龟追逐进阶任务参考与伪代码]] [[N020 turtle_chase小海龟追击项目架构与代码拆解]] [[E003 构建依赖-turtlesim消息拆到turtlesim_msgs]]

## 疑惑点

「这个乌龟的名字是有什么限定吗？一会 A、B，一会 1、2 的，和 spawn、kill 之类的又有什么关系？」

## 实际情况

### 1. 乌龟「名字」的本质 = 命名空间前缀

turtlesim 里每只乌龟用**一个字符串名字**标识。这个名字决定它**所有接口**的命名空间前缀：

| 接口 | 名字叫 `B` 时 |
| ---- | ---- |
| 话题 | `/B/cmd_vel`、`/B/pose` |
| 服务 | `/B/set_pen`、`/B/teleport_absolute`、`/B/teleport_relative`、`/B/rotate_absolute` |

`turtlesim_node` 启动时会**自动 spawn 一只默认乌龟 `turtle1`**，所以教程里满屏 `/turtle1/cmd_vel`——它只是「自动生成的那只」，不是什么特殊保留字。

### 2. spawn —— 新乌龟从哪来

`/spawn` 服务（`turtlesim_msgs/srv/Spawn`）负责「生」：

```
float32 x          # 出生 x
float32 y          # 出生 y
float32 theta      # 出生朝向
string name        # 名字。Optional: 空则自动生成唯一名并返回
---
string name        # 响应: 实际名字(空 name 时回自动生成的)
```

- `name` 是**自由字符串**，叫 `turtle2`、`B`、`alice` 都行，没有命名规则限制。
- `name` 留空时 turtlesim 自动生成唯一名（递增 `turtle2`、`turtle3`…），响应里返回。

### 3. kill —— 按名字删

`/kill` 服务（`turtlesim_msgs/srv/Kill`）请求 `string name`，按名字删掉一只乌龟。删掉后 `/名字/...` 所有接口**当场消失**。

### 4. 「1、2」vs「A、B」—— 结构上没区别，纯命名习惯

| 名字 | 哪来的 |
| ---- | ---- |
| `turtle1` | turtlesim_node 启动自动 spawn 的默认名 |
| `turtle2`、`turtle3`… | spawn 时 `name` 留空，自动生成的唯一名 |
| `A`、`B` | 自己 spawn 时手动给的、更语义化的名字 |

「1、2」是默认/自动命名（官方教程用的）；「A、B」是你在课程设计里**自己起**的名字，直接编码角色（chaser=A、runner=B）。两者都是字符串，没有任何结构区别——唯一差别就是这个名字本身，而它变成话题前缀。

### 5. 名字 = 把 spawn / kill / 话题串起来的「键」

```
spawn(name="B", x, y)   ──►  生出乌龟 B  ──►  /B/cmd_vel、/B/pose… 出现
发 /B/cmd_vel           ──►  控制乌龟 B(不是别的乌龟)
kill(name="B")          ──►  删掉乌龟 B  ──►  /B/... 全部消失
```

所以进阶任务里的「B 在原位消失、新随机位置重生」就是两连击：

```
/kill(name="B")                          # 消失
/spawn(name="B", x=随机, y=随机)          # 新位置重生
```

注意 kill+spawn 后海龟的**笔迹状态会重置**，所以要重设 `/B/set_pen`(off=1) 藏轨迹（见 [[N049 双龟追逐进阶任务参考与伪代码]]）。

### 6. 三层「名字」别混（关键）

三个不同层级，最容易搞混：

| 层级 | 例子 | 是什么 | 谁显示 |
| ---- | ---- | ---- | ---- |
| **节点名** | `Node("wandering_turtle")` | 你写的程序/进程的身份 | `ros2 node list` |
| **乌龟名** | `B` / `A` / `turtle1` | turtlesim 内部的一只乌龟，spawn 时定 | spawn 时你传的 `name` |
| **话题/服务名** | `/B/cmd_vel` | `<乌龟名>` + `/` + 固定接口名，不是独立的第三个名字 | `ros2 topic list` |

在你的 `wandering_turtle.cpp` 里：
- **节点**叫 `wandering_turtle`（跑在你自己的可执行文件里）
- 它控制的**乌龟**叫 `B`（活在 `turtlesim_node` 进程里）
- 两者靠话题 `/B/cmd_vel`、`/B/pose` 连起来

> **Note（连接 / 深化）：**
> - 连接：`cmd_vel`/`pose` 都是 Topic 持续流，乌龟怎么被驱动见 [[N021 控制海龟运动]]；`spawn`/`kill`/`set_pen` 都是 Service 一次性请求。
> - 深化：`turtle1` 是启动自带的一只，若你的项目只需要 A/B 两只，`turtle1` 就是「多余的一只」——要么 `kill turtle1`，要么干脆把其中一只乌龟复用成 `turtle1`。

### 7. spawn 的名字 ≠ 节点名（澄清「自带」）

容易把「spawn 的名字」当成「spawn 自带一个名字」，其实不是。**整个系统里只有两处「自带」名字：**

| 谁 | 名字 | 怎么来的 |
| ---- | ---- | ---- |
| turtlesim_node 启动 | `turtle1` | 自动 spawn，你啥也不用干 |
| spawn 的 `name` 留空 | `turtle2`、`turtle3`… | 自动生成唯一名 |

**其他名字全是你自己取的，而且取在完全不同的两个地方：**

```cpp
// ① 节点名 —— 在「你自己的程序」里，构造节点时取
auto node = rclcpp::Node::make_shared("wandering_turtle");   // ← 这是节点名

// ② 乌龟名 —— 调 spawn 服务时，作为请求字段传
spawn(name="B", x=..., y=...);   // ← 这是乌龟名（turtlesim 进程里的那只）
```

两者**互不相关**：可以同名（节点叫 `B`、乌龟也叫 `B`），也可以不同名（节点叫 `wandering_turtle`、乌龟叫 `B`）——字符串碰巧一样也不代表是同一个东西，它们分别在两个进程、两个命名空间里。

## 思考

（留白 —— 如果 spawn 时 `name` 留空，turtlesim 返回的名字靠什么保证唯一？连续两次 `ros2 service call /spawn` 观察返回的 name 和 `ros2 topic list` 的变化？）

## 总结

**本质：** 乌龟的名字是一个**自由字符串**，它同时是「命名空间前缀」「spawn 的入参」「kill 的定位键」三合一；`1/2` 是自动/默认命名，`A/B` 是自己起名，结构无差别。进阶任务的「重生」就是 `kill(name)` + `spawn(name, 新坐标)` 两次服务调用。
**标签:** #功能实现 #turtlesim #Service服务 #命名Naming #spawn #kill
