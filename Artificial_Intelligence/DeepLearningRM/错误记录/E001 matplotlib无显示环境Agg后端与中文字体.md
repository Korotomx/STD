# E001 · 运行时 — matplotlib 在 WSL 无显示环境下的坑（Agg 后端 + 中文字体）

**时间:** 2026-10-17 21:10
**分类:** #运行时

## 问题

跑 `03_dataset.py` 第 6 节可视化时，依次踩了三个坑：

1. `_tkinter.TclError: couldn't connect to display ":10"` —— matplotlib 默认用 Tk 后端去连 X 显示，报错退出
2. 中文标题变「豆腐块」—— 默认字体 DejaVu Sans 没有中文字形，标题里的中文全部缺失
3. 换成中文字体 `Droid Sans Fallback` 后，英文/数字/符号（`T`、`=` 等）反而缺失

## 原因

1. 本机 GUI 走 xrdp 的 Xvnc `:10`，当前 shell 没连上 X；matplotlib 默认 `TkAgg` 后端要开窗口
2. 默认字体 `DejaVu Sans` 只含 Latin，没有 CJK 字形
3. `Droid Sans Fallback` 是「CJK fallback」字体，Latin 字形不全——单独用它，英文就缺

## 解决方案

在 `import matplotlib.pyplot` 前切到 Agg 后端，并配好字体 fallback 列表：

```python
import matplotlib
matplotlib.use("Agg")        # 无显示环境：只存图、不弹窗
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Droid Sans Fallback"]  # 英文用 DejaVu、中文 fallback 到 Droid
plt.rcParams["axes.unicode_minus"] = False                                  # 负号正常显示
```

要点：
- **Agg 后端**：无 GUI 环境（服务器 / WSL 无显示）画图一律用 `Agg`，`savefig` 存 PNG，不弹窗
- **字体列表顺序不能反**：`["DejaVu Sans", "Droid Sans Fallback"]` —— 英文数字用 DejaVu，中文自动 fallback 到 Droid
