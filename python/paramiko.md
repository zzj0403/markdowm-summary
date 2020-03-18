# paramiko

## 简介

ssh是一个协议，OpenSSH是其中一个开源实现，paramiko是Python的一个库，实现了SSHv2协议(底层使用cryptography)。

由于paramiko属于第三方库，所以需要使用如下命令先行安装

```python
pip3 install paramiko
```

## 简单连接使用

```python
import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 密钥文件
private_key = paramiko.DSSKey.from_private_key_file('zzj01')
# 连接服务器
ssh.connect(hostname='192.168.119.5', port=9603, username='zzj', pkey=private_key)
# 获取命令结果
stdin, stdout, stderr = ssh.exec_command('df -h')
print(stdout.readlines())
# print(result)
# 关闭连接
ssh.close()
```

