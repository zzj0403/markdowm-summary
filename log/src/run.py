from lib.paramiko_client import ParamikoClient
from lib.conf.settings import settings
from lib.log_analysis import log_list_func
from db.mysql_control import *

import time
import datetime


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


def run():
    sftp_client = ParamikoClient()
    for host, hosts in settings.HOST.items():
        # print(host)
        for key, values in hosts.items():
            v_sftp = sftp_client.get_sftp_client(values)
            v_sftp.get('/home/zzj/access.yti.soudlink.net.log', settings.TMP_LOG + key + '_access.log')
            print('======')
            # 打印日志 ，并写入数据库。
            with open(settings.TMP_LOG + key + '_access.log', 'r', encoding='utf8') as f:
                lines = f.readlines()
                ls = []
                for line in lines:
                    # 分析下载过来的日志
                    res = log_list_func(line)
                    res['project'] = host + "_" + key
                    ls.append(res)
                # 写入数据库。
                # print(ls)
                session.execute(log.__table__.insert(), ls)
                session.commit()

            # with open(settings.TMP_LOG + key + '_access.log', 'r', encoding='utf8') as f:
            #     lines = f.readlines()
            #     ls = []
            #     for line in lines:
            #         # 分析下载过来的日志
            #         res, flag = log_list_func(line)
            #         print(res,flag)
            #         if not res:
            #             continue
            #         res['project'] = host + "_" + key
            #         # print(res)
            #         ls.append(res)
            #     # 写入数据库。
            #         break
            #     session.execute(log.__table__.insert(), ls)
            #     session.commit()
