from django.shortcuts import render
from command_log import models


# Create your views here.


def log_info(request):
    host_list = models.host.objects.get('hostname')
    project_lsit = models.host.objects.get('project')
    return render(request, 'log_info.html', locals())


def base(request):
    return render(request, 'base.html', locals())
