`pnpm db:seed` 只往 SQLite 写数据、不起网页；`cherry-pick` 卡住不是等冲突，是 git fetch 连不上 GitHub。

## seed 和 dev 是两件事

- `pnpm db:seed` → `tsx scripts/seed.ts`，只是往 `data.db` 插用户、课程、测验等行，**不启动服务器**，所以没有任何页面。
- `pnpm dev` → `react-router dev`，起在 5173，页面上看到的才是 seed 进去的数据。
- 看到 `✓ Seed complete!` 就说明写成功了，不用等网页。

重来一遍的正确顺序：

```bash
rm data.db
pnpm db:migrate
pnpm db:seed
pnpm dev
```

（seed 用固定 ID 插入、没有清空逻辑，直接重复跑会撞唯一约束。）

## cherry-pick 没动静

`ai-hero-cli cherry-pick` 的第一步不是问你要哪一课，而是：

```bash
git fetch upstream live-run-through
```

国内直连 `github.com` 会一直挂在 TCP 握手，屏幕上什么都不打印，看起来像死机。诊断一行就够：

```bash
timeout 15 git ls-remote https://github.com/ai-hero-dev/cohort-004-project.git HEAD
```

15 秒无输出 = 网络问题，不是仓库问题、更不是冲突。

解法是把 upstream 换成镜像地址，只作用于这一次命令：

```bash
pnpm exec ai-hero-cli cherry-pick --branch=live-run-through \
  --upstream=https://ghfast.top/https://github.com/ai-hero-dev/cohort-004-project.git
```

- 不能再用 `pnpm cherry-pick`：`package.json` 里把 upstream 写死成了 GitHub 原始地址。
- fetch 完成后才会出现 `Which lesson do you want to cherry-pick?` 的搜索列表，选中之后才谈得上 merge 冲突。
- CLI 会自己加 `upstream` remote，结束后再删掉，所以镜像地址不会留在仓库里。

## 可迁移的经验

- npm、git、VS Code 扩展安装在这台机器上都栽在同一件事上：**先确认网络，再怀疑工具**。
- 镜像只用于单次命令，别写进全局 `url.insteadOf`——那会把 `push` 也一起改写。
- 用 `ps aux | grep git-remote-https` 能立刻看清进程到底卡在哪一步。
