# python安装liunx

<hr>

1. 下载

* [python 3.6.10](https://www.python.org/downloads/release/python-3610/)

* 自己的钉钉云存储里有

2. 下载编译python3的依赖包

   ```shell
   yum install -y gcc patch libffi-devel python-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
   ```

3. 编译安装

   ```shell
   # 解压
   tar -zxvf Python-3.6.10.tgz && cd Python-3.6.10
   # 编写配置
   ./configure --prefix=/usr/local/python3.6 --with-ssl
   # 编译安装 
   make &&  make install 
   # 修改环境变量
   vim  /etc/profile
   PYTHON_PATH=/usr/local/python3.6
   export PATH=$PATH:$PYTHON_PATH/bin
   
   source /etc/profile
   
   ```

   

# python创建虚拟环境

> 本环境是python3为基础 

## 安装虚拟环境

```shell
sudo pip3 install virtualenv
sudo pip3 install virtualenvwrapper
```

## 配置环境变量及创建目录

```shell
# 1、在~（家目录）下创建目录用来存放虚拟环境
mkdir .virtualenvs

# 2、打开~/.bashrc文件，并添加如下：
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/python3/bin/python3.6
source /usr/local/python3/bin/virtualenvwrapper.sh

# 3、重新读取环境变量
source ~/.bashrc
```

* WORKON_HOME ：放置你的虚拟环境目录
* VIRTUALENVWRAPPER_PYTHON： 虚拟环境所用的python版本

## 命令创建虚拟环境

```python
# mkvirtualenv -p python版本 虚拟环境名称
mkvirtualenv -p python3 TEST
```

## 如何使用虚拟环境

1. 查看所有的虚拟环境命令

```pyhon
workon
```

2. 进入（使用）虚拟环境命令

```shell
workon TEST
```

3. 退出虚拟环境的命令

```shell
deactivate
```

4. 删除虚拟环境

```shell
rmvirtualenv TEST
先退出：deactivate
再删除：rmvirtualenv TEST
```

# python遇到的知识点总结

## 反射

* ```__getattr__```：当使用点号获取实例属性时，如果属性不存在就自动调用__getattr__方法
* ```__setattr__```：当设置类实例属性时自动调用，如``` self.name = "Liu" ```就会调用__setattr__方法 ，并 执行```self.__dict__[key] = value``` 写入 ```__dict__```中。

```python
class Fun:
    def __init__(self):
        self.name = "Liu"
        self.age = 12
        self.male = True

    def __getattr__(self, value):
        return len

    def __setattr__(self, key, value):
        print("*" * 50)
        print("设置的key:{},  设置的value:{}".format(key, value))
        print("__dict__目前数据 : {}".format(self.__dict__))
        # 属性注册
        self.__dict__[key] = value


fun = Fun()
print("*" * 50)
print("没有getpath方法，调用__getattr__ 返回len的指针执行 打印字符串的长度: {}".format(fun.getpath('zzj0403')))
# 执行结果
**************************************************
设置的key:name,  设置的value:Liu
__dict__目前数据 : {}
**************************************************
设置的key:age,  设置的value:12
__dict__目前数据 : {'name': 'Liu'}
**************************************************
设置的key:male,  设置的value:True
__dict__目前数据 : {'name': 'Liu', 'age': 12}
**************************************************
没有getpath方法，调用__getattr__ 返回len的 指针 执行 打印字符串的长度: 7

```

* ```__getattribute__```当访问某个实例属性时， getattribute会被无条件调用，如未实现自己的getattr方法，会抛出AttributeError提示找不到这个属性，如果自定义了自己getattr方法的话，方法会在这种找不到属性的情况下被调用。

```PYTHON
class demo(object):
    def __init__(self):
        self.a = 10

    def __getattribute__(self, item):
        print("执行方法： __getattribute__ is called ")
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print("执行方法： __getattr__ is called")
        return item


if __name__ == '__main__':
    d = demo()
    print(d.a)
    print(d.b)

# 执行结果
执行方法： __getattribute__ is called 
10
执行方法： __getattribute__ is called 
执行方法： __getattr__ is called
b
```