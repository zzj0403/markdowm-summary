import json

#
# with open(r'D:\code\log\test\47.97.44.176game.host.access.log','r',encoding='utf-8')as f:
#     for lien in f:
#         log_dic= json.loads(lien)
#         print(type(log_dic),log_dic)

# test_json = '{"timestamp":"20/Mar/2020:00:25:43 +0800","remote_addr":"185.202.1.45","uri":"-","body_bytes_sent":173,"bytes_sent":173,"request":"\x03\x00\x00/*\xE0\x00\x00\x00\x00\x00Cookie: mstshash=Administr","request_time":0.245,"status":"400","http_referer":"-","http_x_forwarded_for":"-","http_user_agent":"-"}'
import re
import time

# res = json.loads(test_json)
# print(res)
str_log = '117.132.195.100 - - [20/Mar/2020:00:29:02 +0800] "POST /api/ssvoice/IOSCheck/get/newUserInfo/ios/list/jform HTTP/1.1" 200 "28" "loginKey=0fdb57975a6652e6&offset=195&count=15" "-" "NEngine/1.0 (compatible; MSIE 6.0; Windows NT 5.1)" "-" "0.055" "0.010"'

log_fmt = r'(?P<ip>\d+.*) - - \[(?P<day>\d+)/(?P<month>\w+)/(?P<year>\d+):(?P<time>\S+)\s\S+\s\"(?P<method>\S+) (?P<request>\S+) \S+ (?P<stat_code>\w+) \"(?P<boy_size>\w+)\" \"(?P<request_body>\S+)\" \S+ \"(?P<user_agent>[^\"]+)\" \S+ \"(?P<request_time>\d.\d+)\" \S+'
regex = re.compile(log_fmt, )
matches = regex.match(str_log)


# print(matches.group())

def parse_time(day, month, year, log_time):
    """转化为long型时间"""
    time_str = '%s%s%s %s' % (year, month, day, log_time)
    return time.mktime(time.strptime(time_str, '%Y%b%d %H:%M:%S'))

if __name__ == '__main__':
    date = matches.group("day")
    month = matches.group("month")
    year = matches.group("year")
    day_time = matches.group("time")
    ctime = parse_time(date, month, year, day_time)
    print(ctime)
