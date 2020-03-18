import paramiko
import configparser

from lib.conf.settings import settings


class ParamikoClient:
    def __init__(self, ):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.private_key = paramiko.DSSKey.from_private_key_file(self.config.get('ssh', 'key'))

    def connect(self, hostname):
        try:
            self.client.connect(hostname=hostname,
                                port=self.config.get('ssh', 'port'),
                                username=self.config.get('ssh', 'username'),
                                pkey=self.private_key)
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


client = ParamikoClient()
client.connect('47.97.44.176')
# res = client.run_cmd('df -h')
