from django.shortcuts import render, HttpResponse
from command_log import models
from django.http import JsonResponse
import json


# Create your views here.


def log_info(request):
    project_list = models.project_info.objects.all()
    if request.method == 'POST':
        # pass
        print(request.POST.get('project'))
        print(request.POST.get('host'))

    return render(request, 'log_info.html', locals())


def host_list(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id', None)
        # print(project_id)
        if project_id:
            host_obj = list(models.host_info.objects.filter(project_id__host_info=project_id))
            result = []
            for i in host_obj:
                # 对应的id和城市名称组成一个字典
                result.append({'id': i.id, 'name': i.hostname})
            return JsonResponse(result)


# return render(request, 'log_info.html', locals())


def add_host(request):
    return render(request, 'add_host.html', locals())


def base(request):
    return render(request, 'base.html', locals())


def test(request):
    if request.method == "POST":
        print(request.POST.get('id'))
        back_dic = {'code': 2000, 'msg': ''}
        res = json.dumps(back_dic)
        return HttpResponse(res)
    return render(request, 'test.html')
