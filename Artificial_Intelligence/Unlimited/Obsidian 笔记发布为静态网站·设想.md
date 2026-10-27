把 vault 子目录发布成带关系图谱、双向链接、搜索、KaTeX、Mermaid 的静态网站是可行的。2026-10-24 用 `Artificial_Intelligence/` 试水过一次，效果合格但暂时不维护，这里留下方案与踩坑。

## 选型

GitHub 网页端渲染不了 `![[...]]` 嵌入、callout、关系图谱等 Obsidian 语法。目标是保留双链、反向链接、图谱、公式/Mermaid、全文搜索。选 **Quartz v5**（`jackyzha0/quartz`）+ GitHub Pages：原生支持 wikilink、backlinks、graph view、search，输出纯静态文件。先只发 AI 子集，单独仓库，失败就整体删。

## 当时的结果

| 项目 | 结果 |
| --- | --- |
| 内容 | `Artificial_Intelligence/` 下 82 篇笔记 + 附件，约 107 MB |
| 仓库/站点 | `github.com/Korotomx/AIAIAI`（已撤下）；`korotomx.github.io/AIAIAI/`（已下线） |
| 构建 | Quartz v5 + GitHub Actions，push `main` 自动部署 |
| 验证 | 图谱、双链、反向链接、搜索、公式、Mermaid、图片、手机布局正常 |

撤下不是效果问题，而是暂时不想维护第二个发布渠道。

## 重做步骤

1. **镜像内容到独立目录**，不要在 vault 里直接构建：

   ```bash
   rsync -a --exclude='*.pdf' --exclude='*.canvas' --exclude='.obsidian' \
     <vault>/Artificial_Intelligence/ site/content/
   ```

2. 克隆 Quartz v5，改 `quartz.config.yaml` 的标题、`locale: zh-CN`、`baseUrl`、主题色；关掉统计/字体/OG/cname 等插件，保留 `note-properties` 剥 frontmatter。
3. 第三方资源本地化：KaTeX / Mermaid / d3 / pixi 放进 `vendor/`，构建后把 CDN 地址改成站内路径。
4. GitHub Actions：`npm ci` → `npx quartz build` → 本地化脚本 → `upload-pages-artifact` → `deploy-pages`。

## 踩过的坑

| 坑 | 现象 | 处理 |
| --- | --- | --- |
| Pages 自动开启 | `enablement: true` 失败 | 它要求 PAT，`GITHUB_TOKEN` 不行；手动开 Pages |
| 子路径部署 | 图谱/公式资源 404 | 把 `baseUrl` 改成 `<owner>.github.io/<repo>`，资源前缀同步 |
| explorer 自动滚动 | 打开笔记页窗口自己下滚约 320px | 插件对当前条目调 `scrollIntoView()`；改成只滚侧栏容器 |
| 同名附件 | `![[DLC2.jpg]]` 裂图 | 两个目录同名文件解析到不存在的根路径；发布副本去掉重复目录 |
| 大小写路径 | `/CUDA/主页` 变成跳转页 | Quartz 输出小写 slug，旧链接靠别名页跳转 |
| 国内安装 | `npm install` 慢 | 用 npmmirror 镜像 |
| 仓库体积 | 内容 + 依赖约 143 MB | 排除 PDF/canvas；单文件 < 10 MB，无需 LFS |

## 安全与隐私

- 公开仓库 = 内容公开，发布前扫邮箱、手机号、密钥、内网地址；不发布 `.obsidian/`、PDF、Canvas、压缩包。
- 关闭统计与评论，资源站内自托管；加 `no-referrer` meta，生成 `robots.txt` 与 `sitemap.xml`；私人笔记不要用公开仓库（Pages 私有仓库需要 GitHub Pro）。

技术上完全可行，撤下只是产品决策。恢复时按上面的步骤和避坑表即可，仍建议单独仓库发布；做全 vault 前先处理同名附件与私有内容。