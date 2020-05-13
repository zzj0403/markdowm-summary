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

* `paramiko`的再次封装

```python
import paramiko


class SSHProxy(object):
    def __init__(self, hostname):
        self.hostname = hostname
        self.port = 22
        self.username = "zzj"
        self.private_key = paramiko.RSAKey.from_private_key_file('zzj01')
        self.transport = None

    def open(self):  # 给对象赋值一个上传下载文件对象连接
        self.transport = paramiko.Transport((self.hostname, self.port))
        self.transport.connect(username=self.username, pkey=self.private_key, )

    def command(self, cmd):  # 正常执行命令的连接  至此对象内容就既有执行命令的连接又有上传下载链接
        ssh = paramiko.SSHClient()
        ssh._transport = self.transport

        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        return result

    def upload(self, local_path, remote_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.put(local_path, remote_path)
        sftp.close()
        
    def download(self, remote_path, local_path, ):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.get(remote_path, local_path )
        sftp.close()
        
    def close(self):
        self.transport.close()

    def __enter__(self):
        """with语法一旦触发立刻执行"""
        self.open()
        return self  # 该方法返回什么 as语法后面就接受到什么

    def __exit__(self, exc_type, exc_val, exc_tb):
        """with代码块执行完毕之后自动触发"""
        self.close()

```

* `SSHProxy`使用

  ```python 
  
  with SSHProxy("10.0.0.1")  as obj:
      res = obj.command('df -h')
      print(res)
  with SSHProxy("10.0.0.1")  as obj:
      obj.upload('run.py', '/tmp/test')
  
  
  
  ```

  

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

```python
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

