## Setting
```CLI
Host host_name
    HostName host_address
    User user_name

Host github.com
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes

Host *
    ServerAliveInterval 60
    ServerAliveCountMax 5
    ControlMaster auto
    ControlPath ~/.ssh/cm-%C
    ControlPersist 24h
    AddKeysToAgent yes
    UseKeychain yes
    ConnectTimeout 30
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
