
import re
file = '185.153.199.118 - - [18/Mar/2020:01:37:27 +0800] "\x03\x00\x00/*\xE0\x00\x00\x00\x00\x00Cookie: mstshash=Administr" 400 "173" "-" "-" "-" "-" "0.280" "-"'
log_fmt = r'(?P<ip>\d+.*) - - \[(?P<day>\d+)/(?P<month>\w+)/(?P<year>\d+):(?P<time>\S+)\s\S+\s\"(?P<method>\S+) (?P<request>\S+) \S+ (?P<stat_code>\w+) \"(?P<boy_size>\w+)\" \"(?P<request_body>\S+)\" \S+ \"(?P<user_agent>[^\"]+)\" \S+ \"(?P<request_time>\d.\d+)\" \S+'
regex = re.compile(log_fmt, )
matches = regex.match(file)
print(matches)l