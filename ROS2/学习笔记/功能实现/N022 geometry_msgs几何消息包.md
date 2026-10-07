---
tags:
  - 功能实现
  - 消息类型
  - geometry_msgs
  - 参考Reference
---

# geometry_msgs 几何消息包 · 功能实现 · N022

**时间:** 2026-10-05 15:47
**标签:** #功能实现 #消息类型 #geometry_msgs #参考Reference
**关联:** [[N012 ROS2的库与职责]] [[N021 控制海龟运动]] [[N020 turtle_chase小海龟追击项目架构与代码拆解]]

## 疑惑点

geometry_msgs 包里有什么？有哪些常用的消息类型？命名有什么规律？

## 实际情况

### 1. 是什么

`geometry_msgs` = ROS 2 的**几何消息标准包**，用统一的消息类型描述「空间中的位置、朝向、速度、力」，几乎所有机器人项目的基础依赖。共 32 个消息。

### 2. 分 6 大类

| 类别 | 消息 | 用途 |
|---|---|---|
| 基础积木 | `Point` / `Vector3` / `Quaternion` / `Point32` | 点 / 向量 / 四元数(朝向) |
| 位姿 | `Pose` / `PoseStamped` / `PoseArray` / `PoseWithCovariance` | 位置 + 朝向 |
| 运动 | `Twist` / `TwistStamped` / `Accel` / `Wrench` | 速度 / 加速度 / 力 |
| 变换 | `Transform` / `TransformStamped` | 坐标系变换(tf 用) |
| 形状 | `Polygon` / `PolygonStamped` | 多边形区域 |
| 惯性 | `Inertia` | 惯性张量 |

### 3. 命名规律(最实用)

- **裸类型**：`Pose` / `Twist` / `Point` —— 纯几何量
- **`Stamped` 后缀** = 加 `Header`（时间戳 + 坐标系 `frame_id`）：`PoseStamped` / `TwistStamped` / `PointStamped` / `TransformStamped`
- **`WithCovariance` 后缀** = 加协方差矩阵（表示不确定性）：`PoseWithCovariance` / `TwistWithCovariance`

**带 `Stamped` 的才「挂在某个坐标系下」，是 tf / 导航里最常用的。**

### 4. 重点：Twist 与 Pose

**Twist（速度）**：

```
Vector3 linear    # 线速度（米/秒）
Vector3 angular   # 角速度（弧度/秒）
```

- 2D 差速轮 / 海龟只用 `linear.x`（前进）+ `angular.z`（转向）；3D 才用全 6 自由度。

**Pose + Quaternion（位姿）**：

```
Point      position     # x, y, z
Quaternion orientation  # x, y, z, w
```

- 朝向用**四元数**而非欧拉角，因为欧拉角有「万向锁」，四元数没有且计算稳定。
- 2D 简化：绕 z 轴转 θ → `z = sin(θ/2), w = cos(θ/2)`。

### 5. 易混点：海龟 Pose ≠ geometry_msgs Pose

- `turtlesim_msgs/msg/Pose`：`float32 x, y, theta`（2D + 欧拉角，简化版）
- `geometry_msgs/msg/Pose`：`Point position + Quaternion orientation`（3D + 四元数，通用版）

两者是**不同的类型**，别搞混。

### 6. 实战最常用 5 个

| 消息 | 场景 |
|---|---|
| `PoseStamped` | 定位、导航目标、避障 |
| `Twist` | 速度控制 |
| `TransformStamped` | tf 坐标变换 |
| `Point` | 目标点、点云点 |
| `Quaternion` | 3D 朝向 |

> **Note（连接 / 深化）：**
> - 连接：geometry_msgs 是「消息接口包」（只有 .msg 定义、无逻辑），见 [[N012 ROS2的库与职责]]；我们控制海龟用的 Twist 见 [[N021 控制海龟运动]]。
> - 深化：后续 `tf`（坐标变换）和 `nav2`（导航）大量依赖 `TransformStamped` / `PoseStamped`。

## 思考

（留白 —— `Pose` 用四元数表示朝向，2D 下绕 z 转 90° 的四元数是多少？验证 `z = sin(π/4), w = cos(π/4)`）

## 总结

**本质：** geometry_msgs 是一套几何消息标准包；命名规律（Stamped=带坐标系、WithCovariance=带不确定性）比记忆单个消息更重要；最常用 Twist（速度）、Pose/Quaternion（位姿）、TransformStamped（变换）。
**标签:** #功能实现 #消息类型 #geometry_msgs
