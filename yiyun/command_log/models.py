from django.db import models


#  project + path
# Create your models here.
class project_info(models.Model):
    project = models.CharField(max_length=32, verbose_name='项目名称')
    log_path = models.CharField(max_length=255, verbose_name='日志地址')
    def __str__(self):
        return self.project


# hostname + ip + login——mode
class host_info(models.Model):
    hostname = models.CharField(max_length=32, verbose_name='主机名')
    ip = models.CharField(max_length=64, verbose_name='ip地址')
    password = models.CharField(max_length=255, verbose_name='密码', null=True)
    Private_key = models.FileField(upload_to='key/', null=True)
    Private_password = models.TextField(default=None, verbose_name='密钥密码', null=True)
    project_id = models.ForeignKey(to='project_info', null=True)

    def __str__(self):
        return self.hostname
