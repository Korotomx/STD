追击时算角度差 `angle_error = atan2(dy, dx) - m_theta`，结果可能超出 `[-π, π]`（目标在身后 -170°、自己朝 170°，差是 -340°）。直接乘增益会让海龟转大圈：本应左转 20°，却右转 340°。

一行归一化：

```cpp
double angle_error = std::atan2(
    std::sin(angle_to_target - m_theta),
    std::cos(angle_to_target - m_theta));
```

`atan2(y, x)` 的值域是 `(-π, π]`，能从 y/x 恢复唯一角度。`(sin d, cos d)` 丢掉了 d 的整圈信息（周期 2π），却保留方向，所以 `atan2(sin d, cos d)` 得到 d 落在主值区间的等价角，等价于 `std::remainder(d, 2π)`。

追击转向、机器人航向差等所有「算角度差」的地方都适用。

> PS：如果库提供 `std::remainder(d, 2π)` 也可直接用，语义相同。

任意角度差压回 `[-π, π]` 用 `atan2(sin d, cos d)`——sin/cos 丢圈数、atan2 还原主值。