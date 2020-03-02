from django.test import TestCase

# Create your tests here.
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ORMDemo.settings")
    import django

    django.setup()
    from app01 import models
    res = models.Book1.objects.all()
    print(res)