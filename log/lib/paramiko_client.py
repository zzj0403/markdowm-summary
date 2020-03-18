import paramiko
# import configparser
from lib.conf.settings import settings


class ParamikoClient:
    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.private_key = paramiko.DSSKey.from_private_key_file(settings.KEY)
        self.sftp_client = None
        self.client_state = 0

    def connect(self, hostname):
        try:
            self.client.connect(hostname=hostname,
                                port=settings.PORT,
                                username=settings.USERNAME,
                                pkey=self.private_key,
                                compress=True)
            self.client_state = 1
        except Exception as e:
            print(e)
            try:
                self.client.close()
            except:
                pass

    def run_cmd(self, com_str):
        stdin, stdout, stderr = self.client.exec_command(com_str)
        data = stdout.readlines()
        return data

    def get_sftp_client(self, hostname):
        if self.client_state == 0:
            self.connect(hostname=hostname)
        if not self.sftp_client:
            self.sftp_client = paramiko.SFTPClient.from_transport(self.client.get_transport())
        return self.sftp_client


# #
# client = ParamikoClient()
# #
# client.connect('47.97.44.176')
# # print(client.run_cmd('df -h'))
