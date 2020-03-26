import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PORT = 32101
USERNAME = '1cloud'
KEY = os.path.join(BASE_DIR, 'ssh', 'id_zzj')
TMP_LOG = os.path.join(BASE_DIR, 'files')
REQUEST_ERROR_FILE = os.path.join(BASE_DIR, 'files', 'error_log_request.txt')
LOG_PATH = '/var/log/nginx/'
DOMAIN_NAME = {
    # 'ss': [
    #     'i.moguupd5.com',
    #     'jvi.mimtu.cn',
    #     'yti.soudlink.net'
    # ],
    'beiyu': [
        'i.tingjiankj.cn',
        'i.ybvoice.com'
    ],
    'ke': [
        ''
    ]
}

HOST = {
    # 'zzj': {'test': '47.99.63.207'},
    'ss': {
        'api1': '47.99.63.207',
        'api2': '47.99.129.161',
        'api3': '47.97.73.36',
    },
    'beiyu': {
        'api1': '47.99.164.167',
        'api2': '121.40.230.24',
        'api3': '114.55.174.211',

    }
}
