---
tags:
  - 语法知识
  - C++语法
  - 数学Math
  - 角度Angle
---

# 角度归一化 atan2(sin,cos) · 语法知识 · N053

**时间:** 2026-10-14 23:30
**标签:** #语法知识 #C++语法 #数学Math #角度Angle
**关联:** [[N020 turtle_chase小海龟追击项目架构与代码拆解]] [[N052 双龟追逐三节点Action实现]]

## 疑惑点

chaser 里算「朝向目标的角度差」：

```cpp
double angle_to_target = std::atan2(dy, dx);   // 目标相对自己的方位角
double angle_error = angle_to_target - m_theta;
```

问题：`angle_error` 可能超出 `[-π, π]`（比如目标在身后 -170°，自己朝向 170°，差是 -340°）。直接拿它乘 K 当角速度，乌龟会「转大圈」——本应左转 20° 却右转 340°。

## 实际情况

归一化到 `[-π, π]` 的写法：

```cpp
double angle_error = std::atan2(
    std::sin(angle_to_target - m_theta),
    std::cos(angle_to_target - m_theta));
```

把「角度差」的 sin / cos 作为 `atan2(y, x)` 的两个参数。

## 原理

`atan2(y, x)` 的返回值域是 `(-π, π]`，它能从 y/x 恢复出唯一的角度。而 `(sin d, cos d)` 丢掉了 d 的**整圈信息**（sin/cos 周期 2π），却保留了 d 的方向——所以 `atan2(sin d, cos d)` 得到的就是 d 落在主值区间 `(-π, π]` 里的那个等价角，等价于 `std::remainder(d, 2π)`。

## 总结

任意角度差想压回 `[-π, π]`，用 `atan2(sin(d), cos(d))` 一行搞定；本质是「sin/cos 丢圈数、atan2 还原主值」。追击转向、机器人航向差等所有「算角度差」的地方都用得上。
