# 课程目的

* 体验基础知识点拼凑项目的流程
* 常见模块的使用
* 编程思想的培养

# 课程介绍

一般的互联网公司，都会有一套自己的代码发布平台，并且大部分都是由jenjins来实现的(shell脚本)，其实也有公司自己会定制自己的代码发布平台,并且可以基于其他技术点(saltstack、PHP代码上线脚本、Java开发的脚本)

我们要实现的代码发布就是基于python技术来开发，我们开发的流程是基本流程，具体可能会根据公司业务逻辑的不同加加减减

最后强调:该项目主要用到的都是python的知识点，跟运维、测试知识点基本不沾边

# 今日内容概要

* ### 服务端给客户端推送消息

  截至目前为止，我们所学的web项目都是基于HTTP协议，有客户端主动朝服务端发送请求服务端被动的作出响应

  HTTP协议有四大特性:无/短链接(客户端请求我 我被动的响应 之后咋俩就没有关系了)

  但是我们会经常遇到这样的现象:浏览器打开一个页面，不做任何的操作，过一段时间浏览器自动弹出消息

  比如网页版的qq和微信，我们全部加入一个群聊中，只要有一个人朝群聊中发送了消息，所有人的浏览器页面上都会收到该消息

  我们能够实现服务端给客户端推送消息的感觉(伪/真)

  伪:让每个浏览器每隔一段时间主动偷偷的来服务器索要数据，如果有拿走展示到前端

  * 轮询
  * 长轮询

  真:websocket(长链接),创建链接之后默认不断开(联想网络编程socket 基于TCP的三次握手 send recv),websocket的诞生真正的实现了服务端给客户端主动推送消息

  * websocket

  服务端给客户端推送消息的实际应用场景

  * 大屏幕投票
  * 任务执行流程

* ### gojs插件

  是一个前端插件，可以通过代码动态的展示和修改图标数据(组织架构图，流程图...)

  参考网址:<https://gojs.net/latest/index.html>  

* ### paramiko模块

  底层通过ssh，类似于xshell远程链接服务器并执行操作

  ansible的底层就是用的paramiko模块

* ### gitpython模块

  python代码操作远程仓库

* ### 代码发布功能实现

  * 服务器的管理
  * 项目管理
  * 发布记录

# 重要知识点回顾

* ### ajax操作

  异步提交、局部刷新(偷偷的跟服务端做交互，而不被用户发现)

  ```python
  $.ajax({
    url:"",  # 控制后端提交路口
    type:'',  # 控制提交方式 get post put ...
    data:{},  # 提交的数据
    dataType:'JSON',
    success:function(args){
      # 异步提交之后 处理结果的回调函数
    }
  })
  
  """
  dataType:'JSON'
  该参数的含义是 当后端用的是HttpResponse返回的json格式字符串，则会自动反序列化成前端js的对象类型
  如果不加该参数，则不会自动转换
  而如果后端用的是JsonRespons返回json格式字符串，那么无论加不加该参数都会自动转换
  
  所以为了兼容性考虑，你以后在写的时候加上即可
  """
  from django.http import JsonResponse
  import json
  from django.shortcuts import HttpResponse,render
  
  def index(request):
      back_dic = {'status':True,'msg':'hello world'}
      # return HttpResponse(json.dumps(back_dic))
      return JsonResponse(back_dic)
  
  
  def home(request):
      return render(request,'home.html')
  
  urlpatterns = [
      url(r'^admin/', admin.site.urls),
      url(r'^home/$',home),
      url(r'^index/$',index)
  ]
  
  # 前端代码
  <button onclick="sendMsg()">提交</button>
  """
  给标签绑定事件的两种方式
  第一种
  	标签查找
  	$('#d1').click(function(){})
  第二种
  	行内式
  	<button onclick="sendMsg()">提交</button>
  """
  <script>
      function sendMsg() {
          $.ajax({
              url:'/index/',
              type:'get',
              {#dataType:'JSON',  // 自动处理#}
              success:function (args) {
                  {#var res = JSON.parse(args)  // 自己处理#}
                  alert(typeof args)
              }
          })
      }
  </script>
  ```

* ### 队列

  队列:先进先出

  堆栈:先进后出

  ```python
  # python内部提供了一个模块能够直接让你在内存中维护队列并操作
  
  import queue
  
  
  # 创建一个队列
  q = queue.Queue()
  
  
  # 朝队列中添加数据
  q.put(111)
  q.put(222)
  
  
  # 朝队列中获取数据
  v1 = q.get()
  v2 = q.get()
  # v3 = q.get()  # 没有数据会原地阻塞 直到给数据为止
  # v4 = q.get_nowait()  # 没有数据立刻报错
  # v5 = q.get(timeout=3)  # 没有数据等你三秒 之后再报错  queue.Empty
  try:
      v6 = q.get(timeout=3)
      print(v6)
  except queue.Empty as e:
      pass    
  print(v1,v2)
  ```

  **思考:**基于队列和ajax实现服务端给客户端推送的消息的感觉(伪)

  服务端给每一个客户端维护一个队列,然后在客户端浏览器上书写一段ajax代码请求对应队列里面的数据，没有数据会原地阻塞(pending)，

  以群聊为例，只要有一个人朝后端发送的消息，我就将该消息给每一个队列放一份

* ### 递归

  ```python
  """在python中递归说的就是函数自己无限制的调用自己"""
  def func():
    func()
  func()
  # 在python为了防止内存溢出有最大递归深度限制997 998 官网给出的1000
  
  """在js中是没有递归的概念的  函数可以自己调用自己 属于正常的事件"""
  function func1(){
    $.ajax({
      url:'',
      type:'',
      data:{},
      dataType:'JSON',
      success:fucntion(args){
        func1()
      }
    })
  }
  // 等待页面加载完毕之后自动执行
  $(function(){
    func1()
  })
  ```

