from lib.paramiko_client import ParamikoClient
from lib.conf.settings import settings

if __name__ == '__main__':
    sftp_client = ParamikoClient()
    for k, v in settings.HOST.items():
        print(k)
        for key, values in v.items():
            v_sftp = sftp_client.get_sftp_client(values)
            v_sftp.get('/home/zzj/access.i.moguupd5.com.log', '../test/' + key + '_access.log')
            print('======')
            # 打印日志
            # 分析下载过来的日志，并写入数据库。

