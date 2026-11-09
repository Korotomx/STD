<iframe width="560" height="315" src="https://player.bilibili.com/player.html?bvid=BV16eKb6PEUo&amp;page=13&amp;high_quality=1&amp;danmaku=0" title="Bilibili video player" frameborder="0" allowfullscreen=""></iframe>

原链接：https://www.udemy.com/course/master-golang-build-rest-apis-websocket-grpc-mongodb/?couponCode=MT260720JP  
面向真实工程师的AI编程

## Transcript

**0:00** · 与clade代码协作的重要部分之一是运行bash命令 Bash命令将你的代理从被动的代码编写者转变为能够实际寻求反馈循环的实体能够真正参与项目工作并能充分利用bash的所有功能来查找信息和执行任务现在我们可以手动询问好的为我运行开发服务器由于它非常智能它会理解好的我需要读取package.json文件我需要找到开发服务器的位置然后我需要像这样运行它

**0:28** · 我们将详细解释这里的作用以及这种审批设置但可以肯定的是，有时你清楚想要运行的命令并希望直接运行它然后将结果放入Claude的上下文中实现方法是我刚刚重启了Claude代码实例我只需输入一个感叹号现在进入了bash模式在此输入的内容将转换为bash命令并实际由Claude执行例如为什么不在这里运行npm run type check呢

**0:57** · 现在按下回车后命令立即执行由于我的设置中未运行npm install 出现了大量错误这些错误现在出现在Claude的上下文中我要让它帮助我解决这些错误它可以看到错误并实际处理它们就是这样它发现package.json中引用了zoris但未安装我应该运行npm install，现在好了这对有明确开始和结束的命令效果很好但持久化命令呢

**1:26** · 比如长时间运行的开发服务器，我们可以运行npm 在bash模式下执行dev命令在运行过程中可以按Ctrl+B将其放到后台运行在这个Clade代码版本中出现提示显示命令由用户ID手动后台运行该任务的输出将保存到本地文件在状态行下方可以看到有一个显示的后台任务

**1:55** · 只需向下箭头即可查看按回车键即可查看现在我可以实际查看终端我可以查看这里的情况可以看到它运行在本地主机5175端口这里有很多选项我可以按x停止它如果我需要的话或者直接按左键返回现在我又回到了claw代码实例这在调试开发服务器问题时非常有用比如说或者长时间运行的命令因为claude可以看到所有日志的写入位置可以在界面尝试操作

**2:24** · 或者发送curl请求然后能看到开发服务器的输出我刚重置了实例我们可以看到另一个功能是暂停claude代码如果例如我想运行某个不希望claude看到结果或者不想展示并且有内部状态需要保留的claw数据这时可以使用暂停功能我在这里按ctrl+z，claude代码已被暂停现在我可以运行任何想要的命令这里直接echo foo

**2:53** · 这些内容不会显示给claude代码如果要恢复claude代码只需运行fg 就能恢复claude代码实例及其所有内容这非常实用如果你想直接好的不关心claude代码执行任意命令然后用fg恢复这个决策流程确实如此如果你需要bash命令的输出对claude可见可以使用感叹号启用bash模式用ctrl+b放到后台再次管理这些后台任务

**3:23** · 这对开发服务器非常有用我不每次都用但当我使用时通常是调试开发服务器问题但如果你想完全隐藏命令只需快速按ctrl+z暂停当然，这些都是Windows快捷方式所以如果你用的是Mac可能需要做些不同的操作这些都是在Claude代码中管理bash命令的不同方法做得很好我们下次再见