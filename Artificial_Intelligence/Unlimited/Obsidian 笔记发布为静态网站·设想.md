---
tags:
  - Obsidian
  - 静态网站StaticSite
  - Quartz
  - GitHubPages
  - 发布Publishing
---

# Obsidian 笔记发布为静态网站 · 设想

**时间:** 2026-10-24 试做并撤下
**标签:** #Obsidian #静态网站StaticSite #Quartz #GitHubPages #发布Publishing
**关联:** [[主页]]（AI 栏目导航）· [[README]]（vault 总览；网站若重做应指向它而非子目录）

## 一句话

把 vault 里某个子目录发布成**带关系图谱、双向链接、搜索、KaTeX、Mermaid** 的静态网站是可行的：2026-10-24 用 `Artificial_Intelligence/` 做过一次完整试水，效果合格，但暂时决定不维护，先留下方案和踩坑记录，以后想做时照着重做即可。

## 实际情况

### 0. 为什么会有这个想法

GitHub 网页端渲染不了大部分 Obsidian 语法：`![[...]]` 嵌入、callout、关系图谱都没有；想给别人看笔记时体验很差。目标不是「再做一个博客」，而是**尽量保留 Obsidian 的阅读体验**：

- 双链可点、反向链接可见
- 关系图谱可交互
- 公式、表格、代码块、Mermaid 正常
- 最好能全文搜索

### 1. 选型结论

用 **Quartz v5**（`jackyzha0/quartz`）生成静态站，GitHub Pages 托管。原因是它原生支持 Obsidian 风格 Markdown、wikilink、backlinks、graph view、search，且输出纯静态文件，不需要服务器。

当时的原则：

- **先只发 AI 子集**试水，不动原 vault 仓库
- 单独建一个仓库，失败就整体删掉
- 不引入统计、评论、第三方字体，尽量零外部请求

### 2. 当时实际做出来的东西

| 项目 | 结果 |
| --- | --- |
| 内容 | `Artificial_Intelligence/` 下 82 篇笔记 + 附件，约 107 MB |
| 仓库 | `github.com/Korotomx/AIAIAI`（公开，已撤下） |
| 站点 | `https://korotomx.github.io/AIAIAI/`（已下线） |
| 构建 | Quartz v5 + GitHub Actions，push `main` 自动部署 |
| 验证 | 图谱、双链、反向链接、搜索、公式、Mermaid、图片、手机布局均正常 |

效果本身是达标的；撤下的原因不是效果，而是**暂时不想维护第二个发布渠道**，等以后有明确分享需求再恢复。

## 方案与坑

### 3. 重做时的步骤

1. **镜像内容到独立目录**，不要直接在 vault 里构建：
   ```bash
   rsync -a --exclude='*.pdf' --exclude='*.canvas' --exclude='.obsidian' \
     <vault>/Artificial_Intelligence/ site/content/
   ```
2. 克隆 Quartz v5，改 `quartz.config.yaml`：标题、`locale: zh-CN`、`baseUrl`、主题色。
3. 关闭不需要的插件：`analytics` 置空、`quartz-fonts`、`og-image`、`cname`、`article-title`；保留 `note-properties`（隐藏显示）用来剥 frontmatter。
4. 第三方运行时资源本地化：KaTeX / Mermaid / d3 / pixi 放进 `vendor/`，构建后用脚本把 HTML/JS 里的 CDN 地址改写成站内路径。
5. GitHub Actions：`npm ci` → `npx quartz build` → 本地化脚本 → `upload-pages-artifact` → `deploy-pages`。
6. 仓库 **Settings → Pages → Source** 选 **GitHub Actions**（只需一次）。

### 4. 踩过的坑（重做时直接避开）

| 坑 | 现象 | 处理 |
| --- | --- | --- |
| Pages 自动开启 | `configure-pages` 的 `enablement: true` 失败 | 它要求 PAT，`GITHUB_TOKEN` 不行；手动开 Pages |
| 子路径部署 | 图谱/公式资源 404 | CI 里把 `baseUrl` 改成 `<owner>.github.io/<repo>`，资源前缀同步 |
| explorer 自动滚动 | 打开笔记页窗口自己下滚约 320px，标题被顶出屏幕 | 插件对当前条目调 `scrollIntoView()`；改成只滚侧栏容器 |
| 同名附件 | `![[DLC2.jpg]]` 裂图 | 两个目录有同名文件，wikilink 解析到不存在的根路径；发布副本去掉重复目录 |
| 大小写路径 | `/CUDA/主页` 变成跳转页 | Quartz 统一输出小写 slug，旧链接靠别名页跳转 |
| 国内安装 | `npm install` 慢 | 用 npmmirror 镜像装依赖 |
| 仓库体积 | 内容 + 依赖约 143 MB | 排除 PDF/canvas；单文件不超过 10 MB，无需 LFS |

### 5. 安全与隐私清单

- 公开仓库 = 内容公开，发布前先扫邮箱、手机号、密钥、内网地址
- 不发布 `.obsidian/`、PDF、Canvas、压缩包
- 关闭统计与评论；字体、脚本、样式全部站内自托管
- 给页面加 `<meta name="referrer" content="no-referrer">`
- 生成 `robots.txt` 与 `sitemap.xml`
- 若以后要放私人笔记，**不要用公开仓库**；Pages 私有仓库需要 GitHub Pro

## 结论

技术上完全可行，效果也够用；这次撤下只是产品决策，不是方案失败。以后若要做：

- 恢复成本不高，按第 3 节步骤 + 第 4 节避坑即可
- 建议仍然**单独仓库**发布，不污染 vault 仓库
- 如果要做全 vault，先处理同名附件和私有内容，再一次性发布

## 相关

- [[主页]] — AI 栏目总导航
- [[README]] — vault 总览与学习仪表盘
