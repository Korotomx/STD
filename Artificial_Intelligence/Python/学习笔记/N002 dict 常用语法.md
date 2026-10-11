---
tags:
  - Python
  - 字典dict
  - 哈希表HashTable
  - 数据结构DataStructure
---

# dict 常用语法(字典)· 语法知识 · N002

**时间:** 2026-10-11
**标签:** #Python #字典dict #哈希表HashTable #数据结构DataStructure
**关联:** [[N001 对象、引用与可变性]] [[list 列表]]

## 核心

`dict` = 「键 → 值」的哈希表,等价于 C++ 的 `unordered_map`(C 没有内建等价物)。键唯一、通常用 str/int;值任意。dict 是**可变**类型(见 N001)。

## 常用语法

- **创建**:`{}`、`dict(a=1,b=2)`、`dict([("a",1),...])`、`dict.fromkeys(keys,0)`、`{k:v for ...}` 推导式
- **取值**:`d[k]`(不存在报 KeyError)/ `d.get(k,默认)`(安全)/ `d.setdefault(k,v)`(没有就塞)
- **增改**:`d[k]=v`、`d.update({...})`
- **删除**:`del d[k]`、`d.pop(k[,默认])`、`d.popitem()`、`d.clear()`
- **判断**:`k in d`(最常用)、`len(d)`
- **遍历**:`for k in d`(键)/ `for k,v in d.items()`(键值对,最常用)/ `for v in d.values()`
- **视图**:`keys()/values()/items()` 返回实时视图,要冻结成列表用 `list(...)`
- **合并**:`d1 | d2`(Python 3.9+)、`d1 |= d2`
- **排序**:`sorted(d)`(按键)、`sorted(d.items(), key=lambda x:x[1])`(按值)

## 高频三件套

`in` 判断键、`get` 安全取值、`items()` 遍历键值对。

## 总结

**本质**:dict 是「键→值」映射,靠键哈希实现 O(1) 查找。词频统计套路 `count[w] = count.get(w, 0) + 1` 是 `get` 的经典用法。

**标签:** #Python #字典dict #哈希表HashTable #数据结构DataStructure

## 真实应用(计算机 / ML)

1. **Python 命名空间就是 dict**:函数局部变量、类属性、模块全局变量,底层全是 dict;每次赋值都在往某个 dict 里塞键值对。
2. **NLP 词表 = dict**:`word → id` 的映射就是 dict(Transformer 的 tokenizer 就是一个巨大 dict)。
3. **O(1) 查找**:20 万元素 `in` 1000 次,list 约 0.5s,dict/set 近乎 0s——大数据量下是「能跑完 vs 跑不完」的区别。
4. **可哈希要求**:`functools.lru_cache` 靠 dict 缓存,参数必须可哈希(list 不行、tuple 行)。
