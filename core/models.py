from django.db import models
from django.contrib.auth.models import User


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
    imagem = models.CharField(max_length=255, unique=True, null=True, blank=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ("nome",)

    def __str__(self) -> str:
        return self.nome


class EntradaEstoque(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.SmallIntegerField()
    nota_fiscal = models.CharField(max_length=255, verbose_name="Nota Fiscal", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ("-data",)

    def __str__(self) -> str:
        return "{} {} | {}".format(self.quantidade, self.produto, self.data.strftime("%d/%m/%Y %I:%M%p"))


class SaidaEstoque(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.SmallIntegerField()
    cliente = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ("-data",)

    def __str__(self) -> str:
        return "{} {} | {}".format(self.quantidade, self.produto, self.data.strftime("%d/%m/%Y %I:%M%p"))


class Estoque(models.Model):
    data_atualizacao = models.DateTimeField(verbose_name="Data Atualização", auto_now=True)
    produto = models.OneToOneField(Produto, on_delete=models.PROTECT)

    @property
    def quantidade(self):
        entrada = EntradaEstoque.objects.filter(produto=self.produto).aggregate(
            total=models.Sum('quantidade'))['total'] or 0
        saida = SaidaEstoque.objects.filter(produto=self.produto).aggregate(
            total=models.Sum('quantidade'))['total'] or 0
        return entrada - saida

    class Meta:
        ordering = ("-data_atualizacao",)

    def __str__(self) -> str:
        return "{} {}".format(self.quantidade, self.produto)
