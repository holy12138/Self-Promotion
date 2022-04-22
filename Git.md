## 基本概念：

- 仓库（Repository）：存放项目代码，每个项目对应一个仓库
- 收藏（Star）：收藏项目
- 复刻（Fork）：复制克隆别人的项目变成自己的仓库（独立存在）
- 发起请求（Pull Request）：在Fork的项目仓库里更新，可以申请合并到原仓库，等待原仓库管理员审核
- 关注（Watch）：关注某个开源项目的更新动态
- 事务卡片（Issue）：发现代码BUG的问题，供大家讨论，修复处理后可以close掉



## 初始化git账户：

使用git bash打开命令行界面（设置在github仓库主页显示谁提交了该文件）

- 查看当前信息：git config --list
- 设置用户名：git config --global user.name XXX
- 设置用户名邮箱：git config -- global user.email XXXX



## 基础理论：

- 三个区域：
  - 工作区：本地文件夹，存放当前项目代码，实际写代码的地方，写好的代码git add到暂存区
  - 暂存区：临时存储，git commit -m XXX提交到git仓库
  - git仓库：历史版本

- git管理文件的三种状态：
  - 已修改：modified
  - 已暂存：staged
  - 已提交：committed



## 初始化新的git仓库：

- 创建文件夹：mkdir XXX
- 初始化仓库：进入该文件夹（cd XXX），git init初始化获得.git隐藏文件夹（用于跟踪工作目录文件变化）
- 团队内协作：
  - 将远程仓库项目下载到本地：git clone XXX
  - 当本地库已经存在，可以通过git pull操作将远程库的修改同步到本地
  - 查看当前工作区状态：git status
  - 工作区文件加入暂存区：git add XXX，可以用.表示所有文件
    - add之后如果还对当前文件进行修改：
      - 直接commit的话就提交当前add到暂存区的文件
      - 再次使用add的话就使用最新修改的版本覆盖暂存区的文件
  - 暂存区提交到本地仓库：git commit -m XXX
  - 查看历史提交记录：git log
  - 本地仓库提交到远程仓库：git push
- 团队外协作：
  - 外部人员通过fork操作将远程库复制一份独立版本
  - 再clone到本地库
  - 在本地进行修改，然后push到远程库
  - 修改后的远程库发起pull request请求给原始远程库的管理员进行审核
  - 原始远程库的管理员审核通过后使用merge操作将外部人员修改合并到自身远程库
  - 团队内人员使用pull操作同步外部人员的修改
- 删除文件：
  - 删除工作区和暂存区的文件（要保证工作区和暂存区文件一致）：git rm XXX
  - 强制删除工作区和暂存区的文件（不需要保持一致）：git rm -f XXX
  - 删除暂存区文件：git rm --cached XXX
  - 增加新版本（有痕迹）：git rm XXX -> git commit -m XXX
  - 回到原版本（无痕迹）：git rm XXX -> git reset --soft HEAD~
- 恢复文件：
  - 将最近一次提交到git仓库的文件恢复到先前状态：git reset HEAD XXX（不指定文件名的话，就表示所有文件）
  - 回到上一个版本（但此时只是仓库和暂存区回到上一个版本，会提示工作区的最新版本没有add）：git reset HEAD~1，表示上一个版本，可改变数字来选择版本
  - git reset --mixed HEAD~1：默认，表示指向上一个版本，且回到暂存区
  - git reset --soft HEAD~1：表示指向上一个版本，但不回到暂存区，相当于撤销了一次提交
  - git reset --hard HEAD~1：表示指向上一个版本，且回到暂存区，并将暂存区文件还原到工作区
  - git reset 指定id号（log中），回到指定版本（也可以到当前版本后面的版本，但要使用--hard才能还原工作目录文件）
  - git reset 指定id号（log中） 文件名/路径，恢复指定文件
- 更正：将暂存区提交到仓库，并更正最近一次提交的commit说明（也可以不修改），不增加新版本：git commit -amend [-m XXX]
- 重命名文件：git mv [name1] [name2]
- 查看不同版本之间的区别：
  - git diff：默认比较暂存区和工作目录
  - git diff 版本1的id 版本2的id：查看指定版本之间的区别
  - git diff 版本id：当前工作目录和指定版本之间区别，最新版本直接使用HEAD代替id
  - git diff -cached [版本id]：比较暂存区和仓库
- 设置权限：
  - 进入到.git/conifg
  - url = https://用户名:密码@github.com/用户名/仓库名.git



## 分支管理（分支是指向版本节点的指针）

- 创建分支：git branch XXX
- 切换分支：git checkout XXX
- 创建并切换：git checkout -b XXX
- 合并分支：git merge XXX
- 删除分支： git branch --delete
- 匿名分支（切走的话，所有操作都将消失，适合做实验）：git checkout HEAD~，操作后可以通过git branch XXX 匿名分支id号来创建新分支以保留操作
- checkout：移动指针+覆盖工作区和暂存区
  - 将指定版本中的某些文件拷贝到暂存区和工作区：git checkout HEAD~ XXX
  - 使用当前暂存区覆盖工作区修改（即修改当前工作区后，取消修改）：git checkout -- XXX
  - 与reset区别：
    - 文件级任务：reset只能将指定的文件恢复到暂存区，checkout恢复到工作区和暂存区
    - 提交版本级任务：reset --hard直接进行覆盖，而checkout会尝试合并，并进行检查，如果有冲突则需要先进行操作
    - reset移动head所在的分支指向（直接忽略当前版本），而checkout只移动head自身来指向另一个分支
- 查看当前分支情况：git log --decorate --oneline --graph --all



## 搭建个人网站Github pages：

- 创建个人站点 -> 新建仓库（仓库名为：用户名.github.io）
- 当前仓库下新建index.html文件
- 访问主页网址：https://用户名.github.io
- 搭建项目网站：
  - 进入项目主页，点击setting
  - setting页面里面，点击【launch automatic page generator】来自动生成主题页面
  - 新建站点基础信息设置，先择主题，生成网页
  - 访问主页网址：https://用户名.github.io/仓库名

