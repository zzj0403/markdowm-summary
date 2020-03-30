from django.db import models


#  project + path
# Create your models here.
class log_info(models.Model):
    project = models.CharField(max_length=32, verbose_name='项目名称')
    log_path = models.CharField(max_length=255, verbose_name='日志地址')
    host = models.ForeignKey(to='host')


# hostname + ip + login——mode
class host(models.Model):
    hostname = models.CharField(max_length=32, verbose_name='主机名')
    ip = models.CharField(max_length=64, verbose_name='ip地址')
    password = models.CharField(max_length=255, verbose_name='密码',default=None)
    Private_key = models.FileField(upload_to='key/', default=None)
    Private_password = models.TextField(default=None, verbose_name='密钥密码')
