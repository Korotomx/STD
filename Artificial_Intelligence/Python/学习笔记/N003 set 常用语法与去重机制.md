---
tags:
  - Python
  - 集合set
  - 哈希表HashTable
  - 去重Dedup
  - 数据结构DataStructure
---

# set 常用语法与去重机制 · 语法知识 · N003

**时间:** 2026-10-11
**标签:** #Python #集合set #哈希表HashTable #去重Dedup #数据结构DataStructure
**关联:** [[N001 对象、引用与可变性]] [[N002 dict 常用语法]]

## 常用语法

- **创建**:`set()`、`{1,2,3}`、`set([...])`、`{x for ...}` 推导式(注意 `{}` 是空 dict,不是空 set)
- **增删**:`add(x)` / `remove(x)`(不存在报错)/ `discard(x)`(不报错)/ `pop()`(任意删)/ `clear()`
- **判断**:`x in s`(O(1))、`len(s)`
- **集合运算**:`a|b` 并 / `a&b` 交 / `a-b` 差 / `a^b` 对称差 / `issubset` / `issuperset` / `isdisjoint`

## 实现机制

set 底层是**哈希表**,和 dict 同源(相当于「只有键没有值」的 dict)。增删查平均 O(1)。对照 C++:`std::unordered_set`(哈希表、无序)= Python set;`std::set`(红黑树、有序)Python 无直接对应。

## 为什么能去重

加入元素两步:①算 `hash(x)` 定位桶 → ②桶内比 `==`。相同值 ⟹ 相同 hash ⟹ 同桶 ⟹ `==` 相等 ⟹ 判为重复不加。规则:两元素在 set 里「相同」当且仅当 `hash 相等 且 == 相等`。因此 set 只能放**可哈希 = 不可变**元素(int/str/tuple/frozenset)。

## 风险 / 坑

1. **元素必须可哈希**:`{[1,2]}` → `TypeError: unhashable type: 'list'`(可变对象 hash 不稳定)
2. **无序**:不能索引;要「去重且保序」用 `list(dict.fromkeys(xs))`
3. **内存开销**:哈希表比 list 占内存
4. **自定义对象默认按身份去重**(基于 id,除非重写 `__eq__`/`__hash__`)
5. **NaN 特例**:`nan != nan` 但 hash 相同,可塞多个 NaN

## 总结

**本质**:set = 无序、不可重复、O(1) 查重的哈希集合;去重靠「hash 定位 + == 判定」;最大坑是「只能放不可变元素」。

**标签:** #Python #集合set #哈希表HashTable #去重Dedup #数据结构DataStructure

## 真实应用(计算机 / ML)

1. **O(1) vs O(n)**:`x in set` 是哈希查找 O(1),`x in list` 是线性扫描 O(n);20 万元素差出几个数量级(实测 0.0000s vs 0.5s)。
2. **去重与集合运算**是数据清洗 pipeline 的高频操作(去重、求交集/差集)。
3. **可哈希 = 不可变**:和 N001 的可变性是一套——所以 list 不能进 set、tuple 能。
