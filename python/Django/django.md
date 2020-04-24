# Django

[TOC]



## 安装事项

### jinja2 模板语法

```python
# 安装
pip3 install jinja2
# 调用变量
res = {'username':'zzj','password':123,'hobby':['run','music']}
{{ res }}
<p>{{ res.username }}</p>
<p>{{ res.get('password') }}</p>
<p>{{ res['hobby'] }}</p>
<p>{{ res['hobby'].0 }}</p>
<p>{{ res['hobby'].1 }}</p>
# for 循环
{% for user_dic in user_list %}
	<tr>
		<td>{{ user_dic.id }}</td>
		<td>{{ user_dic.username }}</td>
		<td>{{ user_dic.password }}</td>
	</tr>
{% endfor %}
```



### 创建Django项目

```python

# 安装
pip3 install django==1.11.11
# 创建django项目
django-admin startproject 项目名
# 启动django项目
python3 manage.py runserver host:port
# 创建app
python3 manage.py startapp 应用名
```



### 配置静态文件

* settings.py


1. 静态文件路劲

   ```python
   STATIC_URL = '/static/'
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR,'static')# 将static文件夹暴露给外界
   ]
   # 并创建static目录，将bootstrap.min.css和bootstrap.min.js放入目录中
   ```

2. 文件动态配置

   ```python
   {% load  static %}
   <link rel="stylesheet" href="{% static 'bootstrap-3.3.7-dist/css/bootstrap.min.css' %}">
   <script src="{% static 'bootstrap-3.3.7-dist/js/bootstrap.min.js' %}"></script>
   ```

