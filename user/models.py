from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from formacao.models import Formacao
from experiencia.models import Experiencia
# Create your models here.
class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, null=False)
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
        return self.user.username
    
class Sobre(models.Model):
    descricao = models.TextField(max_length=2600)
    def __str__(self):
        return self.user.username
   