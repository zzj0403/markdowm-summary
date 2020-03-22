import re
import time
from lib.conf.settings import settings


# res = json.loads(test_json)
# print(res)
# file = '117.132.195.100 - - [20/Mar/2020:00:29:02 +0800] "POST /api/ssvoice/IOSCheck/get/newUserInfo/ios/list/jform HTTP/1.1" 200 "28" "loginKey=0fdb57975a6652e6&offset=195&count=15" "-" "NEngine/1.0 (compatible; MSIE 6.0; Windows NT 5.1)" "-" "0.055" "0.010"'
# file = '119.41.152.59 - - [18/Mar/2020:00:07:45 +0800] "POST /api/ssvoice/cp/get/speed/matching/station/audio/list/jform HTTP/1.1" 200 "28" "offset=0&count=1&ssId=100297547" "-" "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; CMCC M761 Build/OPM1.171019.026) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30" "-" "0.004" "0.003"'

# print(matches.groups())


def format_log(line):
    #log_fmt = r'(?P<ip>\d+.*) - - \[(?P<day>\d+)/(?P<month>\w+)/(?P<year>\d+):(?P<time>\S+)\s\S+\s\"(?P<method>\S+) (?P<request>\S+) \S+ (?P<stat_code>\w+) \"(?P<boy_size>\w+)\" \"(?P<request_body>\S+)\" \S+ \"(?P<user_agent>[^\"]+)\" \S+ \"(?P<request_time>\d.\d+)\" \S+'
    log_fmt = r'(?P<ip>\d+.*)\s-\s-\s\[(?P<day>\d+)/(?P<month>\w+)/(?P<year>\d+):(?P<time>\S+)\s\S+\s\"(?P<method>\S+)\s(?P<request>\S+)\s\S+\s(?P<stat_code>\w+)\s\"(?P<boy_size>\w+)\"\s\"(?P<request_body>[^\"]*)\"\s\S+\s\"(?P<user_agent>[^\"]+)\"\s\S+\s\"(?P<request_time>\d.\d+)\"\s\S+'
    regex = re.compile(log_fmt, )
    matches = regex.match(line)
    if not matches:
        with open(settings.REQUEST_ERROR_FILE, 'a', encoding='utf8')as f:
            f.write(line)
        return None
    else:
        return matches

    # print(line)


def parse_time(day, month, year, log_time):
    """转化为long型时间"""
    time_str = '%s%s%s %s' % (year, month, day, log_time)
    res = time.mktime(time.strptime(time_str, '%Y%b%d %H:%M:%S'))
    time_local = time.localtime(res)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    # print(dt)
    return dt


def analysis_agent(useragent):
    if useragent.find('Android'):
        agent = 'Android'
        return agent
    elif useragent.find('Windows'):
        agent = 'Windows'
        return agent
    elif useragent.find('iOS'):
        agent = 'iOS'
        return agent
    else:
        return 'other'


def log_list_func(line):
    matches = format_log(line)
    if matches:
        date = matches.group("day")
        month = matches.group("month")
        year = matches.group("year")
        day_time = matches.group("time")
        time = parse_time(date, month, year, day_time)
        ip = matches.group('ip')
        method = matches.group('method')
        request = matches.group('request')
        stat_code = matches.group('stat_code')
        boy_size = matches.group('boy_size')
        request_body = matches.group('request_body')
        # user_agent = matches.group('user_agent')
        user_agent = analysis_agent(matches.group('user_agent'))
        request_time = matches.group('request_time')
        log_list = [time, ip, method, request, stat_code, boy_size, request_body, user_agent, request_time]
        return log_list


# # #
# if __name__ == '__main__':
#     res = log_list_func()
#     print(res)
with open(r'C:\Users\Administrator\Desktop\markdowm-summary\log\test\test_access.log', 'r', encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        res = log_list_func(line)
        print(res)
