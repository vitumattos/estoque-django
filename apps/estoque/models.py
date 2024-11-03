from django.db import models
from ..produtos.models import Produto

# Create your models here.


class EntradaSaidaEstoque(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    quantidade = models.SmallIntegerField()
    produto = models.ForeignKey(Produto,
                                on_delete=models.CASCADE,
                                limit_choices_to={'ativo': True})
    ordem = models.CharField(max_length=7, choices={
        'Entrada': 'Entrada',
        'Saida': 'Saida'
    })

    class Meta:
        ordering = ("-data",)

    def __str__(self) -> str:
        return "{} de {} {} | {}".format(self.ordem, self.quantidade, self.produto, self.data.strftime("%d/%m/%Y %I:%M%p"))
