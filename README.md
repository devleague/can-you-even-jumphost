# can-you-even-jumphost

### Summary
Jason is a 41 year old systems administrator. He is from Denver, Colorado. He has a son named Rocky.

We found the following sticky note on his desk:
```
Access to private server

Bastion IP:
xxx.xxx.xxx.xxx (fill in as deployment changes)
Password:
duh
```

Your challenge: **Python**

### Requirements
All phases must be programatic aka Python scripting. Other tools can be used but a final PoC for any phase must include a Python script.

### Resources
http://bit.ly/blackhatpython


### Keywords
- proxy
- bastion
- jump host

### Possible Tools
- `os`
- `socket`
- `paramiko`
- ....other?


Infrastructure (Bastion/Jump Host) Setup:
2 Droplets
  - 1 public
    - nc permissions changed to only root or removed
    - 1 user created (jason) with no sudo or other group privs
    - SSH password access allowed
    - SSH pub/priv key generated for jason, added to private
    - Firewall deny by default for egress traffic
    - Firewall allow egress to private subnet/host
  - 1 private
    - 1 user created
    - No SSH password access allowed
    - SSH pub key for jason(public) added to `.ssh/authorized_hosts`
    - Firewall deny by default for ingress traffic
    - Firewall allow ingress from private subnet/host
