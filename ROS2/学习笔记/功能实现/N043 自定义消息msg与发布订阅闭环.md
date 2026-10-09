---
tags:
  - 功能实现
  - 消息类型
  - 接口Interface
  - Topic话题
  - Publisher发布者
  - Subscriber订阅者
---

# 自定义消息 .msg 与发布订阅闭环 · 功能实现 · N043

**时间:** 2026-10-09 21:26
**标签:** #功能实现 #消息类型 #接口Interface #Topic话题 #Publisher发布者 #Subscriber订阅者
**关联:** [[N017 Service概念与srv接口]] [[N034 Action概念与action接口]] [[N022 geometry_msgs几何消息包]]

## 疑惑点

ROS2 自带消息（Twist / Pose…）是通用的，但我的项目有自己的数据结构怎么办？能不能像写 .srv / .action 那样，自己定义一个消息格式，然后像内置消息一样发布 / 订阅？

## 实际情况

1. **动机：内置消息不够用。** 内置消息是「通用最小集」——Twist 只有速度、Pose 只有位姿。当我要传「一只海龟的完整状态」：名字 + 坐标 + 朝向 + 速度 + 死活，就得自己定义一包字段。这就是自定义消息 `.msg`。

2. **`.msg` 文件 = 一包字段。** 每行「类型 字段名」，和 .srv / .action 里的字段写法完全一样：

   ```msg
   # msg/TurtleStatus.msg
   string  name         # 海龟名字
   float32 x            # 世界坐标 x
   float32 y            # 世界坐标 y
   float32 theta        # 朝向角（弧度）
   float32 linear_vel   # 当前线速度
   bool    alive        # 是否存活
   ```

   类型可以是内置（string/float32/bool/int32…），也可以是**另一个消息**（嵌套）。

3. **编译时自动生成类。** 在 CMakeLists 里把 .msg 交给 rosidl，编译后自动产出 C++/Python 类：

   ```cmake
   rosidl_generate_interfaces(${PROJECT_NAME}
     "msg/TurtleStatus.msg"
   )
   ```

   生成的头文件 `turtle_status/msg/turtle_status.hpp`，类名 `turtle_status::msg::TurtleStatus`。用法和内置消息**一模一样**（N022 里怎么用 Twist/Pose，这里就怎么用）：

   ```cpp
   publisher_ = this->create_publisher<turtle_status::msg::TurtleStatus>("/turtle1/status", 10);
   auto status = turtle_status::msg::TurtleStatus();   // 像 Twist() 一样实例化
   status.x = msg->x;
   ```

4. **命名规则（和 .srv/.action 一致）：** `.msg` 文件名大驼峰 `TurtleStatus.msg` → 类名 `TurtleStatus`；字段名 snake_case `linear_vel` → 成员变量 `msg->linear_vel`。

5. **接口在包内（dev_ws 惯例）vs 独立接口包（ros2_ws 惯例）。** 两种组织方式都合法：

   | | 独立接口包（ros2_ws） | 接口在包内（dev_ws） |
   |---|---|---|
   | 接口放哪 | 单独的 turtle_demo_interfaces 包 | 直接放业务包里 |
   | 业务包怎么用 | find_package + 链接 `${..._TARGETS}` | 同包 rosidl_get_typesupport_target + 链接 `${cpp_typesupport_target}` |
   | 生成类 | `turtle_demo_interfaces::msg::...` | `turtle_status::msg::...` |

   dev_ws 选择「接口和用它的节点同包」，所以 CMake 里多一步「取 typesupport 目标」：

   ```cmake
   # 生成 .msg 后，把负责序列化/类型信息的 typesupport 库取出来，节点链接它
   rosidl_get_typesupport_target(cpp_typesupport_target ${PROJECT_NAME} "rosidl_typesupport_cpp")
   target_link_libraries(status_reporter ... ${cpp_typesupport_target})
   ```

6. **发布 / 订阅闭环（项目实战 turtle_status 包）。** 通信链路：

   ```text
   (turtlesim) ──Pose──▶ [/turtle1/pose] ──▶ (status_reporter) ──TurtleStatus──▶ [/turtle1/status] ──▶ (status_watcher)
   ```

   ```mermaid
   graph LR
     T((turtlesim)) -->|Pose| P[/turtle1/pose/]
     P --> R((status_reporter))
     R -->|TurtleStatus| S[/turtle1/status/]
     S --> W((status_watcher))
   ```

   - **status_reporter（发布端）**：订阅原生 Pose，回调里把位姿「翻译」成 TurtleStatus 发布——自定义消息最典型的用法就是这种「翻译 / 重打包」：

     ```cpp
     void pose_callback(const turtlesim_msgs::msg::Pose::SharedPtr msg) {
       auto status = turtle_status::msg::TurtleStatus();
       status.name = turtle_name_;
       status.x = msg->x;
       status.linear_vel = msg->linear_velocity;   // ← 字段重命名：velocity → vel
       status.alive = true;
       publisher_->publish(status);
     }
     ```

   - **status_watcher（订阅端）**：就是普通订阅，和 project1 的 listener 一个套路。

7. **三种接口对比（补齐接口全景）。** 到这一篇，msg/srv/action 三种自定义接口就齐了：

   | 接口 | 文件 | 段数 | 方向 | 生成类 |
   |---|---|---|---|---|
   | 消息 .msg | TurtleStatus.msg | 1 段 | 单向 pub→sub | msg::TurtleStatus |
   | 服务 .srv | TeleportTurtle.srv | 2 段(---) | 一问一答 | srv::TeleportTurtle |
   | 动作 .action | Patrol.action | 3 段(---×2) | 带反馈长任务 | action::Patrol |

## 思考

（留白 —— 如果 .msg 里定义一个字段类型是另一个自定义消息，CMake 里要不要额外声明依赖？生成类的头文件路径里为什么会有两个包名 `turtle_status/turtle_status/msg/...`？）

## 总结

**本质：** 自定义消息 = 自己写一个 `.msg` 文件（一包字段），CMake 里交给 `rosidl_generate_interfaces` 自动生成 C++/Python 类，然后像内置消息一样发布/订阅。dev_ws 惯例是把接口和节点放同一个包（`rosidl_get_typesupport_target` 链接），ros2_ws 惯例是独立接口包（find_package 链接）。三种接口里 .msg 是单向的，.srv 一问一答、.action 带反馈，至此接口体系齐全。
**标签:** #功能实现 #消息类型 #接口Interface #Topic话题
