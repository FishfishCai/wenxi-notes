---
id: dx7g88m48zxzar7q
title: ssh setting
tags: []
refs: []
backrefs: []
---
# Setting
```CLI
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

# ssh public key
```CLI
cat ~/.ssh/id_ed25519.pub
```
