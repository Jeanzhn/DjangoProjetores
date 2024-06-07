from django.contrib import admin
from .models import professor, aluguel,quantidadeprofessor
from django.contrib.admin import ModelAdmin, TabularInline, register


class quantidadeprofessorInLine(TabularInline):
    model = quantidadeprofessor
    extra = 1
    readonly_fields = ['insert_in']

@register(professor)
class VacinometroAdmin(ModelAdmin): # type: ignore
    icon_name = 'user'



@register(aluguel)
class VacinometroAdmin(ModelAdmin): # type: ignore
    extra = 1
    inlines = [quantidadeprofessorInLine]