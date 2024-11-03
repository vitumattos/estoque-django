from django.contrib import admin
from .models import Categoria, Fornecedor, Produto

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Fornecedor)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'categoria',
        'fornecedor',
        'estoque_minimo',
        'preco_custo',
        'preco_venda',
        'imagem',
        'ativo',
        'observacao',
    )
    search_fields = ('produto',)
    list_filter = ('categoria', 'fornecedor', 'ativo')
