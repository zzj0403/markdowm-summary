"""
异常处理的语法结构
try:
	...可能出现错误的代码
except 错误的类型:
	...一旦发生错误 补救措施
当你没办法确定某一块代码是否会出现异常 那么你就用try一下

异常类型
    NameError
    KeyError
    IndexError
"""
# 例子
try:
    # age
    l = [1, 2, 3]
    # l[100]
    d = {'x': 1}
    # d['y']
except KeyError as e:
    print(e)
except NameError as e:
    print(e)
except IndexError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print('当try内部的代码没有任何错误的时候执行')


# 如何自己抛出异常
# 关键字raise
class People:
    def __init__(self, name):
        if not isinstance(name, str):  # 判断数据是否是字符串类型
            raise IndexError('%s must be str type' % name)  # 主动抛出异常
        self.name = name


obj = People('jason')
# obj = People(123)

# 断言 assert     提前断定即将发生的事情 如果跟你预想的不一样 直接报错
l = [1, 2, 3]


# assert len(l) == 2


# 自定义异常类型
class MyError(BaseException):
    def __init__(self, msg):
        super().__init__()  # 先调用父类的方法
        self.msg = msg  # 再调用自己的方法

    def __str__(self):
        return '<%s>' % self.msg


# obj = MyError('我自己的异常')
# print(obj)
raise MyError('我自己定义的异常')  # 主动抛出异常其实就是将异常类的对象打印出来,会走__str__方法
