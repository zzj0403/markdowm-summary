'''
 # 给对象设置属性
def __init__(self,name):
    self.name = name

#会在对象执行打印操作的时候 自动触发
def __str__(self):
    print('我被执行了')
    return 'xxx'

#当你给对象设置属性的时候 自动触发
def __setattr__(self, key, value):
    print(key,value)  # key属性名  value属性值

#当对象在获取一个不存在的属性或者方法的时候 自动触发
def __getattr__(self, item):
    print(item)  # item指代的就是用户想要获取的不存在的属性名

# 产生类触发
def __call__(self, *args, **kwargs):
    print(args,kwargs)

#只允许对 MyClass实例添加name属性。
class MyClass(object):
    __slots__ = ['name']

__del__析构方法
# __del__会在对象被删除之前自动触发
'''


# 例子
class MyClass(object):
    def __init__(self, name):
        self.name = name  # 给对象设置属性

    # def __str__(self): # 必须得有一个返回值
    #     print('我被执行了')
    #     return 'xxx'

    # def __setattr__(self, key, value):  # name jason
    #     print(key,value)  # key属性名  value属性值

    # def __getattr__(self, item):
    #     print(item)  # item指代的就是用户想要获取的不存在的属性名

    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        print('我是call方法')
        return 1111


#
# obj = MyClass('jason')
# obj.age
# print(obj())


# 例题2 运用例子
# 如何  d.yyy = 222 来给对象添加属性和取值

class MyDict(dict):

    def __getattr__(self, item):
        return self.get(item)

    def __setattr__(self, key, value):
        self[key] = value


d = MyDict({'name': 'jason', 'password': '123'})
d.age = 18
d.hoboy = 'run'


# print(d.name)
# print(d)


class MyDict(dict):
    __slots__ = ('age')


d1 = MyDict({'name': 'jason', 'password': '123'})
d1.age = 18


# d1.name = 'zzj' # 'MyDict' object has no attribute 'name'


# 例题3 运用例子
class Date:
    def __init__(self, year, mon, day):
        self.year = year
        self.mon = mon
        self.day = day

    def __del__(self):
        print('我执行啦')


d1 = Date(2016, 12, 3)

del d1.year
print('----------->')