---
tags:
  - 语法知识
  - C++语法
  - 范围for
  - 循环Loop
---

# 范围 for 遍历与哨兵标志位模式 · 语法知识 · N032

**时间:** 2026-10-06 22:45
**标签:** #语法知识 #C++语法 #范围for #循环Loop
**关联:** [[N029 turtle_painter参数中转节点拆解]] [[N031 异常处理try-catch-throw]]

## 疑惑点

这段代码是什么写法？`bool ok = true;` 然后 `for (const auto & ...)` 里 `if (!...) break;` 到底在干嘛？

```cpp
bool ok = true;
for (const auto & res : results) {
  if (!res.successful) { ok = false; break; }
}
```

## 实际情况

### 一、整体语义：检查「是否全都成功」

这段代码在回答一个问题：results 里**每一个**都 successful 吗？结论放在 `ok` 里——全成功 `ok = true`，有一个失败 `ok = false`。

### 二、哨兵标志位模式（惯用法）

```cpp
bool ok = true;                     // ① 先假设「全满足」
for (...) {                         // ② 遍历
  if (不满足) { ok = false; break; } // ③ 发现反例 → 推翻假设 + 提前退出
}
// ④ 循环结束，ok 就是最终结论
```

核心思想：**先乐观地设为 true，遍历中一旦发现反例就置 false 并 break**——不用看完剩下的（已经知道结论了）。

### 三、范围 for 语法

```cpp
for (类型 变量 : 容器) { ... }   // 逐个取出容器里的元素
```

- 比 `for (int i = 0; i < n; i++)` 更简洁，不需要下标；
- 这里的「容器」是 `results`（一个 vector）。

### 四、`const auto &` 是什么

```cpp
for (const auto & res : results)
//     └──┬──┘  └┬┘
//        │      └ 引用：不拷贝元素本身
//        └ auto：类型自动推导（元素是啥类型就是啥）
//   const：只读，不修改元素
```

- `auto` = 让编译器推导类型（这里元素是 `SetParametersResult`）；
- `&` = 引用，遍历时**不拷贝**整个元素（省内存、省时间）；
- `const` = 只读，保证遍历过程不改动元素。

> 合起来 `const auto &` 是遍历容器的**标准姿势**：不拷贝、不改动。

### 五、`!` 与 `break`

- `!res.successful` —— `!` 逻辑非：successful 为 false 时，`!` 后为 true，进入 if；
- `break` —— 立即**跳出整个循环**（不再遍历剩余元素）。

> **Note（连接 / 深化）：**
> - 连接：这段代码在 [[N029 turtle_painter参数中转节点拆解]] 的 apply_color 里，配合 [[N031 异常处理try-catch-throw]] 的 try/catch 使用。
> - 深化：`ok = false; break;` 是「提前退出」，比遍历完再判断更省；但若你**需要知道具体是哪个失败**，就别 break，记录下失败项再继续。

## 思考

（留白 —— 如果不 break、遍历到最后，结论和现在一样吗？什么时候必须 break、什么时候不能 break？）

## 总结

**本质：** 哨兵标志位模式——先设 `bool ok = true`，用范围 for（`const auto &` 不拷贝不改动地遍历）检查每个元素，发现不满足就 `ok = false; break;` 提前退出，循环结束 `ok` 即「是否全满足」的结论。
**标签:** #语法知识 #C++语法 #范围for #循环Loop
