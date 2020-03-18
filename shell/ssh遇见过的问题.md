# ssh登入报错

```shell
ssh -v xxx@xxx
sign_and_send_pubkey: no mutual signature supported
```

* 原因：新的OpenSSH版本（7.0+）不推荐使用DSA密钥，默认情况下不使用DSA密钥（不在服务器或客户端上）。这些密钥不再被使用，因此如果可以，建议尽可能使用RSA密钥

```shell
1.修改~/.ssh/config
vim .ssh/config
Host  servername.com
  HostName 192.168.1.10
  IdentityFile ~/dsa/id_dsa
  PubkeyAcceptedKeyTypes +ssh-dss
2.保存退出，设置权限为600
chmod 600 .ssh/config
```

