from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Experiencia(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField( max_length=60, null=False)
    tipo_de_emprego = models.CharField( max_length=60)
    nome_da_empresa = models.CharField( max_length=60)
    exibir_que_linkedin_ajudou = models.BooleanField()
    localidade = models.CharField( max_length=60)
    trabalho_atualmente_neste_cargo = models.BooleanField()
    mes_inicio = models.CharField(max_length=50, null=False)
    ano_inicio = models.CharField(max_length=50, null=False)
    mes_fim = models.CharField(max_length=50)
    ano_fim = models.CharField(max_length=50)
    finalizar_cargo = models.BooleanField()
    setor = models.CharField(max_length=100, null=False)
    descricao = models.TextField(max_length=2000)
    titulo_do_perfil = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.username.username
    