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

4. **命名规则详解（和 .srv/.action 一致）。** 从 `.msg` 到 C++ 类型，四个层面的命名各有规则：

   | 层面 | 规则 | 例子（TurtleStatus.msg） |
   |---|---|---|
   | `.msg` 文件名 | PascalCase（大驼峰） | `TurtleStatus.msg` |
   | 生成的头文件名 | snake_case（小写下划线） | `turtle_status.hpp` |
   | C++ 类名 | PascalCase（和 .msg 一致） | `TurtleStatus` |
   | C++ 命名空间 | `包名::类型目录::类名` | `turtle_status::msg::TurtleStatus` |

   字段名是 snake_case：`.msg` 里写 `linear_vel`，成员变量就是 `msg->linear_vel`。

   - **头文件路径为什么有两个包名：**

     ```text
     install/turtle_status/include/turtle_status/turtle_status/msg/turtle_status.hpp
                              └──────┬──────┘└──────┬──────┘└─┬─┘└──────┬──────┘
                                第①层包名     第②层包名   类型   头文件
     ```

     第①层 `turtle_status/`（紧跟 include 后）= ament 安装布局，`include/<包名>/` 是导出给使用者的 include 根；第②层 `turtle_status/` = 对应命名空间第一层（`namespace turtle_status`），目录跟着命名空间走；`msg/` = 命名空间第二层（srv 就是 `srv/`、action 就是 `action/`）。**第一个是「安装/导出约定」，第二个是「命名空间的目录映射」，两者撞名纯属巧合（都叫包名）。**

   - **include 为什么只写一个包名：**

     ```cpp
     #include "turtle_status/msg/turtle_status.hpp"   // 只写一个 turtle_status
     ```

     因为编译器的 include 搜索根是 `install/turtle_status/include/turtle_status/`（多一层包名），在这个根下拼 `turtle_status/msg/...` 才正好命中 `.../turtle_status/turtle_status/msg/...`。这个「多一层」的 include 根由 CMake target 导出（`${包名}_TARGETS` / `rosidl_get_typesupport_target`）。

   - **生成的 `.hpp` 是「汇总头文件」**，自己不定义类，只 include detail 里四个文件（`__struct` 结构 / `__builder` / `__traits` / `__type_support` 序列化）。真正的结构体在 `detail/turtle_status__struct.hpp`：

     ```cpp
     namespace turtle_status {
     namespace msg {
     struct TurtleStatus_ {               // ← 内部名带下划线后缀
       std::string name;
       float x, y, theta, linear_vel;
       bool alive;
     };
     using TurtleStatus = TurtleStatus_;  // ← 公开名不带下划线（别名）
     }  // namespace msg
     }  // namespace turtle_status
     ```

     内部 struct 叫 `TurtleStatus_`（下划线后缀），最后 `using TurtleStatus = TurtleStatus_;` 暴露成你用的 `TurtleStatus`——「内部名避嫌、公开名整洁」。

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
