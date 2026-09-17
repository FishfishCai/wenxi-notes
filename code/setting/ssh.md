## Setting
```CLI
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 30
    ControlMaster auto
    ControlPath ~/.ssh/cm-%C
    ControlPersist 24h
    AddKeysToAgent yes
    UseKeychain yes
    ConnectTimeout 20

Host host_name
	HostName host_address
	User user_name
	IdentityFile ~/.ssh/id_ed25519
```

## Public Key
```CLI
cat ~/.ssh/id_ed25519.pub
```
