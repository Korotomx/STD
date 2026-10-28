CUDA 的 SIMT 模型要程序员手动指定“哪个线程算哪块数据、数据在 global/shared/register 之间怎么搬”。**Tile-Level Programming** 把粒度抬高一层：程序员只描述“一个 tile 怎么 load / compute / store”，线程映射、内存布局交给编译器。Triton 和 TileLang 是两种代表。

## 从 thread 到 tile

| 层次 | 程序员要管什么 |
| --- | --- |
| CUDA C++ | thread / warp / block 分工、shared memory、同步、合并访存、bank conflict |
| Triton | program 负责哪个 tile、tile 的形状、load/compute/store；线程映射由编译器做 |
| TileLang | 显式写 shared memory tile、register fragment、pipeline，但仍以 tile 为语义单位 |

一个 tile kernel 的通用骨架：

```
定位当前 tile 负责的数据区域
→ 从 global 加载该 tile
→ tile 内计算
→ 写回 global
→ 处理边界（最后一个不完整 tile）
```

## Triton

**以 program 为单位**：每个 program 负责一个数据 tile。`pid` 是 tile 的编号，`tl.arange` 生成 tile 内偏移，`mask` 处理越界。

```python
@triton.jit
def add_kernel(x, y, z, n: tl.constexpr, BLOCK_SIZE: tl.constexpr):
    pid = tl.program_id(0)
    offsets = pid * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE)
    mask = offsets < n

    x_val = tl.load(x + offsets, mask=mask, other=0.0)
    y_val = tl.load(y + offsets, mask=mask, other=0.0)
    tl.store(z + offsets, x_val + y_val, mask=mask)

def add(x, y):
    z = torch.empty_like(x)
    grid = (triton.cdiv(x.numel(), 1024),)
    add_kernel[grid](x, y, z, x.numel(), BLOCK_SIZE=1024)
    return z
```

### 矩阵乘

`C = A @ B`，`A: M×K`，`B: K×N`。每个 program 算 `C` 的一个 `BLOCK_M × BLOCK_N` tile，沿 `K` 维分块累加：

```python
@triton.jit
def matmul_kernel(A, B, C,
                  M: tl.constexpr, N: tl.constexpr, K: tl.constexpr,
                  stride_am, stride_ak, stride_bk, stride_bn,
                  stride_cm, stride_cn,
                  BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr, BLOCK_K: tl.constexpr):
    pid_m, pid_n = tl.program_id(0), tl.program_id(1)
    offs_m = pid_m * BLOCK_M + tl.arange(0, BLOCK_M)
    offs_n = pid_n * BLOCK_N + tl.arange(0, BLOCK_N)
    offs_k = tl.arange(0, BLOCK_K)

    acc = tl.zeros((BLOCK_M, BLOCK_N), dtype=tl.float32)
    for k0 in range(0, K, BLOCK_K):
        a = tl.load(A + offs_m[:, None] * stride_am
                      + (k0 + offs_k[None, :]) * stride_ak,
                    mask=(offs_m[:, None] < M) & (k0 + offs_k[None, :] < K), other=0.0)
        b = tl.load(B + (k0 + offs_k[:, None]) * stride_bk
                      + offs_n[None, :] * stride_bn,
                    mask=(k0 + offs_k[:, None] < K) & (offs_n[None, :] < N), other=0.0)
        acc += tl.dot(a, b)

    c_ptrs = C + offs_m[:, None] * stride_cm + offs_n[None, :] * stride_cn
    tl.store(c_ptrs, acc, mask=(offs_m[:, None] < M) & (offs_n[None, :] < N))
```

`[None, :]` / `[:, None]` 是广播成二维坐标网格，`mask` 同时管 M、K 两个方向的边界。

### 局限

- 编译器是黑盒：shared memory 布局、bank conflict 全由它决定。
- PTX / SASS 不透明，性能回退难定位。
- 与 CUTLASS / cuBLAS 手工优化仍有差距。
- 复杂 pipeline、warp specialization 难表达。
- 报错和调优靠反复 autotune。

本质是**用控制权换开发效率**。控制权成为瓶颈时，往 TileLang 或 CUDA C++ 走。

## TileLang

更强调**显式层次结构**，更接近手写 CUDA kernel 的骨架，但仍在 tile 语义层。三个抽象层次：

