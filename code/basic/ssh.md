#### 查看ssh公钥
```
1) 使用ls 查看 ~/.ssh 目录内容
/bin/ls -al ~/.ssh

2) 查看公钥内容
/bin/cat ~/.ssh/id_ed25519.pub
```
#### 配置连接文件
```
Host 自定义名字
	HostName 146.235.210.133
	User wenxi
	IdentityFile ~/.ssh/id_ed25519
	IdentitiesOnly yes
```