from django.test import TestCase

# Create your tests here.
import os
import sys
import json
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yiyun.settings")
    import django

    django.setup()
    from command_log import models

    project_list = models.project_info.objects.all()
    host_project = models.host_info.objects.filter(project_id=1)
    result = []
    for h in host_project:
        host_dic = {}
        host_dic['id'] = h.pk
        host_dic['hostname'] = h.hostname
        result.append(host_dic)
    print(result)