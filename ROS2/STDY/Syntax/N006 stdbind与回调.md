成员函数指针不含对象信息，不能独立调用；`std::bind` 把「成员函数 + this」打包成 callable。`_1` 是位置占位符，负责把框架传入的消息接到回调形参上。lambda 是同一件事的更直观写法。

## 为什么需要 bind

`create_wall_timer(周期, 回调)` 需要一个能独立调用（`()`）的东西，即 **callable**：函数指针、函数对象、lambda 都算。

成员函数隐含 `this`：

```cpp
this->timer_callback();          // ✅ this 就是对象
&Talker::timer_callback;         // 只是函数标识，不含「哪个对象」
(obj.*fp)();                     // 成员函数指针必须带上对象
```

`create_wall_timer` 不在类内部、没有 `this`，所以必须把对象一起交过去：

```cpp
std::bind(&Talker::timer_callback, this)
// 等价于「到点执行 this->timer_callback()」
```

`std::bind` 返回的是**函数对象（functor）**，内部存 this + 成员函数指针、重载 `operator()`，不是函数指针。多个对象调同一方法时，方法代码只有一份，数据（`this` 指向的成员）各一份。

## 占位符 `_1` 与消息流入

订阅回调要接收消息，而消息是框架收到消息时自动传进来的：

```cpp
using std::placeholders::_1;
create_subscription<Msg>("topic", 10, std::bind(&Listener::topic_cb, this, _1));
```

bind 的两类参数：

| 类型 | 例子 | 含义 |
|---|---|---|
| 绑死 | `this` | bind 当下确定，之后不变 |
| 占位符 | `_1` | 先空着，调用时用实参填 |

内部大致是：

```cpp
struct Binder {
  void operator()(const Msg & incoming) {
    this->topic_cb(incoming);     // 实参填到 _1 的位置
  }
};
```

规则：`bind(&f, this, _1)` 产出的 callable 需要 1 个参数；`_1` 的个数 = 回调需要框架传入的参数个数。timer 回调无参，所以没有 `_1`；服务回调有两个参数，写 `_1, _2`。

**`_1` 不是消息本身**，只是「第 1 个实参放这里」的标记。

完整链路：

```
publish(msg)
  → rclcpp → rcl → rmw → DDS 序列化/发送
  → 对端反序列化成 Msg 对象
  → rclcpp 调用 callable: Binder(msg)
  → this->topic_cb(msg)
```

漏写 `_1`（`bind(&topic_cb, this)`）会编译报错：回调需要 1 个参数，callable 没有参数来源。

## lambda：更直观的等价写法

```cpp
// bind
std::bind(&Talker::timer_callback, this)

// lambda
[this]() { this->timer_callback(); }
```

语法：`[捕获列表](参数列表) -> 返回类型 { 函数体 }`，返回类型可省略。

| 捕获 | 含义 |
|---|---|
| `[]` | 不捕获 |
| `[this]` | 捕获 this，可访问成员 |
| `[=]` | 按值捕获用到的变量（拷贝） |
| `[&]` | 按引用捕获用到的变量 |
| `[x]` / `[&x]` | 按值 / 按引用捕获 x |

`[this]` 是「把当前对象的 this 借进函数体」，之后可直接写 `apply_color()`、`m_timer`（实际是 `this->...`）。没有 `[this]` 就用不了成员。

lambda 也能带参数，参数由调用方塞进来：

```cpp
m_timer = this->create_wall_timer(2s, [this]() {       // 无参，定时器触发
  apply_color();
  m_timer->cancel();
});

m_param_client->set_parameters({...},
  [this](std::shared_future<...> fut) {                // 有参，结果回来时 ROS 传入
    auto results = fut.get();
  });
```

回调的「参数」不是你填的，是 ROS 在触发时传入的；`fut` 的语义见 [[N009 Executor事件循环]]。

## 坑

- `[=]` 拷贝捕获：对象大时浪费；`[&]` 引用捕获：lambda 活得比变量久会悬空。
- 回调里改成员必须捕获 `this`，捕获局部变量副本不会改到原值。
- 成员函数指针和继承无关，本质是「成员函数 vs 自由函数」的区别。
- `_1` 数量与回调形参数量不匹配会编译失败。

> PS：C++11 之后优先 lambda；需要复用或存进容器时再用 `std::bind`。

bind 补齐成员函数缺的 `this`，`_1` 声明「第几个实参填到第几个形参」；lambda 用捕获列表做到同一件事，参数同样由框架在触发时传入。