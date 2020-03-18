# file = r'C:\Users\Administrator\Desktop\log\test\test_access.log'
# with open(file, 'r', encoding='utf8')as f:
#     for line in f.readlines():
#         res = line.split(' ')
log = '114.230.37.115 - - [18/Mar/2020:21:18:43 +0800] "GET /api/ssvoice/chat/get/microphonelist4/31587/json HTTP/1.1" 200 "3175" "-" "-" "NEngine/1.0 (compatible; MSIE 6.0; Windows NT 5.1)" "-" "0.021" "0.022"'

res = log.split(' ')
print(res)
ip = res[0]
date = res[3].replace('[', '')
method = res[5].replace('"', '')
url = res[6]
status_code = res[8]
body_bytes = res[9].replace('"','')

print(ip, date,method,url,status_code,body_bytes)
