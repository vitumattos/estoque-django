from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome da empresa')
    cnpj = models.CharField(max_length=18, unique=True, verbose_name='CNPJ')
    email = models.CharField(max_length=100, unique=True)
    telefone = models.CharField(max_length=16)
    endereco = models.CharField(max_length=255, verbose_name="endereço")

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=255, unique=True, verbose_name='Nome do Produto')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    estoque_minimo = models.PositiveSmallIntegerField(verbose_name="Estoque mínimo")
    preco_custo = models.FloatField(verbose_name="Preço de custo")
    preco_venda = models.FloatField(verbose_name="Preço de venda")
    imagem = models.FileField(upload_to='produtos_img/', blank=True, null=True, verbose_name='Imagem do Produto')
    ativo = models.BooleanField(default=True)
    observacao = models.TextField(verbose_name="observação", blank=True, null=True,)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome


