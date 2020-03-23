from lib.paramiko_client import ParamikoClient
from lib.conf.settings import settings
from lib.log_analysis import log_list_func
from db.pymysql_test import mysql
import time
import datetime


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


def run():
    sftp_client = ParamikoClient()
    for k, v in settings.HOST.items():
        print(k)
        for key, values in v.items():
            v_sftp = sftp_client.get_sftp_client(values)
            v_sftp.get('/home/zzj/access.i.moguupd5.com.log', settings.TMP_LOG + key + '_access.log')
            print('======')
            # 打印日志            # 分析下载过来的日志，并写入数据库。
            with open(settings.TMP_LOG + key + '_access.log', 'r', encoding='utf8') as f:
                lines = f.readlines()
                for line in lines:
                    res = log_list_func(line)
                    table_name = k + str(getYesterday())
                    mysql.create(table_name)
                    mysql.inset(res)
            mysql.close()
