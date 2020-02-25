'''
1、什么是多台
    多态指的是同一种事物的多种形态
         >人
     动物>狗
         >猪
    三者属于动物，但事其特征有不一样

2、为什么要用多态
    使用者只需要知道一个函数换上不同的对象就能是使用不同的功能例如 len(str) len(list)

3、如何用


'''

# 第一种父类强制要求子类必须遵从父类标准
import abc


class Animal(metaclass=abc.ABCMeta):
    '''
        父类制定标准，不能被使用
        这种方式要求子类必须要有父类这些函数。
    '''

    @abc.abstractmethod
    def talk(self):
        pass

    @abc.abstractmethod
    def eat(self):
        pass


class People(Animal):
    def talk(self):
        print('say hello')

    def eat(self):
        pass


class Dog(Animal):
    def talk(self):
        print('汪汪汪')

    def eat(self):
        pass


def func(animal):
    animal.talk()


p1 = People()
d1 = Dog()
p1.talk()
# func(d1)


# 第二种python从业人员默认的写法

class Disk:
    def read(self):
        print('disk read')

    def write(self):
        print('disk write')


class Process:
    def read(self):
        print('process read')

    def write(self):
        print('processes write')


# obj1 = Disk()
# obj2 = Process()


# obj1.read()
# obj2.write()
