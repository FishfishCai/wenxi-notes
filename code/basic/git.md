#### 初始化
```git
# 在github上初始化一个项目

# 在终端，即文件夹内部初始化git
git init
git add .
git commit -m "initial commit"

# 连接到仓库
git remote add origin https://github.com/FishfishCai/仓库名

# 设置默认分支
git branch -M main

# 首次上传
git push -u origin main
```
#### 上传
```
git add .
git commit -m "fix bugs"
git push
```
#### 拉取
```
# 正常拉取
git pull --rebase
git pull --rebase origin main

# 和remote完全一致
git reset --hard
```
#### 在服务器上连接github
``````
# 先连接ssh
ssh-keygen -t ed25519 -C "13512190480@163.com"
cat ~/.ssh/id_ed25519.pub  # 至github添加该key

# 设置参数
git config --global user.name "CaiWenxi"
git config --global user.email "13512190480@163.com"

# 克隆仓库
git clone git@github.com:FishfishCai/仓库名.git 仓库名
```