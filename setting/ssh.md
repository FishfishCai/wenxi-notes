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

# only offer this key to GitHub, never other keys loaded in ssh-agent
Host github.com
	IdentityFile ~/.ssh/id_ed25519
	IdentitiesOnly yes
```

## GitHub
```CLI
ssh -T git@github.com         # check which account the key logs in as
ssh -O exit git@github.com    # close the GitHub mux so a config change takes effect
```

## Public Key
```CLI
cat ~/.ssh/id_ed25519.pub
```
