res = [{'time': '2020-03-18 15:17:25', 'ip': '94.102.49.190', 'correct_log': '1' ,'project': 'zzj_test'},{'time': '2020-03-18 00:00:04', 'ip': '223.149.104.215', 'method': 'POST', 'request': '/api/ssvoice/gift/get/treasure/box/list/jform', 'stat_code': '200', 'boy_size': '1387', 'request_body': '-', 'user_agent': 'Windows', 'request_time': '0.003', 'correct_log': '0' ,'project':'zzj'}]

from db.mysql_control import *


session.execute(log.__table__.insert(), res)
session.commit()