1. 创建群机器人，并记录webhook及加签密码

![image-20200401140450649](../img/ding_robot1.png)

2. 简单调用

   ```python
   import requests
   import json
   import time
   import hmac
   import hashlib
   import base64
   import urllib
   from urllib import parse
   # 时间搓
   timestamp = round(time.time() * 1000)
   webhook = "https://oapi.dingtalk.com/robot/send?************"
   secret = 'SEC******************************'
   # 两者拼接起来
   string_to_sign = '{}\n{}'.format(timestamp, secret)
   # 
   hmac_code = hmac.new(secret.encode(), string_to_sign.encode(), digestmod=hashlib.sha256).digest()
   
   sing = urllib.parse.quote_plus(base64.b64encode(hmac_code))
   webhook = '{}&timestamp={}&sign={}'.format(webhook, str(timestamp), sing)
   header = {
       "Content-Type": "application/json",
       "Charset": "UTF-8",
   }
   
   message = {
       "msg": "测试",
       "msgtype": "text",
       "text": {
           "content": "test"
       },
   }
   
   message_json = json.dumps(message)
   
   info = requests.post(url=webhook, data=message_json, headers=header)
   print(info)
   ```

   