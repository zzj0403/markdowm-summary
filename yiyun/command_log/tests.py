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
    host_project = models.host_info.objects.filter(project_id__host_info=1)
    print(host_project)
    result = {}
    for i in host_project:
        # 对应的id和城市名称组成一个字典
        result[i.hostname] = i.hostname
    res = json.dumps(result)
    print(res)
