from django.urls import path
from .views import IndexView
from .views import CategoriaCreate, FornecedorCreate, ProdutoCreate, EntradaEstoqueCreate, SaidaEstoqueCreate
from .views import ProdutoList, EstoqueList, MovimentacaoList
from .views import CategoriaUpdate, FornecedorUpdate, ProdutoUpdate
from .views import CategoriaDelete, FornecedorDelete, ProdutoDelete, EntradaEstoqueDelete, SaidaEstoqueDelete

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('cadastrar/categoria/', CategoriaCreate.as_view(), name='cadastrar-categoria'),
    path('cadastrar/fornecedor/', FornecedorCreate.as_view(), name='cadastrar-fornecedor'),
    path('cadastrar/produto/', ProdutoCreate.as_view(), name='cadastrar-produto'),
    path('cadastrar/entrada-estoque/', EntradaEstoqueCreate.as_view(), name='cadastrar-entrada-estoque'),
    path('cadastrar/saida-estoque/', SaidaEstoqueCreate.as_view(), name='cadastrar-saida-estoque'),

    path('listar/produto/', ProdutoList.as_view(), name='listar-produto'),
    path('listar/estoque/', EstoqueList.as_view(), name='listar-estoque'),
    path('listar/movimentacao/', MovimentacaoList.as_view(), name='listar-movimentacao'),

    path('editar/categoria/<int:pk>', CategoriaUpdate.as_view(), name='editar-categoria'),
    path('editar/fornecedor/<int:pk>', FornecedorUpdate.as_view(), name='editar-fornecedor'),
    path('editar/produto/<int:pk>', ProdutoUpdate.as_view(), name='cadastrar-produto'),

    path('deletar/categoria/<int:pk>', CategoriaDelete.as_view(), name='deletar-categoria'),
    path('deletar/fornecedor/<int:pk>', FornecedorDelete.as_view(), name='deletar-fornecedor'),
    path('deletar/produto/<int:pk>', ProdutoDelete.as_view(), name='deletar-produto'),
    path('deletar/entrada-estoque/<int:pk>', EntradaEstoqueDelete.as_view(), name='deletar-entrada-estoque'),
    path('deletar/saida-estoque/<int:pk>', SaidaEstoqueDelete.as_view(), name='deletar-saida-estoque'),

]
