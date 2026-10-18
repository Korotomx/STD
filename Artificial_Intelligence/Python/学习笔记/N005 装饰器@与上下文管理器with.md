---
tags:
  - Python
  - 装饰器Decorator
  - 上下文管理器ContextManager
  - with
  - 魔法方法DunderMethod
  - tryexceptfinally
  - contextlib
---

# 装饰器@与上下文管理器with · 语法知识 · N005

**时间:** 2026-10-18
**标签:** #Python #装饰器Decorator #上下文管理器ContextManager #with #魔法方法DunderMethod #tryexceptfinally #contextlib
**关联:** [[N004 Python 特殊性质与思考方式]]（dunder 魔法方法 / 鸭子类型的直接应用）· [[N001 对象、引用与可变性]]（一等对象、函数也是对象）

## 疑惑点

`@torch.no_grad()` 和 `with torch.no_grad():` 在训练代码里都见过，这俩「@」和「with」到底是什么？为什么同一个 `torch.no_grad()` 既能当装饰器、又能当 `with` 的对象？它们和「上下文管理」是什么关系？

## 实际情况

### 1. `@` 装饰器：接收函数、返回「换皮后的函数」

**本质**：装饰器是一个「接收函数、返回新函数」的函数。`@decorator` 是语法糖：

```python
@decorator
def f():
    ...

# 完全等价于
def f():
    ...
f = decorator(f)
```

注意：装饰器在**函数定义时**就执行、把 `f` 替换掉了。它的价值是能「在调用 f 前后」插入逻辑（计时、日志、缓存、权限、关梯度……），而不侵入函数本体（横切关注点）。

最简例子：

```python
def log(func):                          # 装饰器：收函数
    def wrapper(*args, **kwargs):       # 换皮后的新函数
        print(f"调用 {func.__name__} 前")
        result = func(*args, **kwargs)
        print("调用后")
        return result
    return wrapper

@log
def add(a, b):
    return a + b
```

`add(1, 2)` 会先打印「调用前」再算 `1+2`。你代码里的 `@torch.no_grad()` 同理：把 `evaluate` 整个函数体包进「不算梯度」。

### 2. `with` 上下文管理器：setup → 做 → teardown（保证收尾）

**本质**：`with` 保证「进入时做 setup、离开时（哪怕中途报错）做 teardown」。靠 `__enter__` / `__exit__` 两个魔法方法：

```python
with 对象 as x:
    ...   # x = 对象.__enter__() 的返回值
# 离开 with 块时，自动调 对象.__exit__(...)，哪怕块里抛异常也会调
```

经典例子（文件）：

```python
with open("a.txt") as f:   # __enter__ 打开并返回文件对象
    data = f.read()
# 离开时 __exit__ 自动关闭文件，就算 read 报错也会关
```

对比 C 要手动 `fopen`/`fclose`，忘了 `close` 就泄漏。`with` 把「准备/清理」绑定在代码块的边界上，所以叫「**上下文管理**」——管理一段代码执行期间的资源与状态环境。

### 3. 关键：`torch.no_grad()` 为什么两种用法都行

`torch.no_grad()` 返回一个对象，它**同时**实现了：

- `__enter__` / `__exit__` → 所以能被 `with torch.no_grad():`
- `__call__` → 所以能被 `@torch.no_grad()` 当装饰器

这正是 [[N004 Python 特殊性质与思考方式]] 讲的「鸭子类型」：一个对象能同时扮演两种角色，取决于你用它时调了哪个魔法方法。`with` 调 `__enter__`，装饰器调 `__call__`，各取所需。

### 4. 其它「上下文管理机制」

**`try / except / else / finally`**——其中 `finally` 是 `with` 的「手动版」：无论是否异常都执行清理。`with` 底层就是 `try/finally` 的语法糖封装：

```python
f = open(...)
try:
    data = f.read()
finally:          # 无论如何都执行
    f.close()
```

**`contextlib.contextmanager`**——用生成器 `yield` 快速造上下文管理器，不用写类实现 `__enter__/__exit__`：

```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield                     # yield 前 = __enter__，yield 后 = __exit__
    print(f"耗时 {time.time()-start:.2f}s")
```

### 5. 别混淆：`@` 在 Python 里有第二个意思

- 行首的 `@decorator` = **装饰器**。
- 表达式里的 `a @ b` = **矩阵乘法运算符**（等价 `torch.matmul(a, b)` / `np.matmul`）。PyTorch / NumPy 里会大量见到 `X @ W`。

## 思考

（留白 —— `@` 装饰器和 `with` 上下文管理器，一个包装「函数」、一个包装「代码块」，本质都是在「进入前/离开后」插入逻辑。如果让你设计一个「计时 + 关梯度 + 打印」都要做的训练函数，你会选装饰器还是 `with`？为什么？）

## 总结

**本质：** `@` 装饰器 = 接收函数返回新函数，在「调用前后」插入逻辑（横切关注点）；`with` 上下文管理器 = 靠 `__enter__/__exit__` 在「进入/离开」做 setup/teardown，保证收尾（即使报错）。两者都是 N004 那套 dunder 魔法方法的直接应用：装饰器靠 `__call__`，`with` 靠 `__enter__/__exit__`。`torch.no_grad()` 同时实现两者，所以两种写法都成立。相关机制还有 `try/finally`（`with` 的手动版）和 `contextlib.contextmanager`（用 `yield` 造上下文管理器）。

**标签:** #Python #装饰器Decorator #上下文管理器ContextManager #with #魔法方法DunderMethod #tryexceptfinally #contextlib
