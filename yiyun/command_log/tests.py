from django.test import TestCase

# Create your tests here.
import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zm6_day02.settings")
    import django
    from command_log import models
    django.setup()
    host_list = models.host.objects.get('hostname')
    project_lsit = models.host.objects.get('project')
    print(host_list)
    print(project_lsit)