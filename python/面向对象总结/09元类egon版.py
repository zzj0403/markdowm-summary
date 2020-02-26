
'''
1、什么是元类
    在python中一切皆对象，那么我们用class关键字定义的类本身也是一个对象
    负责产生该对象的类称之为元类，即元类可以简称为类的类

    class Foo: # Foo=元类()
        pass
2、为何要用元类
    元类是负责产生类的，所以我们学习元类或者自定义元类的目的
    是为了控制类的产生过程，还可以控制对象的产生过程

3、如何用元类

'''
#1、储备知识：内置函数exec的用法
# cmd="""
# x=1
# def func(self):
#     pass
# """
# class_dic={}
# exec(cmd,{},class_dic)
#
# print(class_dic)

#2、创建类的方法有两种
# 大前提：如果说类也是对象的化，那么用class关键字的去创建类的过程也是一个实例化的过程
# 该实例化的目的是为了得到一个类，调用的是元类
#2.1 方式一：用的默认的元类type
# class People: #People=type(...)
#     country='China'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def eat(self):
#         print('%s is eating' %self.name)

# print(type(People))

#2.1.1 创建类的3个要素：类名，基类，类的名称空间
class_name='People'
class_bases=(object,)
class_dic={}
class_body="""
country='China'
def __init__(self,name,age):
    self.name=name
    self.age=age

def eat(self):
    print('%s is eating' %self.name)
"""
exec(class_body,{},class_dic)

# 准备好创建类的三要素
# print(class_name)
# print(class_bases)
# print(class_dic)

# People=type(类名，基类，类的名称空间)
# People1=type(class_name,class_bases,class_dic)
# print(People1)
# obj1=People1('egon',18)
# print(People)
# obj=People('egon',18)
#
# obj1.eat()
# obj.eat()

'''
#2.2 方式二：用的自定义的元类
class Mymeta(type): #只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
    def __init__(self,class_name,class_bases,class_dic):
        print(self) #现在是People
        print(class_name)
        print(class_bases)
        print(class_dic)
        super(Mymeta,self).__init__(class_name,class_bases,class_dic) #重用父类的功能

# 分析用class自定义类的运行原理（而非元类的的运行原理）：
#1、拿到一个字符串格式的类名class_name='People'
#2、拿到一个类的基类们class_bases=(obejct,)
#3、执行类体代码，拿到一个类的名称空间class_dic={...}
#4、调用People=type(class_name,class_bases,class_dic)
class People(object,metaclass=Mymeta): #People=Mymeta(类名,基类们,类的名称空间)
    country='China'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print('%s is eating' %self.name)


# 应用：自定义元类控制类的产生过程，类的产生过程其实就是元类的调用过程

class Mymeta(type): #只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
    def __init__(self,class_name,class_bases,class_dic):
        if class_dic.get('__doc__') is None or len(class_dic.get('__doc__').strip()) == 0:
            raise TypeError('类中必须有文档注释，并且文档注释不能为空')
        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')
        super(Mymeta,self).__init__(class_name,class_bases,class_dic) #重用父类的功能

class People(object,metaclass=Mymeta): #People=Mymeta('People',(object,),{....})
    """这是People类"""
    country='China'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print('%s is eating' %self.name)
'''


#3 储备知识：__call__
# class Foo:
#     def __call__(self, *args, **kwargs):
#         print(self)
#         print(args)
#         print(kwargs)
#
#
# obj=Foo()
#
# # 要想让obj这个对象变成一个可调用的对象，需要在该对象的类中定义一个方法__call__方法
# # 该方法会在调用对象时自动触发
# obj(1,2,3,x=1,y=2)


# 4、自定义元类来控制类的调用的过程，即类的实例化过程
class Mymeta(type):

    def __call__(self, *args, **kwargs):
        # print(self) # self是People
        # print(args)
        # print(kwargs)
        # return 123

        # 1、先造出一个People的空对象
        obj=self.__new__(self)
        # 2、为该对空对象初始化独有的属性
        # print(args,kwargs)
        self.__init__(obj,*args,**kwargs)

        # 3、返回一个初始好的对象
        return obj


class People(object,metaclass=Mymeta):
    country='China'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print('%s is eating' %self.name)

    def __new__(cls, *args, **kwargs):
        print(cls)
        # cls.__new__(cls) # 错误
        obj=super(People,cls).__new__(cls)
        return obj

# 分析：调用Pepole的目的
#1、先造出一个People的空对象
#2、为该对空对象初始化独有的属性
# obj1=People('egon1',age=18)
# obj2=People('egon2',age=18)
# print(obj1)
# print(obj2)

obj=People('egon',age=18)
print(obj.__dict__)
print(obj.name)
obj.eat()