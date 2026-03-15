#### 查看ssh公钥
```CLI
cat ~/.ssh/id_ed25519.pub
```
#### 配置连接文件
```
Host *
	ServerAliveInterval 60
	ServerAliveCountMax 999
	TCPKeepAlive yes
	ControlMaster auto
	ControlPath ~/.ssh/cm-%r@%h:%p
	ControlPersist 12h
	IdentitiesOnly yes
	AddKeysToAgent yes
	UseKeychain yes
	ConnectTimeout 20

Host host_name
	HostName host_address
	User user_name
	IdentityFile ~/.ssh/id_ed25519
```