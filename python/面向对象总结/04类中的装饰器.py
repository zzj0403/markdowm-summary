''''
@property     将方法伪装成了函数,可以去掉括号运行
@classmethod  会将类当做第一个参数自动传入
@staticmethod 普通函数  谁来调 都需要手动传参

'''


#  例题1 @property 使用
class Person(object):

    @property
    def name(self):  # 将方法伪装成了函数
        name = '123'
        print(name)


obj = Person()
# obj.name


# @classmethod  和 staticmethod 使用
import settings, uuid


class Mysql:
    def __init__(self, ip, port):
        self.uid = self.__create_uid()
        self.ip = ip
        self.port = port

    def tall_info(self):
        print('%s:%s' % (self.ip, self.port))

    # 绑定给类的方法
    @classmethod
    def from_conf(cls):
        # print('绑定给类的方法 类来调 会将类当做第一个参数自动传入')
        '''
        obj2 = Mysql(settings.ip, settings.port)
        '''
        return cls(settings.ip, settings.port)

    # 非绑定方法
    @staticmethod
    def func(x, y):
        print('不与任何人绑定')
        return x, y

    @staticmethod
    def __create_uid():
        return uuid.uuid1()


obj1 = Mysql('10.0.0.1', 3306)
print(obj1.__dict__)
obj2 = Mysql.from_conf()
print(obj2.__dict__)

print(obj1.func(1, 2))
