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
   ./configure --prefix=/usr/local
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

