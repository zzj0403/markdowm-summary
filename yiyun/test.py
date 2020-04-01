import requests
import json
import time
import hmac
import hashlib
import base64
import urllib
from urllib import parse

timestamp = round(time.time() * 1000)
# print(timestamp)
webhook = "https://oapi.dingtalk.com/robot/send?access_token=f736470bbc4166064c501b9fa104a9d846c535694e730ea337ac12aa753f5c19"
secret = 'SEC541792c427f88583a94bb4deff0663ec7969a3cc0fe314e2a7754eb0eccd8858'
string_to_sign = '{}\n{}'.format(timestamp, secret)
# print(string_to_sign)
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
    # "at": {
    #
    #     "isAtAll": True
    # }

}
message_json = json.dumps(message)

# info = requests.post(url=webhook, data=message_json, headers=header)
# print(info)
def dingmessage():
    # 请求的URL，WebHook地址
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=f736470bbc4166064c501b9fa104a9d846c535694e730ea337ac12aa753f5c19"
    # 构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8",

    }
    # 构建请求数据
    tex = "test"
    secret = 'SEC541792c427f88583a94bb4deff0663ec7969a3cc0fe314e2a7754eb0eccd8858'
    message = {
        "msg": "测试",
        "msgtype": "text",
        "secret": secret,
        "text": {
            "content": tex
        },
        # "at": {
        #
        #     "isAtAll": True
        # }

    }
    # 对请求的数据进行json封装
    message_json = json.dumps(message)
    # 发送请求
    info = requests.post(url=webhook, data=message_json, headers=header)
    # 打印返回的结果
    print(info.text)


# if __name__ == "__main__":
# dingmessage()
import json
import requests

from dingtalkchatbot.chatbot import DingtalkChatbot

#
# webhook = "https://oapi.dingtalk.com/robot/send?access_token=f736470bbc4166064c501b9fa104a9d846c535694e730ea337ac12aa753f5c19"
# secret = 'SEC541792c427f88583a94bb4deff0663ec7969a3cc0fe314e2a7754eb0eccd8858'
# xiaoding = DingtalkChatbot(webhook, secret=secret)
#
# at_mobiles = [18512122996]
# xiaoding.send_text(msg='我就是小丁，小丁就是我！', at_mobiles=at_mobiles)
#