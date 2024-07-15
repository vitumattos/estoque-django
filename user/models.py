from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Perfil(models.Model):
    nome_completo = models.CharField(max_length=100, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
