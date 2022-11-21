from django.db import models

# Create your models here.
class Formacao(models.Model):
    instituicao_ensino = models.CharField(max_length=70)
    diploma = models.CharField(max_length=70)
    area_estudo = models.CharField(max_length=70)
    mes_inicio = models.CharField(max_length=70)
    ano_inicio = models.CharField(max_length=70)
    mes_fim = models.CharField(max_length=70)
    ano_fim =  models.CharField(max_length=70)
    nota =  models.CharField(max_length=70)
    atividades = models.TextField(max_length=500)
    descricao = models.TextField(max_length=1000)
    def __str__(self):
        return self.instituicao_ensino
    



