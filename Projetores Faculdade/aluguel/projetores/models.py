from django.db import models
from django.contrib.auth.models import User # type: ignore
from django.utils.translation import gettext as _t, gettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError

def validate_future_date(value):
    if value.year < 2024:
        raise ValidationError('A data não pode ser no passado.')

# Create your models here.
class professor(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField("Nome",max_length=150)
    matery = models.CharField("Matéria",max_length=150)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"

class aluguel (models.Model):
    info = models.CharField("dados do dia",max_length=150)
    date = models.DateField("Data", null=True, blank=True, validators=[validate_future_date])

    def __str__(self):
        return self.info
    
    class Meta:
        verbose_name = "Aluguel"
        verbose_name_plural = "Alugueis"


class quantidadeprofessor (models.Model):
    data_id = models.ForeignKey(aluguel, on_delete=models.CASCADE, verbose_name="aluguel")
    professor = models.ForeignKey(professor, on_delete=models.CASCADE, verbose_name="professor")
    room = models.CharField("sala",max_length=150)
    matery = models.CharField("matéria",max_length=150)
    insert_in = models.DateTimeField(_("Inserido em"), default=timezone.now)
    


    def __date__(self):
        return self.data_id
    
    class Meta:
        verbose_name = "lista profesor"
        verbose_name_plural = "lista professores"

