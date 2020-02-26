"""
前提
    一切皆对象
元类
    产生类的类
"""
class MyClass:
    pass
# obj = MyClass()
# print(type(obj))
# print(type(MyClass))  # 我们自己写的类 其实内部是由type帮我们创建的
"""
自己写的类产生的对象 = 我们自己写的类(...)
对象(我们自己写的类) = type(...)

type是专门用来生成类的 我们管产生类的类 叫做元类
所以type就是所有类默认的元类


类比较关键的部分
    1.类名
    2.类的父类
    3.类体代码运行之后产生的名称空间
"""
# 不借助于class关键字  来定义一个类


# exec补充


# res1 = """
# x = 1
# y = 2
# z = 3
# """
# g = {}
# l = {}
# exec(res1,g,l)  # 不指定的情况下 字符串里面的代码运行之后产生的名字都会放到局部名称空间中
# print(l)
class_name = 'Teacher'
class_bases = (object,)
class_body = """
school = 'oldboy'

def index(self):
    print('index方法')
def login(self):
    print('login方法')
"""
# class_namespace = {}
# exec(class_body,{},class_namespace)
#
#
# xxx = type(class_name,class_bases,class_namespace)
# # print(xxx.school)
# # xxx.index(1)
# obj = xxx()
# print(obj)
# print(obj.school)
# obj.index()
# obj.login()



# class Mymeta(type):  # 必须是继承了type的类才是自定义元类
#     def __call__(self, *args, **kwargs):
#         # print(self)
#         # print(args)
#         # print(kwargs)
#         # 类加括号走的是__call__方法 那么 该方法返回什么 得到的对象就是什么
#         # return 123
#         """
#         产生一个对象需要做哪些事儿？
#             1.产生一个空对象
#             2.调用__init__实例化对象
#             3.将对象返回
#         """
#         # 1.产生一个空对象
#         obj = self.__new__(self,*args,**kwargs)  # __new__是专门用来帮你创建一个空对象用的
#         # 2.调用__init__实例化对象
#         self.__init__(obj,*args,**kwargs)
#         # 3.将对象返回
#         return obj
#
#
#
# class oldboyTeacher(metaclass=Mymeta):  # 通过metaclass可以指定类的元类
#     school = 'oldboy'
#     def __init__(self,name):
#         self.name = name
#
#     def run(self):
#         print('%s is running'%self.name)
# obj = oldboyTeacher('jason')
# print(obj,type(obj))

"""
obj = Teacher()  类加括号走的就是元类里面的__call__方法 
Teacher = type()


1.对象加括号执行的是父类中的__call__方法
2.一切皆对象 类也是对象(type加括号产生的对象)

"""


# class Mymeta(type):
#     # def __new__(cls, *args, **kwargs):
#     #     print(cls)
#     #     print(args)
#     #     print(kwargs)
#
#     def __new__(cls, class_name,class_bases,class_body):
#         print(class_name)
#         print(class_bases)
#         print(class_body)
#         # 这里需要记住的是，必须在最后调用元类type中的__new__方法来产生该空对象
#         return type.__new__(cls, class_name, class_bases, class_body)
# class OldboyTeacher(object,metaclass=Mymeta):
#     school = 'oldboy'
#
#     def __init__(self, name):
#         self.name = name
#
#     def run(self):
#         print('%s is running' % self.name)
#
# obj = OldboyTeacher('jason')

# 元类能够做的事情
"""
你通过元类 可以拦截类的创建过程 控制类的创建

用到的就是__new__方法
"""

# 模板
class Mymeta(type):
    def __new__(cls, class_name, class_bases, class_dic):
        print(class_name)
        print(class_bases)
        print(class_dic)
        class_dic['xxx'] = '123'
        if 'school' in class_dic:
            class_dic['school'] = 'DSB'
        return type.__new__(cls, class_name, class_bases, class_dic)

class OldboyTeacher(metaclass=Mymeta):
    school = 'oldboy'

    def __init__(self, name):
        self.name = name

    def run(self):
        print('%s is running' % self.name)

print(OldboyTeacher.xxx)  # 发现可以打印出来    123
print(OldboyTeacher.school)  # DSB