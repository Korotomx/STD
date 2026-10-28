用“颜色压缩”做例子：`uchar` 每通道 0~255，三通道有 1600 万种颜色，很多场景不需要这么多。把每个值向下取整到 10 的倍数：

```
I_new = (I_old / 10) * 10        // uchar 除法自动截断
```

比如 0~9 → 0，10~19 → 10。逐像素做除法和乘法很贵，于是有了几种遍历方式的速度对比。

## Mat 在内存里怎么放

- 灰度图：一个 `H × W` 矩阵。
- 彩色图：每列展开成 3 个子列（**BGR**，不是 RGB），所以一行是 `W × 3` 个 `uchar`。
- 行通常连续存放；整块内存连续时（`Mat::isContinuous()` 为真）可以把二维矩阵当成一条长数组来扫。

## 四种访问方式

### 1. 指针（最快的手写方式）

```cpp
int channels = I.channels();
int nRows = I.rows;
int nCols = I.cols * channels;

if (I.isContinuous()) {      // 连续时直接压成一维
    nCols *= nRows;
    nRows = 1;
}

for (int i = 0; i < nRows; ++i) {
    uchar* p = I.ptr<uchar>(i);   // 第 i 行首地址
    for (int j = 0; j < nCols; ++j)
        p[j] = table[p[j]];
}
```

自己负责行尾 padding（可能存在的间隙），最快但要小心越界。

### 2. 迭代器（安全）

```cpp
MatIterator_<Vec3b> it, end;
for (it = I.begin<Vec3b>(), end = I.end<Vec3b>(); it != end; ++it) {
    (*it)[0] = table[(*it)[0]];
    (*it)[1] = table[(*it)[1]];
    (*it)[2] = table[(*it)[2]];
}
```

迭代器自动跨行、跳过间隙。彩色图要用 `Vec3b`；用 `uchar` 迭代器只能碰到蓝通道。

### 3. `at<>` / `Mat_`（随机访问）

```cpp
Mat_<Vec3b> _I = I;
for (int i = 0; i < I.rows; ++i)
    for (int j = 0; j < I.cols; ++j)
        for (int c = 0; c < 3; ++c)
            _I(i, j)[c] = table[_I(i, j)[c]];
```

每次访问都要按 `(row, col)` 算地址；debug 模式还有越界检查。适合**随机取点**，不适合全图扫描。

### 4. `cv::LUT()`（推荐）

```cpp
Mat lookUpTable(1, 256, CV_8U);
for (int i = 0; i < 256; ++i) lookUpTable.at<uchar>(0, i) = table[i];

LUT(I, lookUpTable, J);
```

把 256 种输入值的输出提前算好，运行时只查表。OpenCV 内部经 TBB 多线程，最快。

### 查表为什么快

原式每个像素要做一次除法 + 一次乘法；查表把 256 种可能结果预先算好，运行时只剩一次数组索引。像素数越大，省下的计算越多。

## 计时

```cpp
double t = (double)getTickCount();
// ... 计时区间 ...
t = ((double)getTickCount() - t) / getTickFrequency();
```

`getTickCount()` 是 CPU 从某时刻起的 tick 数，`getTickFrequency()` 是每秒 tick 数，相除得秒。

## 实测（2560×1600 彩色，100 次平均）

| 方式 | 耗时 |
| --- | --- |
| 指针 Efficient Way | 79.47 ms |
| 迭代器 Iterator | 83.72 ms |
| `at` 随机访问 | 93.79 ms |
| `cv::LUT` | **32.58 ms** |

## 结论

- 能用现成 OpenCV 函数就用（`LUT`、`convertTo`、`cvtColor` 等），它们通常多线程且已优化。
- 自己写全图扫描：**指针 > 迭代器 > `at`**。
- `at` 只用于零散取点，不要拿来遍历整图。
- 连续内存判断 + 压成一维，是手写扫描的常用加速。

## 易错点

- OpenCV 彩色通道顺序是 **BGR**。
- `Mat::isContinuous()` 为假时不能把行列直接乘起来当一维数组。
- 迭代器遍历彩色图必须用 `Vec3b`，否则只处理一个通道。
- `uchar` 做除法会截断，`I/10*10` 是向下取整，不是四舍五入。
