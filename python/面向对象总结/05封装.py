'''
什么是封装
    封：对外不是隐藏的，对内是开发的
    装：申请名称空间，装属性或名字

为什么封装
    自定义规则(例2)

如何使用
    对属性前面加  __xxx
'''


# 例子1：如何封装

class People:
    __x = 1000

    def __init__(self, name, height, weight):
        self.name = name
        self.__owner = height
        self.__width = weight

    def eat(self):
        print(self.__owner)
        return self.__width


a1 = People('zzj', 180, 60)
print(a1.name)
# print(a1.height) #访问不到
print(a1.eat())
# 查看类的所有字典
print(People.__dict__)  # {'__module__': '__main__', '_People__x': 1000, ....}
# 查看对象的所有字典
print(a1.__dict__)  # {'__module__': '__main__', '_People__x': 1000, ....}
print(a1._People__width)


# 例2 自定义规则

class People():
    def __init__(self, name, age, ):
        self.__name = name
        self.__age = age

    def tell_info(self):
        print('%s:%s' % (self.__name, self.__age))

    def set_info(self, new_name, nwe_age):
        if type(new_name) is not str:
            raise TypeError('名字必须用字符串类型')
        if type(nwe_age) is not int:
            raise TypeError('年龄必须是数字')
        self.__name = new_name
        self.__age = nwe_age


peo1 = People('zzj', 18)
peo1.set_info('cc', 13)
peo1.tell_info()

# 例子3：property 封装
# ps:将方法伪装成了函数 就是去掉（）依然可以运行
class People():
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) is not str:
            raise TypeError('名字必须是str类型')
        self.__name = name

    @name.deleter
    def name(self):
        raise PermissionError('不让删')


peo1 = People('zzj')
peo1.name = 'cc'
print(peo1.name)
del peo1.name



# 反射
'''
ps:
hasattr  判断是否有某个属性（属性和方法）
getattr  获取属性或者方法
setattr  设置属性或者方法
delattr  删除属性或者方法
'''


class MyLogin(object):
    school = 'oldboy'

    def get(self):
        print('get 方法')

    def post(self):
        print('post 方法')


obj = MyLogin()
# hasattr 方法
res1 = hasattr(obj, 'get')  # 等价于 'school' in MyLogin.__dict__

# getattr  方法
res = getattr(obj, 'school')  # MyLogin.__dict__['school'] 但没有会直接报错
# 所以一般线判断
# if hasattr(obj,'xxx'):
#     res = getattr(obj,'xxx')

#  setattr 给对象设置属性
obj.name = 'jason'  # 第一种设置
setattr(obj, 'age', 18)  # 第二种设置

# delattr给对象删除属性
delattr(obj, 'name')