* ### modelform组件

  也是一个校验性组件，比forms组件更加的强大

  能够非常快速的帮你完成数据的增删改查操作

  

# 今日内容详细

## 服务端给客户端推送消息的效果

* 轮询(伪)
* 长轮询(伪)
* websocket(真)

### 轮询(效率低、基本不用)

```python
"""
让客户端浏览器每隔一段时间(每隔5s)主动朝服务端偷偷的发送请求

缺点:
	消息延迟(5S+网络延迟)
	请求次数多(24小时消耗资源都很高)
"""
```

### 长轮询(使用广泛、兼容性好)

```python
"""
服务端给每一个客户端浏览器创建一个队列，浏览器通过ajax偷偷的朝服务器索要队列中的数据，如果没有数据则会原地阻塞30s但是不会一直阻塞而是利用timeout参数加异常处理的方式，如果超出时间限，客户端在此发送请求数据的请求(递归调用)

优点:
	消息基本没有延迟
	请求次数降低了，节省资源
"""
# 目前大公司都喜欢使用长轮询，比如网页版的qq和微信
```

**基于长轮询原理实现简易版本的群聊功能**

ps:当你使用pycharm创建django项目的时候会自动帮你创建模版文件夹，但是你在终端或者服务器上创建项目的时候是没有该文件夹的

django的每一个应用都可以有自己的urls.py，模版文件夹，静态文件...

当全局没有模版文件夹的时候，那么在查找模版的时候顺序是按照配置文件中注册了的app的顺序，从上往下一次查找

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01.apps.App01Config',
]
```

```python
# 后端
from django.shortcuts import render,HttpResponse
import queue
from django.http import JsonResponse
# Create your views here.


q_dict = {}  # {'jason'："jason的队列对象",...}


def home(request):
    # 获取自定义的客户端唯一标示
    name = request.GET.get('name')
    # 给字典添加键值对 键是唯一表示 值是队列对象
    q_dict[name] = queue.Queue()
    # 返回给前端一个聊天室页面
    return render(request,'home.html',locals())


def send_msg(request):
    # 获取用户发送的消息
    content = request.POST.get('content')
    # 给多有的队列放一份当前数据
    for q in q_dict.values():
        q.put(content)
    return HttpResponse('OK')


def get_msg(request):
    # 获取客户端唯一标示
    name = request.GET.get('name')
    # 获取唯一标示对应的队列对象
    q = q_dict.get(name)
    back_dic = {'status':True,'msg':''}
    try:
        data = q.get(timeout=10)
        back_dic['msg'] = data
    except queue.Empty as e:
        back_dic['status'] = False
    return JsonResponse(back_dic)
```

```html
<h1>聊天室:{{ name }}</h1>
<div>
    <input type="text" id="txt">
    <button onclick="sendMsg()">发送消息</button>
</div>
<h1>聊天记录</h1>
<div class="record">

</div>

<script>
    function sendMsg() {
        $.ajax({
            url:'/send_msg/',
            type:'post',
            data:{'content':$('#txt').val()},
            success:function (args) {

            }
        })
    }

    function getMsg() {
        $.ajax({
            url:'/get_msg/',
            type:'get',
            data:{'name':'{{ name }}'},
            success:function (args) {
                if (args.status){
                    // 将消息通过DOM操作渲染到前端页面
                    // 1 创建标签 p标签
                    var pELe = $('<p>');
                    // 2 给p标签添加文本内容
                    pELe.text(args.msg)
                    // 3 将该p标签渲染到div内部
                    $('.record').append(pELe)
                }
                // 再次朝后端发请求
                getMsg()
            }
        })
    }
    // 等待页面加载完毕之后 立刻执行
    $(function () {
        getMsg()
    })
</script>
```

### websocket(主流浏览器都支持)

```python
"""
HTTP协议
	数据交互式明文的 没有做加密处理
HTTPS协议
	数据交互式加密的 有加密处理 更加安全
	
上述的两个协议都是短链接协议:你请求我 我响应 就完事了 
	
websocket协议
	数据交互式加密的 有加密处理 更加安全
websocket协议是长链接协议:建立连接之后默认不断开，双方都可以主动的收发消息
websocket的诞生真正的实现了服务端给客户端主动推送消息
"""
```

#### 内部原理

```python
"""
1.握手环节:验证当前客户端或者服务端是否支持websocket协议
	客户端浏览器访问服务端之后，会立刻在本地生成一个随机字符串，并且将该随机字符串自己保留然后给服务端也发送一份(基于HTTP协议进行数据交互 请求头里面)
	
	客户端和服务端都会对该随机字符串做以下处理
		1.先将该随机字符串与magic string做字符串的拼接操作(这个magic string是全球统一固定的一个字符串)
		2.再对拼接之后的结果用sha1和base64算法加密
	
	服务端将处理好的结果发送给客户端(基于HTTP协议  响应头里面)
	客户端获取到服务端发送过来的随机字符串之后与自己本地处理好的随机字符串做比对，如果两者一致说明当前服务端支持websocket协议，如果不一致说明不支持，直接报错,如果一致那么双方就会创建websocket连接
	
2.收发数据:数据的解密过程
	ps:
		1.数据基于网络传输都是二进制格式 对应到python里面可以用bytes类型标示
		2.二进制转十进制
	
	1.先读取第二个字节的后七位(payload)
	
	2.根据payload不同做不同的处理
		payload = 127:继续往后读取8个字节(报头占10个字节)
		payload = 126:继续往后读取2个字节(报头占4个字节)
		payload <= 125:不再往后继续读取(报头占2个字节)
	
	3.继续往后读取固定4个字节的数据(masking-key)
		依据该值解析出真实数据	
"""

