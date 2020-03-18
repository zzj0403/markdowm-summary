from conf import config
from lib.conf import global_settings


class mySettings():

    def __init__(self):

        ### 集成默认配置
        for k in dir(global_settings):
            if k.isupper():
                v = getattr(global_settings, k)
                setattr(self, k, v)  #### setattr(self, USER, 'qwe')

        ### 集成用户自定义配置
        for k in dir(config):
            if k.isupper():
                v = getattr(config, k)
                setattr(self, k, v)  ### setattr(self, USER, 'root')


settings = mySettings()
# print(settings.__dict__)
# print(settings.HOST)

