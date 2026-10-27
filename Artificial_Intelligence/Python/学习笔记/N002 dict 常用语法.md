`dict` 与 `set` 都是哈希表容器：dict 存“键 → 值”，set 只存键。两者查找、插入平均 O(1)，键/元素必须可哈希（通常即不可变）。set 因此天然去重，dict 的键天然唯一。

## 共同机制

- 查找：`hash(key)` 定位桶 → 桶内用 `==` 比较；平均 O(1)，冲突严重时最坏 O(n)。
- 可哈希 = 哈希值在对象生命周期内不变 = 通常不可变：`int` / `str` / `frozenset` 可以，`tuple` 需内部元素也可哈希；`list` / `dict` / `set` 不行。
- 自定义对象默认按身份（`id`）哈希；重写 `__eq__` 时应同时重写 `__hash__`。
- 对照 C++：dict ≈ `unordered_map`，set ≈ `unordered_set`；有序的 `std::set` 在 Python 没有直接对应。

## dict 常用语法

| 操作 | 写法 |
| --- | --- |
| 创建 | `{}`、`dict(a=1)`、`dict([(k, v), ...])`、`dict.fromkeys(keys, 0)`、`{k: v for ...}` |
| 取值 | `d[k]`（缺键报 `KeyError`）、`d.get(k, default)`、`d.setdefault(k, v)`（缺键则插入） |
| 增改删 | `d[k] = v`、`d.update(other)`、`del d[k]`、`d.pop(k[, default])`、`d.clear()` |
| 判断 | `k in d`、`len(d)` |
| 遍历 | `for k in d`、`for k, v in d.items()`、`for v in d.values()` |
| 视图 | `keys()` / `values()` / `items()` 是实时视图，要冻结用 `list(...)` |
| 合并排序 | `d1 \| d2`、`d1 \|= d2`；`sorted(d)` 按键，`sorted(d.items(), key=lambda kv: kv[1])` 按值 |

高频三件套：`in` 判键、`get` 安全取值、`items()` 遍历。词频统计是 `get` 的经典用法：

```python
count = {}
for w in words:
    count[w] = count.get(w, 0) + 1
```

## set 常用语法

| 操作 | 写法 |
| --- | --- |
| 创建 | `set()`、`{1, 2, 3}`、`set(iterable)`、`{x for x in xs}`；`{}` 是空 dict |
| 增删 | `add(x)`、`remove(x)`（缺元素报错）、`discard(x)`（不报错）、`pop()`、`clear()` |
| 判断运算 | `x in s`、`a \| b` 并、`a & b` 交、`a - b` 差、`a ^ b` 对称差、`issubset`、`isdisjoint` |

## 去重机制

两个元素“相同”当且仅当 **hash 相等且 `==` 相等**；相同值必有相同 hash，落入同一桶后被 `==` 判定为重复。set 可看作“只有键、没有值”的 dict。

- 直接去重：`set(xs)`。
- 去重且保序：`list(dict.fromkeys(xs))`（dict 3.7+ 保持插入顺序）。

## 坑与边界

1. 可变对象不能作键/元素：`{[1, 2]}` 报 `TypeError: unhashable type: 'list'`。
2. set 无序、不能索引；需要顺序时用 `dict.fromkeys` 保序去重。
3. dict 的插入顺序不是排序；要排序显式 `sorted`。
4. 哈希表比 list 占内存；数据量小时 list 可能更快，数据量大时 O(1) 才是决定性的。
5. `nan != nan` 但 hash 相同，set 里可以存在多个 NaN。
6. 遍历时增删会改变大小并触发 `RuntimeError`，先复制或先收集要改的键；缺键是正常分支用 `get`，是 bug 就让 `d[k]` 的 `KeyError` 暴露。

## 总结

dict/set 都是哈希表，O(1) 查找靠“hash 定位桶 + `==` 判定”。键和元素必须可哈希；set 去重、dict 键唯一都是同一机制的推论。去重保序用 `dict.fromkeys`。