'''
# 反射
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


