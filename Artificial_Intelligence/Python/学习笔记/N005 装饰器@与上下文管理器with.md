装饰器 `@` 包装函数，`with` 包装代码块，两者都在“进入前 / 离开后”插入逻辑。`torch.no_grad()` 同时支持两种写法，因为它既实现了 `__enter__` / `__exit__`，又实现了 `__call__`。

## 装饰器：接收函数、返回新函数

`@decorator` 是语法糖，等价于定义后执行 `f = decorator(f)`，在函数定义时就把 `f` 替换掉。价值在于不侵入函数本体，就能在调用前后插入计时、日志、缓存、权限、关梯度等横切逻辑。

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"call {func.__name__}")
        result = func(*args, **kwargs)
        print("done")
        return result
    return wrapper

@log
def add(a, b):
    return a + b
```

`@torch.no_grad()` 同理：把整个函数体包进“不算梯度”的上下文。

## 上下文管理器：setup → 使用 → teardown

`with obj as x:` 进入时执行 `x = obj.__enter__()`，离开时必调 `obj.__exit__(...)`，块内抛异常也会调。

```python
with open("a.txt") as f:
    data = f.read()
# 离开 with 时自动 close，即使 read 抛异常
```

C 要手动 `fopen` / `fclose`，忘了 close 就泄漏。`with` 把资源清理绑定到代码块边界，所以叫“上下文管理”。

## 为什么 `torch.no_grad()` 两种用法都行

它返回的对象同时实现了：

- `__enter__` / `__exit__` → 能用于 `with torch.no_grad():`
- `__call__` → 能被 `@torch.no_grad()` 当装饰器

鸭子类型的直接体现：同一个对象按使用方式调用不同魔法方法，`with` 调 `__enter__`，装饰器调 `__call__`。

## 相关机制

- `try/finally` 是 `with` 的手动版：无论是否异常都执行清理；`with` 本质是它的封装。
- `contextlib.contextmanager` 用生成器快速造上下文管理器，`yield` 前是 `__enter__`，`yield` 后是 `__exit__`：

```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    yield
    print(f"{time.time() - start:.2f}s")
```

## 坑

- 表达式里的 `a @ b` 是矩阵乘法（`X @ W`），不是装饰器。
- 装饰器在定义时替换函数；不套 `functools.wraps` 会丢掉 `__name__`、docstring 等元数据。
- 被装饰后的函数签名可能变化，影响 IDE 提示和依赖内省的框架。

## 总结

`@` 用 `__call__` 在调用前后插入逻辑，`with` 用 `__enter__` / `__exit__` 保证 setup/teardown；两者都是魔法方法的应用。`torch.no_grad()` 同时实现两套协议，所以两种写法都成立。