"""
请求头
Sec-WebSocket-Key: HCLzbZUPQCdMiVf3Oc8r3g==
"""
```

#### 代码验证(无需掌握，搂一眼即可)

```python
import socket
import hashlib
import base64

# 正常的socket代码
sock = socket.socket()
# 针对mac本 重启服务端总是报端口被占用的情况
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('127.0.0.1', 8080))
sock.listen(5)
conn, address = sock.accept()
data = conn.recv(1024)  # 获取客户端发送的消息


def get_headers(data):
    """
    将请求头格式化成字典
    :param data:
    :return:
    """
    header_dict = {}
    data = str(data, encoding='utf-8')

    header, body = data.split('\r\n\r\n', 1)
    header_list = header.split('\r\n')
    for i in range(0, len(header_list)):
        if i == 0:
            if len(header_list[i].split(' ')) == 3:
                header_dict['method'], header_dict['url'], header_dict['protocol'] = header_list[i].split(' ')
        else:
            k, v = header_list[i].split(':', 1)
            header_dict[k] = v.strip()
    return header_dict

def get_data(info):
    """
    按照websocket解密规则针对不同的数字进行不同的解密处理
    :param info:
    :return:
    """
    payload_len = info[1] & 127
    if payload_len == 126:
        extend_payload_len = info[2:4]
        mask = info[4:8]
        decoded = info[8:]
    elif payload_len == 127:
        extend_payload_len = info[2:10]
        mask = info[10:14]
        decoded = info[14:]
    else:
        extend_payload_len = None
        mask = info[2:6]
        decoded = info[6:]

    bytes_list = bytearray()
    for i in range(len(decoded)):
        chunk = decoded[i] ^ mask[i % 4]
        bytes_list.append(chunk)
    body = str(bytes_list, encoding='utf-8')

    return body

header_dict = get_headers(data)  # 将一大堆请求头转换成字典数据  类似于wsgiref模块
client_random_string = header_dict['Sec-WebSocket-Key']  # 获取浏览器发送过来的随机字符串
magic_string = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'  # 全球共用的随机字符串 一个都不能写错
value = client_random_string + magic_string  # 拼接
ac = base64.b64encode(hashlib.sha1(value.encode('utf-8')).digest())  # 加密处理


tpl = "HTTP/1.1 101 Switching Protocols\r\n" \
      "Upgrade:websocket\r\n" \
      "Connection: Upgrade\r\n" \
      "Sec-WebSocket-Accept: %s\r\n" \
      "WebSocket-Location: ws://127.0.0.1:8080\r\n\r\n"
response_str = tpl %ac.decode('utf-8')  # 处理到响应头中

# 将随机字符串给浏览器返回回去
conn.send(bytes(response_str, encoding='utf-8'))


while True:
      data = conn.recv(1024)
      # print(data)  # b'\x81\x8b\xd9\xf7} \xb1\x92\x11L\xb6\xd7\nO\xab\x9b\x19'
      value = get_data(data)
      print(value)
```

```html
<!--需要你掌握前端一行代码-->
<script>
    var ws = new WebSocket('ws://127.0.0.1:8080/')
    // 这一句话干了很多是
    // 1 自动生成随机字符串
    // 2 对字符串进行一系列的处理
    // 3 接受服务端返回的结果自动做比对校验
