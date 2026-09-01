# VPN rules
```CLI
prepend:
  # ssh
  - DST-PORT,22,DIRECT

  # tailscale
  - PROCESS-NAME,tailscaled,DIRECT
  - DOMAIN-SUFFIX,tailscale.com,DIRECT
  - DOMAIN-KEYWORD,tailscale,DIRECT
  - IP-CIDR,100.64.0.0/10,DIRECT,no-resolve

  # email
  - DOMAIN,imap.gmail.com,🇭🇰 香港智能
  - DOMAIN,smtp.gmail.com,🇭🇰 香港智能
  - DOMAIN,pop.gmail.com,🇭🇰 香港智能
  - DOMAIN-SUFFIX,imap.googlemail.com,🇭🇰 香港智能
  - DOMAIN-SUFFIX,smtp.googlemail.com,🇭🇰 香港智能

append: []

delete: []

```
