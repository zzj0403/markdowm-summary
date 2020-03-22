from lib.paramiko_client import ParamikoClient
from lib.conf.settings import settings
from lib.log_analysis import log_list_func


def run():
    sftp_client = ParamikoClient()
    for k, v in settings.HOST.items():
        print(k)
        for key, values in v.items():
            v_sftp = sftp_client.get_sftp_client(values)
            v_sftp.get('/home/zzj/access.i.moguupd5.com.log', '../test/' + key + '_access.log')
            print('======')
            # 打印日志
            # 分析下载过来的日志，并写入数据库。
            res = log_list_func('../test/' + key + '_access.log')
            print(res)
