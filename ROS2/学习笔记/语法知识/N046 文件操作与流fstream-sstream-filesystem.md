---
tags:
  - 语法知识
  - C++语法
  - 流Stream
  - 文件File
  - IO输入输出
  - 类Class
  - 对象Object
---

# 文件操作与流（fstream / sstream / filesystem） · 语法知识 · N046

**时间:** 2026-10-10 21:44
**标签:** #语法知识 #C++语法 #流Stream #文件File #IO输入输出 #类Class #对象Object
**关联:** [[N040 实例instance是什么]] [[N041 栈和堆的底层实现与区别]] [[N042 同步异步与阻塞非阻塞]]

## 疑惑点

读文件、写文件、把一行字符串解析成数字、拼路径、判断文件存不存在——这些操作看起来像「系统自带的功能」。它们到底是不是也都用「类 + 类对象」实现的?`<fstream>` `<sstream>` `<filesystem>` 这几个库之间是什么关系?

## 实际情况

1. **是的,全都是类。** C++ 标准库把「输入输出」和「文件系统」整体封装成了类:你写的每个变量都是某个类的**实例**,操作靠对象的方法或运算符重载,没有任何魔法。对照表:

   | 你想做的事 | 头文件 | 用的类 | 典型对象 |
   | ---------- | ------ | ------ | -------- |
   | 读文件 | `<fstream>` | `std::ifstream` | `std::ifstream in(file);` |
   | 写文件 | `<fstream>` | `std::ofstream` | `std::ofstream out(file, std::ios::app);` |
   | 字符串当流解析 | `<sstream>` | `std::stringstream` | `std::stringstream ss(line);` |
   | 路径 / 目录操作 | `<filesystem>` | `fs::path` | `fs::path p = dir / name;` |
   | 控制台输出 | `<iostream>` | `std::ostream`(预置实例) | `std::cout` |

2. **「流(stream)」是一个类层次(继承)。** 基类定义统一的 `<<` / `>>` 接口,派生类决定「流连到哪里」:

   ```
               basic_ios（基类:流的公共状态与格式标志）
                /        \
      basic_istream     basic_ostream      ← 读接口 >> / 写接口 <<
             \           /
          basic_iostream（可读可写）
             /              \
     ifstream / ofstream   stringstream    ← 连「文件」 / 连「内存里的 string」
     (fstream = 三者合一)

   std::cout / std::cin 不是类,是标准库已经替你造好的 ostream / istream「实例」
   ```

3. **逐条语法(来自 try 工程 valid.cpp / image.cpp 的真实写法):**

   **a. 文件输出 `ofstream` —— 打开方式决定覆盖还是追加:**
   ```cpp
   std::ofstream out(file, std::ios::out | std::ios::app);  // 追加;不加 app 则覆盖
   if (!out.is_open()) { /* 打不开就处理 */ }
   out << img[i][j] << "\t";   // 运算符 << 重载,和 cout 用法完全一样
   out.close();
   ```

   **b. 文件输入 `ifstream` —— `getline` 读一整行到 string,`>>` 读单个值:**
   ```cpp
   std::ifstream in(file);
   std::string line;
   while (std::getline(in, line)) { ... }  // 每次读一行;读到文件末尾返回 false,循环结束
   ```

   **c. 字符串流 `stringstream` —— 把 string 当成「流」来读,配合 `>>` 抽数字:**
   ```cpp
   std::stringstream ss(line);
   int tmp;
   while (ss >> tmp) { cnt++; }   // 从字符串里一个个抽 int,抽空后返回 false
   ```

   **d. 文件系统 `filesystem` —— `path` 对象 + 运算符 `/` 拼路径 + 常用函数:**
   ```cpp
   fs::path dir  = fs::current_path();    // 当前工作目录,返回一个 path 对象
   fs::path file = dir / "R_image.txt";   // 运算符 / 重载:拼接路径
   if (!fs::exists(dir)) { ... }          // 判断路径是否存在
   ```

4. **三个「目的地」、同一套接口。** `<iostream>` 定义流的骨架(`<<` 和 `>>`),`<fstream>` / `<sstream>` / `std::cout` 只是「流连向哪」不同:屏幕、文件、内存字符串——三者写法一模一样,这正是「流」这个抽象统一了它们。

> **Note(连接 / 深化):**
> - 连接:`std::cout` 就是标准库预置好的一个 ostream 实例,见 [[N040 实例instance是什么]];`ifstream` / `stringstream` 这类对象默认建在栈上,见 [[N041 栈和堆的底层实现与区别]];读文件时程序会卡住等磁盘返回,是典型的同步阻塞,见 [[N042 同步异步与阻塞非阻塞]]。
> - 深化:「流」是 C++ 对输入输出的统一抽象——不管目标是屏幕、文件还是内存字符串,都用同一套 `<<` / `>>`;`<filesystem>` 则是另一套针对「路径」的抽象,它内部本质就是字符串(路径 = 文本)。

## 思考

（留白 —— 为什么 `rw_image` 里不直接 `in >> tmp` 读文件,而是先 `getline` 拿一行 string、再用 `stringstream` 解析?两种读法有什么区别?）

**补充(2026-10-10):** 两种读法的**单位**不同。`in >> tmp` 以「空白分隔的 token」为单位,会**连换行一起跳过**,读进来是一坨,分不清「哪几个数属于同一行」;而 `rw_image` 要统计「每行几列、并校验每行列数一致(矩形图像)」,必须按行处理。`getline` 以「换行」为单位,一次取回一整行(丢弃换行符),拿到行的边界;再把这行 `string` 包成 `stringstream`,`while (ss >> tmp)` 只在**这一行内部**抽数字,抽到行尾返回 false,`cnt` 就精确等于这一行的列数。二者组合 = 「先按行切 → 再行内按 token 切」,是处理表格/矩阵文本的标准套路。若直接 `in >> tmp`,遇到「某行数字个数不对」的非矩形文件也发现不了;而 `getline` + `cnt != columns` 正是靠行边界才校验出 `Invalid image(txt) format!`。

## 总结

**本质:** 文件读写(`fstream`)、字符串解析(`sstream`)、路径操作(`filesystem`)全部是「类 + 对象」——流是一个类层次,`ifstream` / `ofstream` / `stringstream` 是它的派生实例,`std::cout` 是预置实例;它们共用 `<<` / `>>` 接口,区别只在于「流连向哪里」。
**标签:** #语法知识 #C++语法 #流Stream #文件File #IO输入输出 #类Class #对象Object
