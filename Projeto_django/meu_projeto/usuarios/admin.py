from django.contrib import admin
from .models import Professor,datashow
from django.contrib.admin import ModelAdmin, register

@register(Professor)
class professor(ModelAdmin): 
    icon_name = 'user'

@register(datashow)
class datashow(ModelAdmin): 
    extra = 1
    