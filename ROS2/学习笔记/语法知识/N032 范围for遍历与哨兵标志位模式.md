范围 for 用 `const auto &` 遍历容器，不拷贝也不修改；哨兵标志位模式则是「先假设全部满足，发现反例就置 false 并 break」。

## 哨兵模式

```cpp
bool ok = true;
for (const auto & res : results) {
  if (!res.successful) { ok = false; break; }
}
// ok 就是「是否全都成功」
```

四步：先假设全满足 → 遍历 → 发现反例推翻假设并提前退出 → 循环结束得到结论。一旦发现反例就不必看完剩余元素。

## 范围 for

```cpp
for (类型 变量 : 容器) { ... }
```

比下标循环简洁，不需要索引。

`const auto &` 三部分：

| 组成 | 含义 |
|---|---|
| `auto` | 编译器推导元素类型 |
| `&` | 引用，不拷贝整个元素 |
| `const` | 只读，遍历时不改动元素 |

合起来是遍历容器的标准姿势。

`!res.successful` 是逻辑非，false 时进入 if；`break` 立即跳出整个循环。

## 坑

- 遍历时修改容器（增删元素）会让迭代器失效。
- 需要知道「具体哪个失败」时不要 break，记录失败项后继续。
- 只读遍历却漏了 `&`，大对象会逐个拷贝。
- 需要在循环中改元素时不能用 `const`。

> PS：C++20 可用 `std::ranges::all_of(results, [](auto & r){ return r.successful; })` 一行表达同样语义。

`const auto &` 是无拷贝只读遍历的标准写法；哨兵标志位 = 乐观假设 + 反例 break，用来回答「是否全部满足」。