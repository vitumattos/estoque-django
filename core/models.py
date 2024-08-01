from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    telefone = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=255, verbose_name="Endereço")

    def __str__(self) -> str:
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    estoque_minimo = models.PositiveSmallIntegerField(verbose_name="Estoque mínimo", default=0)
    descricao = models.TextField(verbose_name="Descrição")
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    preco_custo = models.FloatField(verbose_name="Preço de custo")
    preco_venda = models.FloatField(verbose_name="Preço de venda")
    imagem = models.CharField(max_length=255, null=True, blank=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ("nome",)

    def __str__(self) -> str:
        return self.nome


class EntradaSaidaEstoque(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    quantidade = models.SmallIntegerField()
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    nota_fiscal = models.CharField(max_length=255, verbose_name="Nota Fiscal", null=True, blank=True)
    cliente = models.CharField(max_length=255, null=True, blank=True)
    ordem = models.CharField(max_length=4, choices={
        'SELL': 'SELL',
        'BUY': 'BUY',
    })
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ("-data",)

    def save(self, *args, **kwargs):
        self.atualiza_estoque()
        super().save(*args, **kwargs)

    def atualiza_estoque(self):
        produto = self.produto

        if self.ordem == 'BUY':
            nova_quantidade = produto.estoque.quantidade + self.quantidade
        else:
            nova_quantidade = produto.estoque.quantidade - self.quantidade

        # Atualiza o estoque do produto
        produto.estoque.quantidade = max(nova_quantidade, 0)  # Evita quantidades negativas
        produto.estoque.save()

    def __str__(self) -> str:
        return "{} - {} {} | {}".format(self.ordem, self.quantidade, self.produto, self.data.strftime("%d/%m/%Y %I:%M%p"))


class Estoque(models.Model):
    data_atualizacao = models.DateTimeField(verbose_name="Data Atualização", auto_now=True)
    produto = models.OneToOneField(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField(default=0)

    class Meta:
        ordering = ("-data_atualizacao",)

    def __str__(self) -> str:
        return "{} {}".format(self.quantidade, self.produto)


# Sinal para criar um novo registro de estoque quando um produto é criado
@receiver(post_save, sender=Produto)
def criar_estoque(sender, instance, created, **kwargs):
    if created:
        Estoque.objects.create(produto=instance)
