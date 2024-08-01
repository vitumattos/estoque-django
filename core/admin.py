from django.contrib import admin
from .models import Categoria, Fornecedor, Produto, Estoque, EntradaSaidaEstoque

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Fornecedor)
admin.site.register(EntradaSaidaEstoque)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'categoria',
        'estoque_minimo',
        'descricao',
        'fornecedor',
        'preco_custo',
        'preco_venda',
        'imagem',
        'ativo',
    )
    search_fields = ('produto',)
    list_filter = ('categoria', 'fornecedor', 'ativo')


@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'data_atualizacao',
    )