| | Level 1 硬件无关 | Level 2 Tile 级 | Level 3 线程级 |
| --- | --- | --- | --- |
| 并行 | 编译器隐式决定 | 显式 Grid / Tile / Block | 显式 Thread / Warp / WarpGroup |
| 内存 | 以 global 直访为主 | 显式 shared / register fragment | 寄存器 + ISA 级访存 |
| 计算 | 自动调度 | `T.gemm` + software pipeline | inline PTX、手写微内核 |
| 性能 | 中 | 高 | 最高（局部热点） |
| 可移植性 | 高 | 中-高 | 低-中 |
| 场景 | 原型、教学 | 主力实现、性能工程 | 瓶颈路径、特殊指令 |

### 核心 primitive

| primitive | 作用 |
| --- | --- |
| `@tilelang.jit` | 编译成可调用 kernel |
| `@T.prim_func` | 定义 TIR 函数 |
| `T.Kernel(...)` | 建 grid，一个实例 = 一个 CTA |
| `T.Tensor` / `T.Buffer` | global memory 上的输入输出 |
| `T.alloc_shared` | CTA 共享的输入 tile |
| `T.alloc_fragment` | 寄存器里的累加器 |
| `T.copy` | 内存层次之间搬数据 |
| `T.gemm` | tile 级矩阵乘加 |
| `T.Pipelined` | 沿 K 维分块，重叠搬运与计算 |

数据流固定为：

```
Global ──T.copy──▶ Shared ──T.gemm──▶ Register Fragment ──T.copy──▶ Global
```

### 矩阵乘

```python
@tilelang.jit
def matmul(M, N, K, BLOCK_M, BLOCK_N, BLOCK_K,
           dtype="float16", accum_dtype="float32"):
    @T.prim_func
    def main(A: T.Buffer((M, K), dtype),
             B: T.Buffer((K, N), dtype),
             C: T.Buffer((M, N), accum_dtype)):
        with T.Kernel(T.ceildiv(N, BLOCK_N), T.ceildiv(M, BLOCK_M), threads=128) as (bx, by):
            A_shared = T.alloc_shared((BLOCK_M, BLOCK_K), dtype)
            B_shared = T.alloc_shared((BLOCK_K, BLOCK_N), dtype)
            C_local  = T.alloc_fragment((BLOCK_M, BLOCK_N), accum_dtype)
            T.clear(C_local)

            for k in T.Pipelined(T.ceildiv(K, BLOCK_K), num_stages=3):
                T.copy(A[by * BLOCK_M, k * BLOCK_K], A_shared)
                T.copy(B[k * BLOCK_K, bx * BLOCK_N], B_shared)
                T.gemm(A_shared, B_shared, C_local)

            T.copy(C_local, C[by * BLOCK_M, bx * BLOCK_N])
    return main
```

与 Triton 的差异：shared memory tile 和 register fragment **显式声明**，K 维分块用 `T.Pipelined(num_stages=...)` 明确表达流水线。

## 三者怎么选

```
原型 / 通用算子 / 教学   → Triton（写起来最快）
主力实现 / 性能工程      → TileLang（能控内存层次和 pipeline）
极端调优 / 特殊硬件指令  → CUDA C++（inline PTX、warp 级控制）
```

## 识别信号

- 问「写高性能算子该用什么」→ 按抽象层次选：原型/通用算子 Triton，性能工程 TileLang，极端调优 CUDA C++。
- 代码里是 `tl.load` / `tl.store` / `@triton.jit` → tile DSL，关注 tile 形状而不是线程下标。
- 问「为什么 Triton 写起来短」→ 编译器替你做线程映射和 shared memory 分配，不是运算变少。
- 需要显式控制 shared memory、register fragment、流水线级数 → TileLang（`T.Pipelined`）。
- 看到「program」这个词 → 是 tile 计算实例，别和 thread、block 混用。

## 容易混淆的点

- 三者都是 **DSL**：CUDA C++ 是面向 GPU 的 DSL，Triton/TileLang 是更上层的 tile DSL。
- Triton 的 `program` 不等于 CUDA 的 `thread`，也不完全等于 block；它是“一个 tile 的计算实例”。
- Triton 并非不关心内存，只是 shared memory 策略由编译器决定；TileLang 把这层拿回来。
- TileLang 不是“更快的 Triton”，而是**控制粒度更细**；写得对才更快。

## 总结

CUDA 手动把 tile 映射到线程；Triton 只写 tile 的 load/compute/store，让编译器做线程映射；TileLang 在 tile 语义上重新显式暴露 shared memory、register fragment 和 pipeline。抽象越高越易写，越低越能压榨性能。
