# 删除图片并刷新CDN

## 七牛云代码

- 安装SDK 包

```shell
pip install qiniu
```

- 代码

```python
# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, put_file, etag, build_batch_delete, BucketManager, CdnManager

access_key = ''
secret_key = ''
q = Auth(access_key, secret_key)


def delete_list_file(bucket_name, delete_list):
    bucket = BucketManager(q)

    ops = build_batch_delete(bucket_name, delete_list)
    ret, info = bucket.batch(ops)
    print(info)


def cdn_manager(urls):
    cdn_manager = CdnManager(q)
    refresh_url_result = cdn_manager.refresh_urls(urls)
    print(refresh_url_result)


if __name__ == '__main__':
    urs = [
        'https://xxxx.com/pic/D9C44D798597E0256CF1111140D7BA42.png',
    ]

    file_name_list = []
    for i in urs:
        res = i.split('/', 3)[3]
        file_name_list.append(res)
    delete_list_file('o', file_name_list)
    cdn_manager(urs)

```



## 腾讯云代码

- 下载SDK包

```shell
pip install tencentcloud-sdk-python
pip install -U cos-python-sdk-v5
```



```python
# -*- coding: utf-8 -*-


from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import json
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

secret_id = ''  # 替换为用户的 secretId
secret_key = ''  # 替换为用户的 secretKey
region = 'ap-shanghai'  # 替换为用户的 Region
token = None  # 使用临时密钥需要传入 Token，默认为空，可不填
scheme = 'https'  # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
# 2. 获取客户端对象
client = CosS3Client(config)


def delete_file(Bucket, file_name_list):
    response = client.delete_objects(
        Bucket=Bucket,
        Delete={
            'Object': file_name_list,

            'Quiet': 'true'
        }
    )
    return response


def refresh_url(urls):
    from tencentcloud.common import credential
    from tencentcloud.common.profile.client_profile import ClientProfile
    from tencentcloud.common.profile.http_profile import HttpProfile
    from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
    from tencentcloud.cdn.v20180606 import cdn_client, models

    try:
        cred = credential.Credential(secret_id, secret_key)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cdn.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = cdn_client.CdnClient(cred, "ap-shanghai", clientProfile)

        req = models.PurgeUrlsCacheRequest()
        params = {'Urls': urls}
        json_str = json.dumps(params)
        req.from_json_string(json_str)

        resp = client.PurgeUrlsCache(req)
        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)


if __name__ == '__main__':
    urls = [
        'http://xxx.moguupd.com/test/test.jpg',
        'http://xxx.moguupd.com/test/test1.jpg',

    ]
    file_name_list = []
    for i in urls:
        dic = {'Key': ''}
        res = i.split('/', 3)[3]
        dic['Key'] = res
        file_name_list.append(dic)
    delete_file('xxx', file_name_list)
    refresh_url(urls)

```

