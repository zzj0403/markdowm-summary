'''
1、什么是单例模式
    单例模式：基于某种方法实例化多次得到实例是同一个
2、为何用单例模式
    当实例化多次得到的对象中存放的属性都一样的情况，应该将多个对象指向同一个内存，即同一个实例
3、如何用
'''

# 单例模式实现方式一：
# import settings
#
# class Mysql:
#     __instacne=None
#
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port
#
#     @classmethod
#     def from_conf(cls):
#         if cls.__instacne is None:
#             cls.__instacne=cls(settings.IP,settings.PORT)
#         return cls.__instacne
# # obj=Mysql('1.1.1.10',3306)
#
# obj1=Mysql.from_conf()
# obj2=Mysql.from_conf()
# obj3=Mysql.from_conf()
#
# print(obj1)
# print(obj2)
# print(obj3)
#
# obj4=Mysql('10.10.10.11',3307)


# 单例模式实现方式二(装饰器实现)：
# import settings
# def singleton(cls):
#     cls.__instance=cls(settings.IP,settings.PORT)
#     def wrapper(*args,**kwargs):
#         if len(args) == 0 and len(kwargs) == 0:
#             return cls.__instance
#         return cls(*args,**kwargs)
#     return wrapper
#
# @singleton #Mysql=singleton(Mysql) #Mysql=wrapper
# class Mysql:
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port
#
#
# obj1=Mysql() #wrapper()
# obj2=Mysql() #wrapper()
# obj3=Mysql() #wrapper()
# print(obj1 is obj2 is obj3)
# print(obj1)
# print(obj2)
# print(obj3)
# obj4=Mysql('1.1.1.4',3308)
# print(obj4)


# 单例模式实现方式三：
import settings


class Mymeta(type):
    def __init__(self, class_name, class_bases, class_dic):  # self=Mysql
        super(Mymeta, self).__init__(class_name, class_bases, class_dic)
        self.__instance = self.__new__(self)  # 造出一个Mysql的对象
        self.__init__(self.__instance, settings.ip, settings.port)  # 从配置文件中加载配置完成Mysql对象的初始化

        # print(self.__instance)
        # print(self.__instance.__dict__)

    def __call__(self, *args, **kwargs):  # self=Mysql
        if len(args) == 0 and len(kwargs) == 0:
            return self.__instance

        obj = self.__new__(self)
        self.__init__(obj, *args, **kwargs)
        return obj


class Mysql(object, metaclass=Mymeta):  # Mysql=Mymeta(...)
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port


obj1 = Mysql()
obj2 = Mysql('10.10.10.11', 3308)

print(obj1.__dict__)
print(obj2.__dict__)
