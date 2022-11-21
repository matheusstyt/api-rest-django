from django.db import models
from formacao.models import Formacao
from experiencia.models import Experiencia
# Create your models here.
class User(models.Model):
    usuario = models.CharField(max_length=50, null=False)
    nome = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50)

    sobrenome = models.CharField(max_length=50, null=False)
    nomesocial = models.CharField(max_length=50, null=True)
    bio = models.TextField()
    titulo = models.CharField(max_length=150, null=False)
    local = models.CharField(max_length=50 , null=False)
    pais = models.CharField(max_length=50 , null=False)
    cidade = models.CharField(max_length=50 , null=False)
    formacao = models.ManyToManyField(Formacao)
    experiencia = models.ManyToManyField(Experiencia)
    setor = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50, null=True)
    exibir_a_empresa_atual_na_minha_introdução = models.BooleanField()
    exibir_formação_na_minha_introdução = models.BooleanField()
    def __str__(self):
        return self.usuario
    
class Sobre(models.Model):
    descricao = models.TextField(max_length=2600)
    def __str__(self):
        return self.descricao
   