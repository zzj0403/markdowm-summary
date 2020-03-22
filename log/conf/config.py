import os

PORT = 9603
USERNAME = 'zzj'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
KEY = os.path.join(BASE_DIR, 'files', 'zzj')

REQUEST_ERROR_FILE = os.path.join(BASE_DIR, 'files', 'error_log_request.txt')
HOST = {
    'zzj': {'test': '47.97.44.176', }
}
# local_path = '/home/zzj/logs'
