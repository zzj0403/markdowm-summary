from django.shortcuts import render, HttpResponse
from command_log import models
from django.http import JsonResponse
import json


# Create your views here.

def host_list(request):
    project_list = models.project_info.objects.all()
    if request.method == 'POST':
        project_id = request.POST.get('project_id', None)
        # print(project_id)
        if project_id:
            host_obj = models.host_info.objects.filter(project_id=project_id)
            result = []
            for h in host_obj:
                host_dic = {}
                host_dic['id'] = h.pk
                host_dic['hostname'] = h.hostname
                result.append(host_dic)
            result = json.dumps(result)
            print(result)
            return HttpResponse(result, "application/json")
    return render(request, 'log_info.html', locals())


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
