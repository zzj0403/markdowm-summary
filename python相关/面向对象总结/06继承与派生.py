'''
什么是继承
     继是新建类的方式,称为子类
     子类继承父类的属性
为什么要用继承
    继承好处能否减少代码

如何用？
    在python中支持一个类继承多个父类
'''


# 例题1
class People:  # （父类）
    school = 'oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


# 继承父类 People
class Shudent(People):
    def choose_course(self):
        print('%s is choosing course' % self.name)


# 继承父类 People
class Teacher(People):
    def __init__(self, name, age, sex, level):
        # 派生（子类中新定义的属性）
        # super(Teacher, self).__init__(name, age, sex) #老写法
        super().__init__(name, age, sex) #（当前位置Teacher的父类去找）
        self.level = level

    def score(self, stu_ibj, num):
        stu_ibj.score = num
        # print('%s is score' % self.name)


zzj = Teacher('zzj', 18, 'male', '10')
cc = Shudent('cc', 12, 'female')

# super（）会基于当前所在的查找位置继续往后查找
# print(Teacher.mro()) # [<class '__main__.Teacher'>, <class '__main__.People'>, <class 'object'>]
