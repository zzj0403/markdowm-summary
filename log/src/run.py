from lib.paramiko_client import ParamikoClient
from lib.conf.settings import settings
from lib.log_analysis import log_list_func
from db.mysql_control import *
import os

import datetime


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    yesterday = str(yesterday).replace('-', '')
    return yesterday


def down_log_and_save(host, ip, project_name, domain, ):
    '''下载列表中日志并分析储存到数据库'''
    sftp_client = ParamikoClient()
    v_sftp = sftp_client.get_sftp_client(ip)
    local_path = settings.TMP_LOG + '/' + project_name + '_' + host + '_' + domain + '_access.log'
    remote_path = settings.LOG_PATH + domain + "/" + 'access.' + domain + '.log'
    v_sftp.get(remote_path, local_path)
    with open(local_path, 'r', encoding='utf8') as f:
        lines = f.readlines()
        ls = []
        for line in lines:
            # 分析下载过来的日志
            res = log_list_func(line)
            res['project'] = project_name + '_' + host
            res['domain'] = domain
            ls.append(res)
        # 写入数据库。
        session.execute(log.__table__.insert(), ls)
        session.commit()


def host_list():
    '''读取配置文件的主机和需要下载的域名日志，并返回列表'''
    host_list = []
    for project_name, host_group in settings.HOST.items():

        for host, ip in host_group.items():
            # print(project_name,host)

            for project, domain_group in settings.DOMAIN_NAME.items():
                if project == project_name:
                    for domain in domain_group:
                        host_msg = host, ip, project_name, domain
                        host_list.append(host_msg)

    return host_list


def run():
    msg_list = host_list()
    # print(msg_list)
    for single in msg_list:
        down_log_and_save(single[0], single[1], single[2], single[3])
