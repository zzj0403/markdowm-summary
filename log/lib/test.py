# from datetime import datetime
# import re
#
# logline = '183.60.212.153 - - [18/Mar/2020:10:23:29 +0800] "GET /api/ssvoice/recommend/get/recommend/room/133V/jform HTTP/1.1" 200 16691 "-" "Mozilla/5.0 (Linux; U; Android 9; zh-cn; MIX 3 Build/PKQ1.180729.001) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1"'''
# log = '218.108.128.187 - - [18/Mar/2020:00:12:06 +0800] "POST /api/ssvoice/recommend/get/recommend/room/133V/jform HTTP/1.1" 200 "17618" "offset=0&loginKey=3be877c662f4d927&roomTagId=1213&count=100" "-" "Mozilla/5.0 (Linux; U; Android 9; zh-cn; MIX 3 Build/PKQ1.180729.001) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1" "-" "0.114" "0.083"'
#
#
#
#
#
# def extract(line):
#     pattern = '(?P<remote_addr>[\d\.]{7,}) - - (?:\[(?P<datetime>[^\[\]]+)\]) "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+) "[^"]+" "(?P<user_agent>[^"]+)"'
#     regex = re.compile(pattern)
#     matcher = regex.match(line)
#     if matcher:
#         return {k: ops.get(k, lambda x: x)(v) for k, v in matcher.groupdict().items()}
#     else:
#         raise Exception('No match')
#
#
# ops = {
#     'datetime': lambda timestr: datetime.strptime(timestr, "%d/%b/%Y:%H:%M:%S %z"),
#     'request': lambda request: dict(zip(('method', 'url', 'protocol'), request.split())),
#     'status': int,
#     'size': int
# }
#
# if __name__ == '__main__':
#     log_pro = extract(logline)
#     print(log_pro)
#     for k, v in log_pro.items():
#         print(k, v)


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
