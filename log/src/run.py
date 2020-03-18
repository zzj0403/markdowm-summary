from lib.paramiko_client import ParamikoClient
from lib.conf.settings import settings

if __name__ == '__main__':
    sftp_client = ParamikoClient()
    for k, v in settings.HOST.items():
        print(k)
        for values in v:
            v_sftp = sftp_client.get_sftp_client(values)
            v_sftp.get('/tmp/config','../test/' + values + '_congfig')
            print('======')



