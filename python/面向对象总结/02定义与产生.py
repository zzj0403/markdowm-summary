class Student:
    # 学校
    school = '清华大学'  # 数据(属性)
    name = '类中的name'
    # 让对象在产生的时候 有自己的属性
    def __init__(self,name,age,gender):  # 形参中放 你想让对象有的而独立的属性 name,age,gender
        self.name = name  # self指代的就是每一次类实例化(加括号调用)产生的对象
        self.age = age  # 该句式 类似于往对象的空字典中 新增键值对
        self.gender = gender

    # 选课
    def choose_course(self):  # self就是一个普普通通的形参名而已   功能
        print(self)  # 对象来调  指代的就是对象本身
        print(self.name)
        print('学生选课功能')

obj = Student('jason',18,'male')  # 其实类名加括号会执行类中__init__方法

"""
对象(类)获取名称空间中的属性和方法的统一句式   句点符(.)
__dict__ 查看对象所有的属性
"""
# print(obj.__dict__)
# print(obj.school)
# obj.choose_course()