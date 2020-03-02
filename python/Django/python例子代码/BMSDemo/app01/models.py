from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
"""
图书管理系统  基本表设计

书籍表

出版社表

作者表

作者详情表


表关系确立
    书籍与出版社
        先站在书籍表    一对多不成立
            一本书能否由多个出版社(版权问题 不能有多个)
        再站在出版社表  一对多成立
            一个出版社能否出版多本书   
        结论:书籍与出版社是单向的一对多关系 所以最终他们的关系就是一对多 

    书籍与作者
        多对多 

    作者与作者详情
        一对一  


    orm创建表关系的时候 遵循以下规则
        一对多  
            外键字段建在多的那一方  

        多对多
            需要创建第三张表来维护关系
            多对多外键字段可以建在任意一方  但是推荐你建在查询频率较高的一方

        一对一
            一对一外键字段可以建在任意一方  但是推荐你建在查询频率较高的一方


"""






class Book1(models.Model):
    # bid = models.AutoField(primary_key=True)
    # verbose_name就是对该字段的注释信息  一般情况下我们会给所有的字段都加上该参数
    title = models.CharField(max_length=64, verbose_name='书名')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='价格')
    # 年月日
    publish_time = models.DateField(auto_now_add=True)
    # 年月日 时分秒
    # models.DateTimeField()

    # 库存数 与 卖出数
    kucun = models.IntegerField(verbose_name='库存', default=1000, null=True)
    maichu = models.IntegerField(verbose_name='卖出', default=1000, null=True)

    # 使用自定义的char类型字段

    # 书对于出版社是多 所以外键字段建在书籍表
    # to就是用来指定与哪张表做关联  默认关联的就是表的主键字段
    publish = models.ForeignKey(to='Publish')  # 写字符串则无需考虑前后问题
    """
    ForeignKey在实际数据库创建字段的时候 会自动给字段加上_id的后缀
    如果你自作聪明自己加了_id的后缀 那么不好意思 我照样再后面继续加_id后缀
    """
    # publish = models.ForeignKey(to=Publish)  # 直接写表名也可以 但是必须确保表名出现再当前代码的上面

    # 多对多外键字段可以建在任意一方  但是推荐你建在查询频率较高的一方
    authors = models.ManyToManyField(to='Author')
    # 该字段是虚拟字段 仅仅是用来告诉orm创建第三张关系表而已 ...
    """
    orm会自动帮你创建书籍与作者的第三张关系表
    """



class Publish(models.Model):
    name = models.CharField(verbose_name='出版社名称', max_length=64)
    addr = models.CharField(verbose_name='出版社地址', max_length=64)
    # email varchar(254)
    email = models.EmailField(verbose_name='邮箱地址')
    # def __str__(self):
    #     return self.name

class Author(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=64)
    age = models.IntegerField(verbose_name='年龄')

    # 一对一
    author_detail = models.OneToOneField(to='AuthorDetail')
    """
    OneToOneField也会自动给字段加_id后缀 如果你写了不管 继续加_id
    """


class AuthorDetail(models.Model):
    # IntegerField默认带正负号 只能表示10位数字 无法存储手机号
    phone = models.BigIntegerField(verbose_name='电话号码')
    addr = models.CharField(verbose_name='家庭住址', max_length=64)


class User(models.Model):
    username = models.CharField(max_length=32)
    gender_choices = (
        (1, '男'),
        (2, '女'),
        (3, '其他'),
    )
    # env_choices = (
    #     ('test','测试'),
    #     ('prod','生产'),
    # )
    gender = models.IntegerField(choices=gender_choices)

    # env = models.CharField(max_length=64,choices=env_choices)
