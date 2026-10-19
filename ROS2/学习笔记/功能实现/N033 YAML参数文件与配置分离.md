---
tags:
  - 功能实现
  - Parameter参数
  - YAML配置
  - launch启动
  - 命令行CLI
---

# YAML 参数文件：参数配置与代码分离 · 功能实现 · N033

**时间:** 2026-10-07 15:18
**标签:** #功能实现 #Parameter参数 #YAML配置 #launch启动 #命令行CLI
**关联:** [[N024 参数概念与四大通信机制全景]] [[N025 参数的声明读写与命令行工具]] [[N029 turtle_painter参数中转节点拆解]]

## 疑惑点

参数已经能用 `declare_parameter` 声明、`ros2 param set` 修改了，为什么还要 YAML？参数写死在代码/launch 里有什么问题？YAML 文件长什么样、怎么加载、和之前学的 `ros2 param dump / load` 是什么关系？

## 实际情况

1. **动机：配置与代码分离。** 参数如果写死在代码（`declare_parameter("background_r", 30)`）或 launch 内联字典里，改一个值就要改代码 / 改 launch。YAML 把「参数值」独立成配置文件——改配置不动代码，同一个节点也能用不同 YAML 跑出不同行为。

2. **YAML 文件格式：必须套「节点名 → `ros__parameters`」这一层。** ROS 2 的 YAML 参数文件不是裸键值对，顶层键是**节点名**（不是参数名），下面固定跟一个 `ros__parameters:` 子键，真正的参数才写在它下面：

   ```yaml
   # params.yaml —— 顶层键 = 节点名
   turtle_painter:
     ros__parameters:
       background_r: 30
       background_g: 144
       background_b: 255
       use_sim_time: false
   ```

   - 一个文件可装多个节点：并列再写一个节点名块即可。
   - 通配符 `/**` 表示「应用到所有节点」，常用于全局参数：

     ```yaml
     /**:
       ros__parameters:
         use_sim_time: true
     ```

3. **加载方式一：launch 里传「文件路径字符串」。** 关键点——launch 的 `parameters` 列表里，**传字符串 = 文件路径，传字典 = 内联参数**，二者含义不同：

   ```python
   import os
   from ament_index_python.packages import get_package_share_directory

   cfg = os.path.join(
       get_package_share_directory('turtle_demo'),  # 定位 install 后的 share 目录
       'config', 'params.yaml')

   Node(package='turtle_demo', executable='turtle_painter',
        name='turtle_painter',
        parameters=[cfg])        # ← 字符串：从文件加载
   ```

   对比之前的内联写法（作用相同，但参数值写死在 launch 里）：

   ```python
   parameters=[{'background_r': 30, 'background_g': 144, 'background_b': 255}]  # ← 字典：内联
   ```

   两者可混用，后面的覆盖前面的：`parameters=[cfg, {'background_b': 0}]`。

4. **加载方式二：命令行 `--ros-args --params-file`。** 不经过 launch，直接 `ros2 run` 也能挂参数文件：

   ```bash
   ros2 run turtle_demo turtle_painter --ros-args --params-file /path/to/params.yaml
   ```

5. **导出：`ros2 param dump` 生成的正是这种格式。** N024 里 `dump` 导出的 YAML 正好是「节点名 + `ros__parameters`」结构，所以 dump 出来的文件能直接再 load 回去——这就是 dump 和 YAML 文件的关系：

   ```bash
   ros2 param dump /turtle_painter > turtle_painter.yaml   # 导出当前参数
   ros2 param load /turtle_painter turtle_painter.yaml     # 原样加载回来
   ```

6. **YAML 值类型 → ROS 2 参数类型推断。** YAML 本身弱类型，ROS 2 加载时按字面量推断参数类型：

   | YAML 写法 | 推断的参数类型 |
   | --------- | ------------- |
   | `30` | integer |
   | `3.14` | double |
   | `true` / `false` | bool |
   | `hello` / `"hello"` | string |
   | `[1, 2, 3]` | integer array |
   | `[1.5, 2.5]` | double array |
   | `["a", "b"]` | string array |

   这和 `declare_parameter` 默认值定类型是同一个道理（见 [[N025 参数的声明读写与命令行工具]]）：**推断出的类型必须和节点里 declare 的类型一致**，否则加载报错。

7. **坑 ①：节点名不匹配 → 静默不生效。** YAML 顶层节点名必须和实际节点名**完全一致**（含命名空间）。对不上时 ROS 2 **不报错**，参数悄悄没加载上——排查时最容易忽略。

8. **坑 ②：YAML 布尔字面量陷阱。** YAML 把 `yes/no/on/off`（及大小写变体）都当布尔值。想传字符串 `"on"` 必须加引号，否则被推断成 `true`。

9. **实战对照 `turtle_demo`：** 现在 `config/params.yaml` 文件其实已写好，但 `turtle_demo.launch.py` 里用的还是内联字典、并没有引用这个文件。把第 3 步的写法接进 launch，参数就从「写死在 launch」变成「从 YAML 加载」，两者值相同、行为一致。

> **Note（连接 / 深化）：**
> - 连接：YAML 文件 = 参数的「持久化配置」，配合 N024 的 `dump`/`load` 命令行、参数服务，构成参数的完整操作面：**declare 定骨架 → YAML/内联/命令行定初值 → ros2 param set 运行时改 → 回调响应**。
> - 深化：launch 里 `parameters` 既能传字符串（文件）也能传字典（内联），本质是 launch 把参数「打包」成一批值，在节点启动时一次性灌进节点的参数容器（[[N026 参数存在哪-节点内的键值对容器]] 里的那个 map）——YAML 只是把这批值提前写进了文件。

## 思考

（留白 —— 如果 YAML 里写的类型和 `declare_parameter` 默认值定下的类型不一致，加载时会发生什么？为什么 launch 里内联字典能覆盖 YAML 文件里的同名参数？）

## 总结

**本质：** YAML 参数文件把参数值从代码/launch 里搬进独立配置文件（配置与代码分离）；格式固定为「节点名 → `ros__parameters` → 键值对」，通过 launch 的 `parameters=[文件路径]` 或命令行 `--params-file` 在节点启动时灌进参数容器；`ros2 param dump` 导出的正是这种格式。类型由字面量推断、节点名必须匹配，否则静默失效或报错。
**标签:** #功能实现 #Parameter参数 #YAML配置 #launch启动 #命令行CLI
