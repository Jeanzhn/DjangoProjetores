from django.db import models
from django.utils.translation import gettext as _t, gettext_lazy as _

class Professor(models.Model):
    user_id = models.AutoField(primary_key=True, verbose_name= 'user.id')
    nome = models.CharField('nome-professor',max_length=100, default='nome padrao')
    materia = models.CharField('materia-professor', max_length=100, default='Materia Padrao')
    sala = models.CharField('sala', max_length=3)
    def __str__(self):
        return f"{self.user_id} - {self.nome} - {self.materia} - {self.sala}"
    
    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"    

class datashow(models.Model):
    marca = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    reservado = models.BooleanField(default=False)
    Professor = models.ForeignKey(Professor, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"{self.marca} - {self.quantidade} - {self.reservado} - {self.Professor}"
    