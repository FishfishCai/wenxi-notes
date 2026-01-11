#### 初始化
1. 在github初始化一个项目
2. 在vscode中（gitignore同一层）初始化git
```git
git init
git add .
git commit -m "initial commit"
```
3. 连接到仓库
```git
git remote add origin https://github.com/FishfishCai/仓库名
```
4. 设置默认分支
```git
git branch -M main
```
5. 首次上传
```git
git push -u origin main
```
#### 上传
```
git add .
git commit -m "说明这次改了什么"
git pull --rebase # 先pull
git push
```
#### 拉取更新
```
git reset --hard
git pull --rebase
git pull --rebase origin main
```
#### 终止 add
```git
rm -f /Users/wenxicai/Documents/research/TemFNO/code/.git/index.lock   
git restore --staged . 
```
#### 在服务器上连接github
```
ssh-keygen -t ed25519 -C "13512190480@163.com"
cat ~/.ssh/id_ed25519.pub
到github上加上这个key
git clone git@github.com:FishfishCai/仓库名.git 仓库名
```
#### 在服务器上上传文件
```
git config --global user.name "CaiWenxi"
git config --global user.email "13512190480@163.com"
```