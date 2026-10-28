文件读写、字符串解析、路径操作在 C++ 里全部是「类 + 对象」：`fstream`、`sstream`、`filesystem` 各提供一组类，`std::cout` 只是标准库预置的 ostream 实例。三者共用 `<<` / `>>` 接口，区别只在流连向哪里。

## 类与头文件

| 想做的事 | 头文件 | 类 | 典型对象 |
|---|---|---|---|
| 读文件 | `<fstream>` | `std::ifstream` | `std::ifstream in(file);` |
| 写文件 | `<fstream>` | `std::ofstream` | `std::ofstream out(file, std::ios::app);` |
| 字符串当流 | `<sstream>` | `std::stringstream` | `std::stringstream ss(line);` |
| 路径/目录 | `<filesystem>` | `fs::path` | `fs::path p = dir / name;` |
| 控制台 | `<iostream>` | `std::ostream` | `std::cout` |

## 流是类层次

```
            basic_ios（公共状态与格式标志）
             /        \
   basic_istream     basic_ostream     ← >> / <<
            \        /
          basic_iostream
             /            \
   ifstream / ofstream   stringstream
   （fstream 三者合一）

std::cout / std::cin 是预置好的 ostream / istream 实例
```

## 语法

文件输出，打开方式决定覆盖还是追加：

```cpp
std::ofstream out(file, std::ios::out | std::ios::app);   // 追加；不加 app 则覆盖
out << img[i][j] << "\t";
out.close();
```

文件输入，`getline` 读整行，`>>` 读单个值：

```cpp
std::ifstream in(file);
std::string line;
while (std::getline(in, line)) { ... }   // 到文件末尾返回 false
```

字符串流，把 string 当流来读：

```cpp
std::stringstream ss(line);
int tmp;
while (ss >> tmp) { ++cnt; }             // 抽空后返回 false
```

文件系统：

```cpp
fs::path dir  = fs::current_path();
fs::path file = dir / "R_image.txt";     // 运算符 / 重载为拼路径
if (!fs::exists(dir)) { ... }
```

## 按行读 vs 按 token 读

`in >> tmp` 以「空白分隔的 token」为单位，会连换行一起跳过，分不清哪几个数属于同一行；`getline` 以换行为单位，一次取回一整行。

处理表格/矩阵文本的标准套路是「先按行切 → 行内再按 token 切」：

```cpp
while (std::getline(in, line)) {
  std::stringstream ss(line);
  int tmp, cnt = 0;
  while (ss >> tmp) ++cnt;
  if (cnt != columns) { /* 行内列数不一致 */ }
}
```

直接 `in >> tmp` 无法发现「某行数字个数不对」的非矩形文件；`getline` + 列数校验才能靠行边界检查格式。

## 坑

- 写文件不加 `std::ios::app` 会覆盖原内容。
- `getline` 丢弃换行符；与 `>>` 混用时注意残留的换行。
- 路径拼接用 `fs::path` 的 `/`，不要手写字符串加斜杠。
- 文件流对象默认在栈上，离开作用域自动关闭；手动 `close()` 后不要再读写。

> PS：二进制读写用 `std::ios::binary`；大文件逐行流式处理，不要一次读进内存。

文件、字符串、路径操作都是类与对象；流用统一的 `<<` / `>>`，只是目的地不同；矩阵文本先 `getline` 切行、再用 `stringstream` 切列。