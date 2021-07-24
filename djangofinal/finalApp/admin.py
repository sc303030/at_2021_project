from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(TestUser)


@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    pass