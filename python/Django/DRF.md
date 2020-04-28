# DRF框架

> - 全称 django-rest framwework

<<<<<<< HEAD
1. 接口
2. CBV生命周期源码。
3. 请求组件，解析组件，响应组件
4. 序列化组件
5. 认证、权限、频率
6. 其他组件：过滤、筛选、排序、路由
7. 源码分析

- 安装

```bash
pip install djangorestframework
```

- 简单使用

```python
urls.py
urlpatterns = [
    url(r'^test/$', views.Test.as_view()),
]
views.py
class Test(APIView):
    def get(self, request, *args, **kwargs):
        return Response('drf_get_ok')
```

## 访问的生命周期

1. 请求走的是APIView的as_view方法。

   - 请求走的是APIView的as_view方法。

     ```python
     class Test(APIView):
             def get(self, request, *args, **kwargs):
             return Response('drf_get_ok')
     ```

   - 进入APIView的as_view调用父类的as_view

     ```python
     view = super().as_view(**initkwargs)
     return csrf_exempt(view)
     # 调用父类as_view返回的view 并禁用csrf
     ```

   - 父类as_view，方法走的有是APIView的dispatch

     ```python
     return self.dispatch(request, *args, **kwargs)
     #self对象是Test，查找方法的路径是：实例->类->父类。test是APIView对象，去rest_framework找dispatch
     ```

   - 完成dispatch任务返回处理结果.

     ```python
     request = self.initialize_request(request, *args, **kwargs)
     # initialize_request 方法处理request请求 放回结果
     ```
=======
1. 序列化
2. 请求和响应
3. 基于类的视图
4. 认证和权限
5. 关联和超链接的apis
6. 视图集和路由
7. 概要和客户端库

![DRF_http_request](../../img/DRF_http_request.png)
>>>>>>> 5f3b0882232b1cbff954c5607722a37bf941bbe1

