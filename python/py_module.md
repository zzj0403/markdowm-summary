# 模块

## paramiko

参考过的博客

- [官方文档](http://docs.paramiko.org/en/stable/index.html)

- [Singvis](https://www.cnblogs.com/singvis/p/11967984.html)

- [itlance_ouyang ](https://www.jb51.net/article/134134.htm)

### 简介

ssh是一个协议，OpenSSH是其中一个开源实现，paramiko是Python的一个库，实现了SSHv2协议(底层使用cryptography)。

由于paramiko属于第三方库，所以需要使用如下命令先行安装

```python
pip3 install paramiko

```

### 简单连接使用

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

### 简单sftp连接

```python
import paramiko

# 获取SSHClient实例
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接SSH服务端
client.connect("192.168.119.5", username="root", password="zzjqwe123",compress=True)
# 获取Transport实例
tran = client.get_transport()
# 获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)

remotepath = '/root/test_access.log'
localpath = r'C:\Users\Administrator\Desktop\log\test\test1_access.log'

sftp.get(remotepath, localpath)
client.close()
```

### 作为一个类

* 具体请看[github](https://github.com/zzj0403/markdowm-summary/blob/master/log/lib/paramiko_client.py)

* settings对象看conf文件

### 犯过的错误

```python 
# 报错：'str' object has no attribute 'get_fingerprint'
self.private_key = paramiko.DSSKey.from_private_key_file(settings.KEY)
self.client.connect(hostname=hostname,
                    port=settings.PORT,
                    username=settings.USERNAME,
                    # pkey=settings.KEY, KEY -> str pkey用的是一个对象不是一个字符串
                    pkey=self.private_key,
                    compress=True) 
```

## pymysql

### 简单使用

```PYTHON
import pymysql
conn = pymysql.connect(
    host='47.97.44.176',
    user='zzj',
    port=13006,
    password='4dAnFoLdh7mB39yCp76E',
    database='test',
    charset='utf8'
)

cursor = conn.cursor()
sql = "SELECT * FROM tmp_auto_user_book"
res = cursor.execute(sql)
print(res)
cursor.close()
conn.close()
```

