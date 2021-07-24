import json

from django.db import models

# Create your models here.

class TestModel(models.Model):
    test_list = models.TextField(blank=False)