</script>
```

总结:实际生产中我们不会使用到上面后端的代码，因为太繁琐了

我们会直接使用别人封装好的模块，内部已经帮助我们完成了上述所有的操作

## 后端框架如何支持websocket

```python
"""
并不是所有的框架都支持websocket
django
	- 默认不支持websocket
	- 可以借助于第三方的工具:channles模块
flask
	- 默认不支持
	- 可以借助于第三方的工具:gevetwebsocket模块
tornado
	- 默认就是支持的
"""
```

## django如何支持websocket

#### 安装channels模块需要注意

* 版本不能使用最新版，如果直接安装了最新版，它可能会自动将你的django版本也升级为最新版
* python解释器简易你使用3.6版本(官网的说法是：3.5可能有问题，3.7也有可能有问题)

#### 安装

```python
pip3 install channels==2.3
```

#### 基于channels模块实现群聊功能

* 配置文件中注册channles应用

  ```python
  INSTALLED_APPS = [
      # 1 注册channles
      'channels'
  ]
  # 注册之后django项目无法正常启动了
  CommandError: You have not set ASGI_APPLICATION, which is needed to run the server.
  ```

* 配置文件中定义配置ASGI_APPLICATION

  ```python
  ASGI_APPLICATION = 'zm6_deploy.routing.application'
  # ASGI_APPLICATION = '项目名同名的文件夹名.项目名同名的文件夹内创建一个py文件(默认就叫routing.py).在该py文件内容定义一个变量（application）
  
  """
  django默认的http协议 路由视图函数对应关系
  urls.py >>> views.py
  
  django支持websocket之后 需要单独创建路由与视图函数对应关系
  routing.py  >>> consumers.py
  
  扩展:当你的视图函数特别多的时候 你可以根据功能的不同的拆分成不同的py文件
  views文件夹
  	user.py
  	account.py
  	shop.py
  	admin.py
  	...
  """
  ```

* 在项目名同名的文件夹下创建routing.py文件书写以下固定代码

  ```python
  from channels.routing import ProtocolTypeRouter,URLRouter
  
  
  application = ProtocolTypeRouter({
      'websocket':URLRouter([
          # 写websocket路由与视图函数对应关系
      ])
  })
  ```

  上述配置完成后，django就会由原来的wsgiref启动变成asgi启动，并且即支持原来的http协议又支持websocket协议

  ```python
  class ProtocolTypeRouter:
      """
      Takes a mapping of protocol type names to other Application instances,
      and dispatches to the right one based on protocol name (or raises an error)
      """
      def __init__(self, application_mapping):
          self.application_mapping = application_mapping
          if "http" not in self.application_mapping:
              self.application_mapping["http"] = AsgiHandler
  ```

  url访问

  ```python
  """
  http协议
  	/index/  >>>  index函数
  	浏览器窗口直接输入url即可访问
  
  websocket
  	/chat/  >>>   ChatConsumer
  	利用js内置对象访问 new WebSocket()
  """
  ```

  后端三个方法

  ```python
  from channels.generic.websocket import WebsocketConsumer
  from channels.exceptions import StopConsumer
  
  
  consumers_object_list = []
  
  
  class ChatConsumers(WebsocketConsumer):
      def websocket_connect(self, message):
          """握手环节 验证及建立链接"""
          # print('建立链接')
          self.accept()  # 建立链接
          # 将所有链接对象添加到列表中
          consumers_object_list.append(self)
  
      def websocket_receive(self, message):
          """客户端发送消息到服务端之后自动触发该方法"""
          print(message)  # {'type': 'websocket.receive', 'text': 'hello world'}
          # 给客户端回复消息
          # self.send('你好啊')
          text = message.get('text')
          # 再给用户返回回去
          # self.send(text_data=text)  # self谁来就是谁 这里就相当于是单独发送
  
          # 循环出列表中所有的链接对象 发送消息
          for obj in consumers_object_list:
              obj.send(text_data=text)
  
      def websocket_disconnect(self, message):
          """客户端断开链接之后自动触发"""
          # print('断开了')
          # 应该将断开的链接对象从列表中删除
          consumers_object_list.remove(self)
          raise StopConsumer()
  ```

  前端四个方法

  ```html
  <h1>聊天室</h1>
  <div>
      <input type="text" id="txt">
      <button onclick="sendMsg()">发送消息</button>
  </div>
  <h1>聊天记录</h1>
  <div class="record">
  </div>
  
  <script>
      var ws = new WebSocket("ws://127.0.0.1:8000/chat/");
  
      // 1 请求链接成功之后  自动触发
      ws.onopen = function () {
          {#alert('链接成功')#}
      }
      // 2 朝服务端发消息
      function sendMsg() {
          ws.send($('#txt').val())
      }
      // 3 服务端给客户端回复消息的时候 自动触发
      ws.onmessage = function (args) {
          {#alert(args)  // 是一个对象 #}
          var res = args.data
          {#alert(res)#}
          var pEle = $('<p>');
          pEle.text(res);
          $('.record').append(pEle)
      }
      // 4 断开链接之后自动触发
      ws.onclose = function () {
          console.log('断开链接了')
      }
  </script>
  ```

  上述的群聊功能实现，是我们自己想的一种比较low的方式

  其实channels模块给你提供了一个专门用于做群聊功能的模块channle-layers模块

  该模块暂时不讲，我们放到后面写代码的时候再来看实际应用

## gojs插件

如果要想使用，需要下载它的js文件，我们这里需要了解的就三个

* go.js

  使用gojs插件必须要导入的文件,用于 生产环境

* go-debug.js

  debug模式，能够帮你打印日志，一般调试的时候使用

* Figures.js

  go.js内部自带的图标比较有限，当你发现你渲染的图标加载不出来的时候，就需要导入Figures.js

总结:在使用gojs的时候导入go.js和Figures.js就完事了

#### 基本使用

规律：先在页面上用div划定一片区域，之后所有的渲染操作全部在该div内部进行

```html
<div id="myDiagramDiv" style="width:500px; height:350px; background-color: #DAE4E4;"></div>

<script src="go.js"></script>
<script>
  var $ = go.GraphObject.make;
  // 第一步：创建图表
  var myDiagram = $(go.Diagram, "myDiagramDiv"); // 创建图表，用于在页面上画图
  // 第二步：创建一个节点，内容为jason
  var node = $(go.Node, $(go.TextBlock, {text: "jason"}));
  // 第三步：将节点添加到图表中
  myDiagram.add(node)
</script>
```

#### **概念介绍**

* TextBlock文本
* Shapes图形
* Node节点  将文本与图形结合到一起
* Link箭头 指向问题

**TextBlock文本**

```html
<div id="myDiagramDiv" style="width:500px; height:350px; background-color: #DAE4E4;"></div>
<script src="js/go.js"></script>
<script>
    var $ = go.GraphObject.make;
    // 第一步：创建图表
    var myDiagram = $(go.Diagram, "myDiagramDiv"); // 创建图表，用于在页面上画图
    var node1 = $(go.Node, $(go.TextBlock, {text: "jason"}));
    myDiagram.add(node1);
    var node2 = $(go.Node, $(go.TextBlock, {text: "jason", stroke: 'red'}));
    myDiagram.add(node2);
    var node3 = $(go.Node, $(go.TextBlock, {text: "jason", background: 'lightblue'}));
    myDiagram.add(node3);
</script>
```

**Shapes图形**

```html
<div id="myDiagramDiv" style="width:500px; height:350px; background-color: #DAE4E4;"></div>
<script src="go.js"></script>
<script src="Figures.js"></script>
<script>
    var $ = go.GraphObject.make;
    // 第一步：创建图表
    var myDiagram = $(go.Diagram, "myDiagramDiv"); // 创建图表，用于在页面上画图
    var node1 = $(go.Node,
        $(go.Shape, {figure: "Ellipse", width: 40, height: 40})
    );
     myDiagram.add(node1);
     var node2 = $(go.Node,
        $(go.Shape, {figure: "RoundedRectangle", width: 40, height: 40, fill: 'green',stroke:'red'})
    );
    myDiagram.add(node2);
    var node3 = $(go.Node,
        $(go.Shape, {figure: "Rectangle", width: 40, height: 40, fill: null})
    );
    myDiagram.add(node3);
    var node5 = $(go.Node,
        $(go.Shape, {figure: "Club", width: 40, height: 40, fill: 'red'})
    );
    myDiagram.add(node5);
</script>
```

**Node节点**

```html
<div id="myDiagramDiv" style="width:500px; height:350px; background-color: #DAE4E4;"></div>
<script src="go.js"></script>
<script src="Figures.js"></script>
<script>
    var $ = go.GraphObject.make;
    // 第一步：创建图表
    var myDiagram = $(go.Diagram, "myDiagramDiv"); // 创建图表，用于在页面上画图

    var node1 = $(go.Node,
         "Vertical",  // 垂直方向
        {
            background: 'yellow',
            padding: 8
        },
        $(go.Shape, {figure: "Ellipse", width: 40, height: 40,fill:null}),
        $(go.TextBlock, {text: "jason"})
    );
    myDiagram.add(node1);

    var node2 = $(go.Node,
        "Horizontal",  // 水平方向
        {
            background: 'white',
            padding: 5
        },
        $(go.Shape, {figure: "RoundedRectangle", width: 40, height: 40}),
        $(go.TextBlock, {text: "jason"})
    );
    myDiagram.add(node2);

    var node3 = $(go.Node,
        "Auto",  // 居中
        $(go.Shape, {figure: "Ellipse", width: 80, height: 80, background: 'green', fill: 'red'}),
        $(go.TextBlock, {text: "jason"})
    );
    myDiagram.add(node3);
</script>
```

**Link箭头**

```html

<div id="myDiagramDiv" style="width:500px; min-height:450px; background-color: #DAE4E4;"></div>
    <script src="go.js"></script>
    <script>
        var $ = go.GraphObject.make;

        var myDiagram = $(go.Diagram, "myDiagramDiv",
            {layout: $(go.TreeLayout, {angle: 0})}
        ); // 创建图表，用于在页面上画图

        var startNode = $(go.Node, "Auto",
            $(go.Shape, {figure: "Ellipse", width: 40, height: 40, fill: '#79C900', stroke: '#79C900'}),
            $(go.TextBlock, {text: '开始', stroke: 'white'})
        );
        myDiagram.add(startNode);

        var downloadNode = $(go.Node, "Auto",
            $(go.Shape, {figure: "RoundedRectangle", height: 40, fill: 'red', stroke: '#79C900'}),
            $(go.TextBlock, {text: '下载代码', stroke: 'white'})
        );
        myDiagram.add(downloadNode);

        var startToDownloadLink = $(go.Link,
            {fromNode: startNode, toNode: downloadNode},
            $(go.Shape, {strokeWidth: 1}),
            $(go.Shape, {toArrow: "OpenTriangle", fill: null, strokeWidth: 1})
        );
        myDiagram.add(startToDownloadLink);
    </script>
```

思考:上述的数据都是直接在页面上写死的，如何做到数据是从后端动态获取并渲染呢？？？

#### 数据绑定式

```html
<div id="diagramDiv" style="width:100%; min-height:450px; background-color: #DAE4E4;"></div>

    <script src="go.js"></script>
    <script>
        var $ = go.GraphObject.make;
        var diagram = $(go.Diagram, "diagramDiv",{
            layout: $(go.TreeLayout, {
                angle: 0,
                nodeSpacing: 20,
                layerSpacing: 70
            })
        });

        diagram.nodeTemplate = $(go.Node, "Auto",
            $(go.Shape, {
                figure: "RoundedRectangle",
                fill: 'yellow',
                stroke: 'yellow'
            }, new go.Binding("figure", "figure"), new go.Binding("fill", "color"), new go.Binding("stroke", "color")),
            $(go.TextBlock, {margin: 8}, new go.Binding("text", "text"))
        );

        diagram.linkTemplate = $(go.Link,
            {routing: go.Link.Orthogonal},
            $(go.Shape, {stroke: 'yellow'}, new go.Binding('stroke', 'link_color')),
            $(go.Shape, {toArrow: "OpenTriangle", stroke: 'yellow'}, new go.Binding('stroke', 'link_color'))
        );

        var nodeDataArray = [
            {key: "start", text: '开始', figure: 'Ellipse', color: "lightgreen"},
            {key: "download", parent: 'start', text: '下载代码', color: "lightgreen", link_text: '执行中...'},
            {key: "compile", parent: 'download', text: '本地编译', color: "lightgreen"},
            {key: "zip", parent: 'compile', text: '打包', color: "red", link_color: 'red'},
            {key: "c1", text: '服务器1', parent: "zip"},
            {key: "c11", text: '服务重启', parent: "c1"},
            {key: "c2", text: '服务器2', parent: "zip"},
            {key: "c21", text: '服务重启', parent: "c2"},
            {key: "c3", text: '服务器3', parent: "zip"},
            {key: "c31", text: '服务重启', parent: "c3"}
        ];
        diagram.model = new go.TreeModel(nodeDataArray);
        // 动态控制节点颜色变化
        var node = diagram.model.findNodeDataForKey("zip");
        diagram.model.setDataProperty(node, "color", "lightgreen");
    </script>
```

#### 如何去除gojs自带的水印

1.去go.js文件中查找一个固定的字符串，并注释掉该字符串所在的一行代码

```js
"""
7eba17a4ca3b1a8346
"""
a.kr=b.V[Ra("7eba17a4ca3b1a8346")][Ra("78a118b7")](b.V,Jk,4,4);
```

2.在注释掉的地方添加一行代码

```js
a.kr=function(){return false};
```

## paramiko模块

**安装**

```python
pip3 install paramiko
```

**使用**

paramiko既可以链接服务器执行命令又可以上传下载文件

链接远程服务器的时候有两种方式

* 用户名密码的方式
* 公钥私钥的方式

```python
"""用户名密码的方式执行命令 """
import paramiko


ssh = paramiko.SSHClient()
# 允许链接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 用户名和密码的方式
ssh.connect(hostname='172.16.219.173',port=22,username='root',password='jason123')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ip a')
"""
stdin  允许输入额外的命令  
stdout  正确的执行结果
stderr  错误的结果
"""
# 获取命令的执行结果
res = stdout.read()
print(res.decode('utf-8'))

# 关联链接对象
ssh.close()


"""概要私钥的方式执行命令"""
# 首先你需要生成你自己的公钥私钥 然后将你的公钥拷贝到远程服务器 之后通过自己的私钥即可链接服务器
"""
mac本为例
1 生成
ssh-keygen -t rsa
2 拷贝到远程服务器
ssh-copy-id -i ~/.ssh/id_rsa.pub 用户名@服务器地址
"""
import paramiko

# 读取本地私钥
private_key = paramiko.RSAKey.from_private_key_file('a.txt')

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='172.16.219.173', port=22, username='root', pkey=private_key)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ls /')
# 获取命令结果
result = stdout.read()
print(result.decode('utf-8'))
# 关闭连接
ssh.close()
```

#### 上传下载文件

```python
"""用户名密码的方式"""
import paramiko

# 用户名和密码
transport = paramiko.Transport(('172.16.219.173', 22))
transport.connect(username='root', password='jason123')

sftp = paramiko.SFTPClient.from_transport(transport)

# 上传文件
# sftp.put("a.txt", '/data/b.txt')  # 注意上传文件到远程某个文件下 文件必须存在

# 下载文件
sftp.get('/data/b.txt', 'hahaha.txt')  # 将远程文件下载到本地并重新命令
transport.close()

"""密钥的方式"""
import paramiko
private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')
transport = paramiko.Transport(('hostname', 22))
transport.connect(username='jason', pkey=private_key)
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('/tmp/location.py', '/tmp/test.py')

# 将remove_path 下载到本地 local_path
sftp.get('remove_path', 'local_path')
transport.close()
```

**补充:私钥在内存也可以读取链接**

```python
key = """放私钥"""

import paramiko
from io import StringIO

private_key = paramiko.RSAKey(file_obj=StringIO(key))

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.16.85', port=22, username='root', pkey=private_key)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')
# 获取命令结果
result = stdout.read()

# 关闭连接
ssh.close()

print(result)
```

执行命令和上传下载文件的代码是有所区别的

#### 编程建议:当你在使用一个模块的时候，如果该模块功能挺多的，那么我建议对该模块进行一个功能的封装，将所有的功能封装到一个类中，之后调用该类产生的对象即可执行所有的模块方法

```python
# 对paramiko模块进行封装
import paramiko


class SSHProxy(object):
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.transport = None

    def open(self):  # 给对象赋值一个上传下载文件对象连接
        self.transport = paramiko.Transport((self.hostname, self.port))
        self.transport.connect(username=self.username, password=self.password)

    def command(self, cmd):  # 正常执行命令的连接  至此对象内容就既有执行命令的连接又有上传下载链接
        ssh = paramiko.SSHClient()
        ssh._transport = self.transport

        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        return result

    def upload(self, local_path, remote_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.put(local_path, remote_path)
        sftp.close()

    def close(self):
        self.transport.close()

    def __enter__(self):
        """with语法一旦触发立刻执行"""
        print('呵呵呵')
        return self  # 该方法返回什么 as语法后面就接受到什么

    def __exit__(self, exc_type, exc_val, exc_tb):
        """with代码块执行完毕之后自动触发"""
        print('hahaha')
```

#### 面试题

```python
"""
请在ConText类中添加代码完成该类的实现 不报错
class	ConText:
	pass
	
with ConText() as ctx:
	ctx.do_something()
"""
class	ConText:
	def __enter__(self):
    return self
    
  def __exit__(self,*args,**kwargs):
    """当你不知道函数或者方法都有哪些形参的时候 你就用*args,**kwargs代替"""
    pass
 	
  def do_something(self):
    pass
  
with ConText() as ctx:
	ctx.do_something()
```

## gitpython模块

让你能够通过python代码操作git

**安装**

```python
pip3 install gitpython
```

**基本使用**

```python
# 下载远程仓库的代码
import os
from git.repo import Repo


# 定义一个本地存储远程仓库代码的路径
download_path = os.path.join('jason','NB')
Repo.clone_from('https://github.com/DominicJi/TeachTest.git',
                to_path=download_path,
                branch='master'
                )
```

**更多方法**

```python
# ############## 2. pull最新代码 ##############
# import os
# from git.repo import Repo
#
# local_path = os.path.join('jason', 'NB')
# repo = Repo(local_path)
# repo.git.pull()

# ############## 3. 获取所有分支 ##############
# import os
# from git.repo import Repo
#
# local_path = os.path.join('jason', 'NB')
# repo = Repo(local_path)
#
# branches = repo.remote().refs
# for item in branches:
#     print(item.remote_head)

# ############## 4. 获取所有版本 ##############
# import os
# from git.repo import Repo
#
# local_path = os.path.join('jason', 'NB')
# repo = Repo(local_path)
#
# for tag in repo.tags:
#     print(tag.name)

# ############## 5. 获取所有commit ##############
import os
from git.repo import Repo

local_path = os.path.join('jason', 'NB')
repo = Repo(local_path)

# 将所有提交记录结果格式成json格式字符串 方便后续反序列化操作
commit_log = repo.git.log('--pretty={"commit":"%h","author":"%an","summary":"%s","date":"%cd"}', max_count=50,
                          date='format:%Y-%m-%d %H:%M')
log_list = commit_log.split("\n")
real_log_list = [eval(item) for item in log_list]
print(real_log_list)
"""
[
{'commit': 'de8b592', 'author': 'JiBoYuan', 'summary': '家里写的代码', 'date': '2018-07-04 22:50'}, 
{'commit': '943ed78', 'author': 'JiBoYuan', 'summary': '新加了一个文本文件', 'date': '2018-07-04 21:14'}, 
{'commit': '817e64d', 'author': 'JiBoYuan', 'summary': '加了一句', 'date': '2018-07-04 21:12'}, 
{'commit': '045a9cd', 'author': 'JiBoYuan', 'summary': '初次提交', 'date': '2018-07-04 20:51'}
]

"""
# ############## 6. 切换分支 ##############
# import os
# from git.repo import Repo
#
# local_path = os.path.join('jason', 'NB')
# repo = Repo(local_path)
#
# before = repo.git.branch()
# print(before)
# repo.git.checkout('master')
# after = repo.git.branch()
# print(after)
# repo.git.reset('--hard', '854ead2e82dc73b634cbd5afcf1414f5b30e94a8')

# ############## 7. 打包代码 ##############
# with open(os.path.join('jason', 'NB.tar'), 'wb') as fp:
#     repo.archive(fp)
```

**对gitpython模块进行方法的封装**

```python
import os
from git.repo import Repo
from git.repo.fun import is_git_dir


class GitRepository(object):
    """
    git仓库管理
    """
    def __init__(self, local_path, repo_url, branch='master'):
        self.local_path = local_path
        self.repo_url = repo_url
        self.repo = None
        self.initial(repo_url, branch)

    def initial(self, repo_url, branch):
        """
        初始化git仓库
        :param repo_url:
        :param branch:
        :return:
        """
        if not os.path.exists(self.local_path):
            os.makedirs(self.local_path)

        git_local_path = os.path.join(self.local_path, '.git')
        if not is_git_dir(git_local_path):
            self.repo = Repo.clone_from(repo_url, to_path=self.local_path, branch=branch)
        else:
            self.repo = Repo(self.local_path)

    def pull(self):
        """
        从线上拉最新代码
        :return:
        """
        self.repo.git.pull()

    def branches(self):
        """
        获取所有分支
        :return:
        """
        branches = self.repo.remote().refs
        return [item.remote_head for item in branches if item.remote_head not in ['HEAD', ]]

    def commits(self):
        """
        获取所有提交记录
        :return:
        """
        commit_log = self.repo.git.log('--pretty={"commit":"%h","author":"%an","summary":"%s","date":"%cd"}',
                                       max_count=50,
                                       date='format:%Y-%m-%d %H:%M')
        log_list = commit_log.split("\n")
        return [eval(item) for item in log_list]

    def tags(self):
        """
        获取所有tag
        :return:
        """
        return [tag.name for tag in self.repo.tags]

    def change_to_branch(self, branch):
        """
        切换分值
        :param branch:
        :return:
        """
        self.repo.git.checkout(branch)

    def change_to_commit(self, branch, commit):
        """
        切换commit
        :param branch:
        :param commit:
        :return:
        """
        self.change_to_branch(branch=branch)
        self.repo.git.reset('--hard', commit)

    def change_to_tag(self, tag):
        """
        切换tag
        :param tag:
        :return:
        """
        self.repo.git.checkout(tag)


if __name__ == '__main__':
    local_path = os.path.join('codes', 'luffycity')
    repo = GitRepository(local_path,remote_path)
    branch_list = repo.branches()
    print(branch_list)
    repo.change_to_branch('dev')
    repo.pull()
```

## 代码发布项目概述图

参考群截图

Ps:当服务器过多的时候，全部到平台下载数据，平台服务器压力过大，如何解决？？？

比特流技术:将所有人都变成数据的下载者和数据的上传者



### 项目编写思路

写一张表完成该表所有的操作，再写一张再完成

## 服务器管理

```python
class Server(models.Model):
    """服务器表"""
    hostname = models.CharField(verbose_name='主机名',max_length=32)
```

任何一个项目都是由基本的增删改查组成的，并且占了整个项目的80%以上

我们在开发项目的时候，只需要认认真真的写一个完整的增删改查功能。之后所有其他数据的操作直接CV大法加搬砖完成

**添加功能**

```python
"""
1.当模型表字段特别多的时候 前端页面书写繁琐   渲染标签
2.对用户填入的数据应该做数据的校验					 校验数据
3.实时展示提示信息												展示信息
"""		
```

**modelform组件**

```python
"""它是forms组件的加强版本，比forms组件更加强大，并且大部分的方法跟form组件一样"""
class ServerModelForm(ModelForm):
    class Meta:
        model = models.Server  # 指定待操作的模型表
        fields = '__all__'  # 展示所有字段到前端

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # print(self.fields)  # OrderedDict([('hostname', <django.forms.fields.CharField object at 0x10715e198>)])
        for k,field in self.fields.items():
            # 循环当前模型表中所有的字段对象 都添加一个class=form-control的属性
            field.widget.attrs['class'] = 'form-control'
            
def server_add(request):
    # 1 生成一个空的modelform对象
    form_obj = ServerModelForm()
    if request.method == 'POST':
        form_obj = ServerModelForm(data=request.POST)
        # 3 校验数据是否合法
        if form_obj.is_valid():
            # 4 保存数据
            form_obj.save()
            # 5 跳转到服务器展示页
            """
            redirect括号内即可以写url其实还可以写反向解析的别名，但是如果有无名有名分组的情况
            则需要借助于reverse
            """
            return redirect('server_list')

    # 2 将该对象传递到前端页面
    return render(request,'form.html',locals())
```

django默认的语言环境是英文，其实django内部支持很多国家的语言，你只需要在配置文件中修改即可

```PYTHON
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# 如何查看所有支持的语言环境
from django.conf import global_settings
LANGUAGES = [
    ('af', gettext_noop('Afrikaans')),
    ('ar', gettext_noop('Arabic')),
    ('ast', gettext_noop('Asturian')),
    ('az', gettext_noop('Azerbaijani')),
  ...
]
```

**编辑功能**

```python
def server_edit(request,edit_id):
    # 获取用户想要编辑的对象 展示给用户看
    edit_obj = models.Server.objects.filter(pk=edit_id).first()
    # 其实添加页面和编辑页面是一模一样的 只不过编辑页面需要将当前待编辑的数据展示出来
    form_obj = ServerModelForm(instance=edit_obj)
    # 只要有instance参数 那么modelform在渲染标签的时候就会自动将对象数据渲染出来
    if request.method == 'POST':
        form_obj = ServerModelForm(data=request.POST,instance=edit_obj)
        if form_obj.is_valid():
            form_obj.save()  # 有无instance参数来判断到底是新增数据还是编辑数据
            return redirect('server_list')
    return render(request,'form.html',locals())
```

**删除功能**

数据不能点击立刻删除，应该有一个二次确认的过程

在数据删除成功之后，页面不应该直接刷新，你要考虑分页的情况

这个时候你可以使用DOM操作的方式直接删除对应的标签即可

```html
<script>
        function removeData(ths,sid) {
             var res = confirm('你确定要删除吗?');
             // 判断res的值 决定是否朝后端发送请求
             if (res){
                $.ajax({
                    url:'/server/delete/'+ sid + '/',
                    type:'get',
                    success:function (args) {
                        if (args.status){
                            // 页面实时刷新  考虑分页的情况 用户在哪个页面删除数据 删除之后还应该在哪个页面
                            // 通过DOM操作直接删除对应的html代码
                            $(ths).parent().parent().remove()
                        }
                    }
                })
            }
        }
    </script>
```

## 项目管理

```python
class Project(models.Model):
    """项目表"""
    title = models.CharField(verbose_name='项目名',max_length=32)
    repo = models.CharField(verbose_name='仓库地址',max_length=128)

    env_choices = (
        ('prod','正式'),
        ('test','测试'),
    )
    env = models.CharField(verbose_name='环境',
                           max_length=16,
                           choices=env_choices,
                           default='test'
                           )
```

直接拷贝服务器所有的代码,修改名字即可

#### **代码优化**

* 针对modelform应该单独开设文件存储

* 将modelform类中相同的代码抽取出来做成基类

  ```python
  """
  什么是类
  	类是对象公共的属性与技能的结合体
  什么是父类
  	父类是类公共的属性和技能的结合体
  """
  from django.forms import ModelForm
  
  
  class BaseModelForm(ModelForm):
      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          # print(self.fields)  # OrderedDict([('hostname', <django.forms.fields.CharField object at 0x10715e198>)])
          for k, field in self.fields.items():
              # 循环当前模型表中所有的字段对象 都添加一个class=form-control的属性
              field.widget.attrs['class'] = 'form-control'
              
              
  from app01.myforms.base import BaseModelForm
  from app01 import models
  
  
  class ServerModelForm(BaseModelForm):
      class Meta:
          model = models.Server  # 指定待操作的模型表
          fields = '__all__'  # 展示所有字段到前端
  ```

* 给modelform自定义一个是否需要添加bootstrap样式类的配置

  ```python
  class BaseModelForm(ModelForm):
      exclude_bootstrap = []
  
      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          # print(self.fields)  # OrderedDict([('hostname', <django.forms.fields.CharField object at 0x10715e198>)])
          for k, field in self.fields.items():
              if k in self.exclude_bootstrap:
                  continue
              # 循环当前模型表中所有的字段对象 都添加一个class=form-control的属性
              field.widget.attrs['class'] = 'form-control'
  ```

* 给项目表新增两个字段

  ```python
      path = models.CharField(verbose_name='线上项目地址',max_length=128)
      """
      一个项目可不可以跑在多个服务器上？？？？      可以的
      一台服务器是否可以跑多个项目呢？？？         可以的   混用
      """
      servers = models.ManyToManyField(verbose_name='关联服务器',to='Server')
  ```



# 作业布置

一定要自己动手给我把服务器和项目的增删改查操作写出来！！！









