3. 更多静态文件资源配置(了解）

   ```python
   STATICFILES_DIRS = [  # 一旦接口前缀正确 会按照从上往下的顺序依次去下面的文件夹中查找文件,找到一个立刻结束
   os.path.join(BASE_DIR,'static'),  # 将static文件夹暴露给外界
   os.path.join(BASE_DIR,'static1'),  # 将static文件夹暴露给外界
   ]
   ```



### 特别注意事项 

* settings.py

1. 创建的app一定要取配置文件中注册才能生效	

```python
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	# 我们自己创建的app必须要到这个地方注册
	'app01.apps.App01Config'  # 全写
	'app01'  # 支持简写
]
```
2. 命令行创建不会自动创建templates文件夹 需要你手动创建并且还需要取配置文件中配置加一句配置

```python
[os.path.join(BASE_DIR, 'templates')]
	TEMPLATES = [
		{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
		'APP_DIRS': True,
		'OPTIONS': {
		'context_processors': [
		'django.template.context_processors.debug',
		'django.template.context_processors.request',
		'django.contrib.auth.context_processors.auth',
		'django.contrib.messages.context_processors.messages',
				],
			},
		},
]
```

## MTV模型![](https://yinyueka-1300115034.cos.ap-shanghai.myqcloud.com/test/MTV.png)

## 路由层

* urls.py

### 路由匹配

```python
from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'^login/$',views.login)
]
```



### 路由分发

```python
from django.conf.urls import url,include
url(r'^app01/',include('app01.urls')),
url(r'^app02/',include('app02.urls'))
# 注意路由分发之所以能够实现 前提是 总路由里面url千万不能以$结尾
```



### 无名与有名分组

```python
# 无名分组:将括号内的正则表达式匹配到的内容当做位置参数传递给视图函数
url(r'^index/(\d+)/',views.index)
# 有名分组:将括号内的正则表达式匹配到的内容当做关键字参数传递给视图函数
url(r'^index/(?P<别名>\d+)/',views.index)有名分组
# views.py
def login(request, year):
    print(year)
    return HttpResponse()
```



### 反向解析 


  * 事先先给路由与视图函数对应关系起一个别名,然后通过一些方法借助于该别名得到一个返回结果  该结果能够再次访问到对应的路由

1. 有名解析

   ```python
   # python代码
   url(r'^shopper/(\d+)/', views.shopper,name='shop'),
   # 前端解析
   <a href="{% url 1 'shop' %}">111</a>
   # 后端解析
   print(reverse('shop'，args=(1,))) >>/shopper/
   ```
   
2. 有名解析test/数字/
   ```python
   # python代码
   url(r'^test_add/(?P<year>\d+)/',views.testadd,name='add')#
   #前端解析
   {% url 'add' 数字 %}#推荐使用上面这种
   {% url 'add' year=数字 %}
#后端解析
   reverse('add',args=(数字,))
   reverse('add',kwargs={'year':数字})
   ```



### 名称空间（了解）

* 当有多个应用下给路由与视图函数其别名冲突的情况下，反向解析并不会自动解析出对应的路径，那么如何解决该问题

  1. 利用名称空间的概念

     ```python
     # 在总路由分发的时候 还可以给每一个应用创建名称空间
     # 路由分发与名称空间
         url(r'^app01/',include('app01.urls',namespace='app01')),
         url(r'^app02/',include('app02.urls',namespace='app02')),
     # 子路由
         #app01
         url(r'^index/',views.index,name='index')
         #app02
         url(r'^index/',views.index,name='index')
     # 反向解析
     	reverse('app01:index')
     	reverse('app02:index')
     ```

  2. 只需要保证同一个django项目别名不冲突即可

     ```python
     #我们可以规定在期别名的时候，默认加上应用名前缀
     url(r'^index/',views.index,name='app01_index')
     url(r'^index/',views.index,name='app02_index')
     ```
  
     

## 视图层

### 三种返回方法

1. HttpResoponse返回字符串

2. render返回一个html页面

3. redirect内部重定向

   ```python
   def index(request):
       return HttpResponse()
       return render(request, 'index.html')
       return redirect('/login')
   """
   视图函数必须要返回一个HttpResponse对象
   The view day01.urls.index didn't return an HttpResponse object. It returned None instead.
   
   class HttpResponse
   
   def render():
       return HttpResponse(content, content_type, status)
      
   reidrect父类的父类继承的也是HttpResponse类
   """
   ```



### 前后端数据交换（JsonResponse）

​       前后端交互数据依赖的就是json格式的数据 因为python后端和前端js都支持json格式的数据并且都能够序列化反序列化

```python
# 使用JsonResponse
return JsonResponse(user_dict,json_dumps_params={'ensure_ascii':False})
# 针对非字典格式的数据 需要加safe参数
l = [1,2,3,4,5,6,7,8]
return JsonResponse(l,safe=False)
```



### 上传文件（form 表单）

1. form表单中比较重要的参数
   * action:控制后端提交路径
   * method:控制提交的方式(默认是get请求)
   * enctype:控制数据提交的编码格式(默认不支持传文件)
   * novalidate:取消浏览器帮我们做的一系列校验动作
2. form表单上传文件需要制定的参数
   * enctype必须有默认的urlencoded改成formdata
   * method必须是post

```python
#代码演示
def file(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)  # 获取文件数据
        file_obj = request.FILES.get('file')  # 文件对象
        print(file_obj.name)  # 查看文件名

        with open(file_obj.name,'wb') as f:
            for chunk in file_obj.chunks():  # 循环读取文件每一行内容写入硬盘
                f.write(chunk)

    # 先返沪给用户一个可以上传文件的页面
    return render(request,'file.html')


urlpatterns = [
    url(r'^file/',views.file)
]
```

```html
<form action="" method="post" enctype="multipart/form-data">
<p>name:<input type="text" name="username"></p>
<p>file:<input type="file" name="file"></p>
<input type="submit">
</form>
```

### FBV与CBV



## 模版层

### 传值

```python
# 第一种:指名道姓的传(节省资源)
return render(request,'ab_render.html',{'data':user_dic})`
# 第二种:简单暴力 直接讲当前名称空间中所有的名字全部传递给html文件  
return render(request,'ab_render.html',locals())
# 调用
前端通过{{}}就可以获取到后端传入的变量 {{ i }}
```



### 过滤器

```html
<h1>过滤器:|  |左边的是第一个参数 右边的是第二个参数</h1>
<p>加:{{ i|add:100}}</p>
<p>求长度:{{ l|length }}</p>
<p>默认值:{{ bb|default:'这个玩意没有值' }}</p>
<p>切片操作:{{ l|slice:'0:5:2' }}</p>
<p>文件大小:{{ file_size|filesizeformat }}</p>
<p>截取字符(三个点也算):{{ s|truncatechars:10 }}</p>
<p>截取单词(三个点不算):{{ s|truncatewords:3 }}</p>
<p>截取单词(三个点不算):{{ ss|truncatewords:3 }}</p>
<p>格式化日期{{ today|date:'Y年/m月' }}</p>
<p>让浏览器自动识别html标签并渲染:{{ html_s|safe }}</p>
<p>{{ link|safe }}</p>
#python里
link = '<a href="http://www.bilibili.com" target="_blank" >111</a>'
```



### 流程控制

```python
# 相当于for i in [1,2,3,4]
{% for foo in l %} 
    {% if forloop.first %}
        <p>这是我的第一次</p>
    {% elif forloop.last %}
        <p>这是最后一次了啊</p>
    {% else %}
        <p>{{ foo }}</p>
    {% endif %}
{% endfor %}
```



### 自定义

* 必须要按照下面的三步操作
  1. 在应用下新建一个名称必须叫templatetags文件夹
  2. 在该文件夹下创建一个任意名称的py文件
  3.  在该py文件内 必须先写以下两行代码

```python
from django.template import Library
	register = Library()
# 自定义过滤器
@register.filter(name='my_filter')
def func(x, y):
    #变量加减
    return x + y
# 自定义标签
@register.simple_tag(name='my_simple')
def index(a,b,c,d,*args,**kwargs):
	#字符拼接
    return '%s-%s-%s-%s'%(a,b,c,d)
```

```python
# 使用自定义标签
<h1>自定义过滤器及标签的使用过滤器最多只能接受两个参数标签则没有参数限制</h1>
{% load mytag %}
{{ 1|my_filter:10 }}
{% my_simple 1 2 3 4 %}
```



### 继承

* 一般情况下我们会在模板页面是那个定义三块区域，这样的好处就在于继承模版的主页面还可以有自己的css样式和js代码
```python
# home.html
{% block css %}
{% endblock %}

{% block content %}
{% endblock %}

{% block js %}
{% endblock %}
```
* 子页面使用
```python
# login.html
{% extends 'home.html' %}
{% block content %}
     <p>登入</p>
{% endblock %}
{% block css %}
	    <style>
        h1 {
            color: #1b6d85;
        }
        </style>
{% endblock %}
{% block css %}
	alert(123)
{% endblock %}
```

### 导入（了解）

```python
# 当某一块前端样式需要被很多页面使用的时候 你就可以考虑使用模版的导入来简化代码量
{% include 'myform.html' %}
```

> ​	总结 

```python
{{}}:变量相关
{%%}:逻辑相关
```

## 模型层

### django连接MySQL

1. 配置文件中修改配置

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'orm',  # 要连接的数据库，连接前需要创建好
        'USER': 'zzj',  # 连接数据库的用户名
        'PASSWORD': '4dAnFoLdh7mB39yCp76E',  # 连接数据库的密码
        'HOST': '47.97.44.176',  # 连接主机，默认本级
        'PORT': 13006,  # 端口 默认3306
        'CHARSET': 'utf8'
    }
}
```
2. 去项目名或者应用名下面的__init__文件指定连接mysql的模块由默认的mysqldb换成pymysql

```python
import pymysql
pymysql.install_as_MySQLdb()
```



### django对库的[命令](http://naotu.baidu.com/file/3d05365eaff310f683d09833b58284e4?token=86e1300d52704336)

1. 创建库[参考](https://www.cnblogs.com/liuqingzheng/articles/9627915.html)

   ```python
   # 在项目中的models.py
   class Book(models.Model):
       title = models.CharField(max_length=64, verbose_name='书名')
       price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='价格')
       publish_date = models.DateField()
   
   #执行下面的两条命令
   1.python3 manage.py makemigrations
   将操作数据库的操作记录到小本本上(应用下的migrations文件夹)
   2.python3 manage.py migrate 将models里面的操作同步到数据库中
   ```

2. 增删改查操作[参考](https://www.cnblogs.com/xiaoyuanqujing/articles/11643894.html)

   ```python
   #filter()
   res = models.User.objects.filter(username=username)
   
   #all()
   res = models.Book.objects.all() #<QuerySet [<Book: 水浒传>]>
   
   #filter() pk会自动查找当前表的主键字段
   res = models.Book.objects.filter(pk=2)  #<QuerySet [<Book: 水浒传>]>
   
   #get() 不推荐你使用get 因为当筛选条件不存在的时候get会直接报错.
   res = models.Book.objects.get(pk=100)
   
   #values(字典) and values_list(元组)
   models.Book.objects.values('title',)#<QuerySet [{'title': '三国演义'},]>
   res = models.Book.objects.values_list('title','price')
   #<QuerySet [('三国演义', Decimal('345.32'))]>
   
   #count()
   res = models.Book.objects.count()# 2
   
   #distinct()  去重(一定要是完全一样的数据才能去重)
   # 主键不同 （错误）
   res = models.Book.objects.all().distinct()
   # 完全一样的数据
   res = models.Book.objects.values('title').distinct()
   
   #order_by()排序
   res =order_by() models.Book.objects.order_by('price')  # 默认是升序
   res = models.Book.objects.order_by('-price')  # 加减号降序
   ...
   #增create()
   user_obj =models.User.objects.create(username=username,password=password)
   #改1.update()  批量更新
   models.User.objects.filter(id=1).update(username='jasonNB')
   #删1.delete()  批量删除
   models.User.objects.filter(id=2).delete()
   
   ```

3. 双下划线操作

   ```python
   res = models.Book.objects.filter(price__gt=400)
   res = models.Book.objects.filter(price__lt=300)
   res =models.Book.objects.filter(price__range=(300,500))
   res =models.Book.objects.filter(price__in=(300,500,400))
   res =models.Book.objects.filter(publish_date__year=2019)
   res =models.Book.objects.filter(publish_date__month=(2019))
   res =models.Book.objects.filter(tilte__icontains=(2019))
   res =models.Book.objects.filter(tilte__contains=(2019))
   print(res.query)
   print(res)
   ```

* 查看 所有orm内部sql语句(拷贝以下代码到settings.py文件即可)

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}
```



### django如何创建表外键关系

orm创建表关系的时候遵循以下规则:

* 一对多：外键字段建在多的那一方  

* 多对多：需要创建第三张表来维护关系，多对多外键字段可以建在任意一方，但是推荐你建在查询频率较高的一方

* 一对一：一对一外键字段可以建在任意一方  但是推荐你建在查询频率较高的一方

* 一对多和一对一都会自动给字段加_id后缀

```python
# 以图书管理系统为例
# verbose_name就是对该字段的注释信息  一般情况下我们会给所有的字段都加上该参数
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=64,verbose_name='书名')
    price = models.DecimalField(max_digits=8,decimal_places=2,verbose_name='价格')
    publish_time = models.DateField()
    # 因为一个出版社可以出多本书，所以书是多。
    # 默认关联的表的主键字段
    publish = models.ForeignKey(to='Publish')
    # 书和作者是多对多的关系
    authors = models.ManyToManyField('Author')
    
class Publish(models.Model):
    name = models.CharField(verbose_name='出版社名称', max_length=64)
    addr = models.CharField(verbose_name='出版社地址', max_length=64)
    email = models.EmailField(verbose_name='邮箱地址')

class Author(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    author_detail = models.OneToOneField(to='AuthorDetail')

class AuthorDetail(models.Model):
    # IntegerField默认带正负号 只能表示10位数字 无法存储手机号
    phone = models.BigIntegerField(verbose_name='电话号码')
    addr = models.CharField(verbose_name='家庭住址', max_length=64)

```



### Django外键字段的增删改查

1. 一对多外键自建的增删改查

   ```python
   # 增
   models.Book1.objects.create(title='sgyy',price=232.3,publish_date='2020-2-25',publish_id=1)
   
   publish_obj = models.Publish.objects.filter(pk=2).first()
   models.Book1.objects.create(title='fsb', price=223.3, publish_date='2020-2-25', publish=publish_obj)
   
   #改
   models.Book1.objects.filter(pk=1).update(publish_id=3)
   
   publish_obj = models.Publish.objects.filter(pk=1).first()
   models.Book1.objects.filter(pk=2).update(publish=publish_obj)
   '''
   经常使用的是对象操作数据
   '''
   # 删除（基本不会删数据）
   
   # 查 
   
   ```

   

2. 多对多外键自建的增删改查

   * 增

     ```python
     '''
     add
     	去多对多第三张关系表中添加数据;
     	括号内即可以传数字也可以传数据对象;
     	并且支持传多个，逗号隔开即可!!!
     '''
     # 方法一：
     book_obj = models.Book1.objects.filter(pk=2).first()
     book_obj.authors.add(1)
     # 方法二：
     book_obj = models.Book1.objects.filter(pk=2).first()
     authors_obj = models.Author.objects.filter(pk=2).first()
     authors_obj1 = models.Author.objects.filter(pk=3).first()
     book_obj.authors.add(authors_obj,authors_obj1)
     ```
   
     
   
   * 修改
   
     ```python
     """
       set
     	括号内既可以传数字也可以传数据对象
       	并且也都支持多个
       	但是传的必须是可迭代对象(),[],
           内部 先删除后新增
     """
     # 方法一：
     book_obj = models.Book1.objects.filter(pk=2).first()
     book_obj.authors.set([1,3])
     # 方法二：
     authors_obj = models.Author.objects.filter(pk=2).first()
     authors_obj1 = models.Author.objects.filter(pk=3).first()
     book_obj = models.Book1.objects.filter(pk=3).first()
     book_obj.authors.set([authors_obj, authors_obj1])
     ```
   
     
   
   * 删除
   
     ```python
     """
     remove  
            括号内既可以传数字也可以传数据对象
            并且支持传多个
     """
     # 方法一：
     book_obj = models.Book1.objects.filter(pk=2).first()
     book_obj.authors.remove(1)
     # 反法二：（同上）
     ```
   
     
   
   * 清空
   
     ```python
     """
     clear
     	括号内无需传递任何参数
     """
     book_obj = models.Book1.objects.filter(pk=2).first()
     book_obj.authors.clear()
     ```



### Django正反向的概念

>**跨表查询口诀
>	正向查询按外键字段
>	反向查询按表名小写**

* 正向：A>B中查找，如果A中有B的外键

* 反向：就是反过来查，B没有A的外键

  **总结：就是看外键在谁那里**



[多表操作参考博文](https://www.cnblogs.com/xiaoyuanqujing/articles/11643910.html)

### 基于对象的跨表的查询（mysql子查询）

```python
# 查询书籍主键为1的出版社名称
book_obj = models.Book1.objects.filter(pk=1).first()
res = book_obj.publish.name
print(res)
```

```python
# 查询书籍主键id为1的作者姓名
book_obj = models.Book1.objects.filter(pk=1).first()
# print(book_obj.authors)  # app01.Author.None
res = book_obj.authors.all().last().name
print(res)
```

```python
#查询zzj作者手机
author_obj = models.Author.objects.filter(name='zzj').last()
res = author_obj.author_detail.phone
print(res)
```

```总结：外键字段关联的数据可能有多条还是单条来决定是否加all()```

```python
# 查询是东方出版社出过的书籍
publish_obj = models.Publish.objects.filter(name='东方出版社').first()
res = publish_obj.book1_set.all().values('title',)
print(res)
```

```python
# 查询手机号是120的作者
author_detail_obj = models.AuthorDetail.objects.filter(phone=110).first()
print(author_detail_obj.author.name)
```

```总结：当结果为多个的时候需要用_set.all()反之不需要用_set.all()```



### 基于双下划线跨表查询（连表查询）

```python
# 查询主键为1的书籍的出版社名称
res = models.Book.objects.filter(pk=1).values('publish__name','publish__addr','title')
print(res)
# 查询东方出版社出版社过的书籍名称
res = models.Publish.objects.filter(name='东方出版社').values('book__title')
print(res)
#查询主键为1的书籍的出版社名称( 不用Book表 )
res = models.Publish.objects.filter(book__pk=1).values('name')
print(res)
# 查询书籍主键为1的书对应的作者的手机号码
res = models.AuthorDetail.objects.filter(author__book1__pk=1).values('phone')
print(res)
```

### 聚合查询

```python
# 关键字 
aggregate
from django.db.models import Max,Min,Count,Sum,Avg
# 只要是跟数据库相关的模块 一般情况下都在django.db.models下面
res = models.Book.objects.aggregate(Sum('price'),Count('pk'),Avg('price'),Max('price'),Min('price'))
```

### 分组查询

```python
# 关键字
annotate

'''
models后面点什么表名 就按照什么分组
	models.Book.objects.annotate  按照书分组
如果我想按照表中的某个字段分组 
	models.Book.objects.values('price').annotate()  values括号内写什么就按照什么分组
'''
 
# 统计作者出的价格最高的一本书
res = models.Author.objects.annotate(mp=Max('book1__price')).values('name','mp')
print(res)

# 统计每个出版社出版了多少书
res = models.Publish.objects.annotate(bc=Count('book1__pk')).values('name','bc')
print(res)

# 统计不止一个作者的图书
res = models.Book1.objects.annotate(ac=Count('authors__pk')).filter(ac__gt=1).values('title','ac')
print(res)

# 4.查询各个作者出的书的总价格
res = models.Author.objects.annotate(sb=Sum('book1__price')).values('name', 'sb')
print(res)
```

`你要统计的作为分组，annotate后面跟着查的数据`

### F与Q查询

```python
from django.db.models import F ,Q

# F

# 1 查询 库存数大于卖出数的书籍名称
res = models.Book.objects.filter(kucun__gt=900)  #查询条件数据来源于数据库表其他字段
res = models.Book.objects.filter(kucun__gt=F('maichu'))
print(res)

# 2 将所有书籍的价格全部上涨100块
models.Book.objects.update(price=F('price')+100)

# 3 给所有书的名字后面加爆款  （了解）
# 报错
models.Book.objects.update(title=F('title')+'爆款')

# 正确写法 较为繁琐
from django.db.models.functions import Concat
from django.db.models import Value

ret3 = models.Book.objects.update(name=Concat(F('name'), Value('爆款')))


#F

"""
filter在不借助于其他任何方法的前提下 只支持and关系
"""
res = models.Book.objects.filter(Q(title='三国演义'),Q(kucun=1000))  # 逗号隔开还是and关系
res = models.Book.objects.filter(Q(title='三国演义')|Q(kucun=1000))  # |  or
res = models.Book.objects.filter(~Q(title='三国演义')|Q(kucun=1000))  #  ~  not
print(res)


# Q
q = Q()  # 1 先生成一个q对象  q对象默认也是and关系

q.connector = 'or'  # 将默认的and关系改为or
q.children.append(('title','三国演义'))  # 添加筛选条件
q.children.append(('kucun',1000))

res = models.Book1.objects.filter(q)
print(res)
```

### 常用字段及参数 

**[链接参考](https://www.cnblogs.com/liuqingzheng/articles/9627915.html)**

| ORM常用字段         | 对应mysql类型及用法                             |
| :------------------ | ----------------------------------------------- |
| AutoField()         | 专门用来定义表的主键字段 primary_key = True     |
| CharField()         | 必须指定max_length  对应到数据库是varchar类型   |
| IntergerField()     | int                                             |
| BigIntergerField()  | bigint                                          |
| DecimalField()      | decimal(小数) max_digits decimal_places         |
| EmailField()        | varchar                                         |
| DateField()         | date                                            |
| DateTimeField()     | datetime                                        |
| BooleanField(Field) | 布尔值类型（但是真正到了数据库会自动转换成1/0） |
| TextField(Field)    | 文本类型（专门用来存储大段文本内容!!!）         |
| FileField(Field)    | 字符串，路径保存在数据库                        |

```python
# 参数详情
DateField()			date
DateTimeField()  datetime
# 有两个参数
  - auto_now_add:在数据创建的时候会自动将当前创建时间添加到该字段中，后续不会修改除非人为主动修改
  - auto_now:每一次修改数据的时候 都会将当前修改的时候自动添加到该字段，也就是说展示的永远是最新的一次操作时间

FileField(Field) 字符串，路径保存在数据库，文件上传到指定目录
	- upload_to:用来指定文件的存储位置
"""
```

### choices参数

```python
针对可以将所有的情况枚举的字段，你就可以考虑使用choices参数

class User(models.Model):
    username = models.CharField(max_length=32)
    gender_choices = (
        (1,'男'),
        (2,'女'),
        (3,'其他'),
    )
     gender = models.IntegerField(choices=gender_choices)

      
user_obj = models.User.objects.filter(pk=4).first()
print(user_obj.gender)

# 针对choices参数的字段  如何展示对应的注释信息
"""
    固定语法:get_xxx_display()
    如果有对应关系则展示对应关系
    如果没有展示的还是数字
"""
print(user_obj.get_gender_display())
```



### 自定义类型字段	

```python
from django.db.models import Field

### 自定义char类型字段

class MyCharField(Field):
    def __init__(self,max_length,*args,**kwargs):
        self.max_length = max_length
        super().__init__(max_length=max_length,*args,**kwargs)
def db_type(self, connection):
    return 'char(%s)'%self.max_length


# 重要参数
max_length
default
null
verbose_name
blank=True  # 用来告诉Django admin后台管理该字段可以为空
# 一般情况下为了兼容 我们会给可以为空的字段加上两个参数
is_eat = models.CharField(null=True,blank=True)

db_index
如果db_index=True 则代表着为此字段设置索引。

"""
注意django1.X在创建外键关系的时候默认都是级联更新纪念删除的
但是2.X以上需要你自己手动加上

db_constraint
on_delete
on_update
"""
```

## 

### 









































# ajax

## ajax基本使用

```python
$('#submit').click(function () {
    $.ajax({
      url:'',  # 填写后端地址
      type:'',  # 填写请求方式
      data:'',  # 填写交互的数据 如果是get请求该参数可加可不加(url?后面有没有参数)
      dataType:"JSON",
      success:function(args){
        # 异步提交任务一旦有结果会自动将结果返回给该函数 该函数自动执行
      }
    })
}
# 参数详情
dataType参数：能够自动帮你讲json格式字符串的二进制数据直接自动解码并反序列化成前端js中的对象类型
如果HttpReponse返回的需要用这个dataType参数
而JsonReponse不用使用dataType参数
"""
前后端交互数据类型一般都是字典
在写ajax请求的时候 dataType参数加着 这样是最优的选择
"""
```

## 前后端传输数据编码格式(请求头里面的contentType参数)

1. **urlencoded**

   ```
   form 表单默认提交的编码格式urlencoded
   	django后端针对符合urlencoded编码格式的数据会自动解析并放到request.POST中供用户使用
   	urlencoded编码数据格式：username=jason&password=123
   ```

2. **formdata**

   ```
   django后端针对formdata格式的数据
   	会将符合urlencoded格式数据还是自动解析并放到requets.POST
   	而针对文件数据则会自动解析放到request.FILES中
   
   form表单是无法发送json格式数据的
   ```

3. **json/application**

   ```
   ajax默认提交数据的方式也是urlencoded 
   这里就能够解释为什么form和ajax提交post请求后端都是从request.POST中获取数据
   name=egon&password=123
   ```

   

## ajax发送json格式数据

```python
# 前后端数据交互的时候 你不能欺骗对方 一定要做到数据和编码格式一致性
"""
django后端针对json格式的数据不会做任何的处理
而是原封不动的放在request.body中
需要你自己获取并自己处理
"""
print(request.body)
json_bytes = request.body
# json.loads可以反序列化符合json格式的二进制数据 能够自动识别需要先解码再反序列化
json_dict = json.loads(json_bytes)


data:JSON.stringify({'name':'tank','password':123}),
// 编码格式
contentType:'json/application',
```

## ajax发送文件数据

```python
# ajax发送文件数据 需要借助于内置对象FormData
"""该对象即可以携带文件数据也可以携带普通的键值对(符合urlencoded格式)"""
function sendMsg() {
        var myFormData = new FormData();
        // 添加普通键值对
        myFormData.append('username','jason');
        myFormData.append('password','666');
        // 添加文件数据
        myFormData.append('myfile',$('#d1')[0].files[0]);

        $.ajax({
            url:'',
            type:'post',
            data:myFormData,

            // 发送文件必须要指定两个参数
            processData:false,  // 告诉浏览器对数据不做任何处理
            contentType:false,  // 不使用任何编码 因为django后端能够自动识别myFormData对象

            success:function (args) {
                console.log(agrs)
            }
        })
    }
```

## 批量插入数据

```python
def pl(request):
    # 朝book表中添加1000条数据
    # for i in range(1,10001):
    #     # 频繁操作数据库 压力过大
    #     models.Book.objects.create(title='第%s本书'%i)
    # 批量插入数据
    book_list = []
    for i in range(1,10001):
        book_list.append(models.Book(title='第%s本书'%i))  # 朝列表中添加数据对象
    models.Book.objects.bulk_create(book_list)  # 10s

    # 再将数据展示到前端页面
    book_queryset = models.Book.objects.all()  # 2s
    return render(request,'pl.html',locals())
```

## 分页器