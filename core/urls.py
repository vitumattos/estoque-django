from django.urls import path
from .views import IndexView
from .views import CategoriaCreate, FornecedorCreate, ProdutoCreate, EntradaSaidaEstoqueCreate
from .views import ProdutoList, EstoqueList, EntradaSaidaEstoqueList
from .views import CategoriaUpdate, FornecedorUpdate, ProdutoUpdate, EntradaSaidaEstoqueUpdate
from .views import CategoriaDelete, FornecedorDelete, ProdutoDelete, EntradaSaidaEstoqueDelete
from .views import EntradaEstoqueCreate, SaidaEstoqueCreate

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('cadastrar/categoria/', CategoriaCreate.as_view(), name='cadastrar-categoria'),
    path('cadastrar/fornecedor/', FornecedorCreate.as_view(), name='cadastrar-fornecedor'),
    path('cadastrar/produto/', ProdutoCreate.as_view(), name='cadastrar-produto'),
    path('cadastrar/entrada-saida-estoque/', EntradaSaidaEstoqueCreate.as_view(), name='cadastrar-entrada-saida-estoque'),
    path('cadastrar/entrada-estoque/', EntradaEstoqueCreate.as_view(), name='cadastrar-entrada-estoque'),
    path('cadastrar/saida-estoque/', SaidaEstoqueCreate.as_view(), name='cadastrar-saida-estoque'),

    path('listar/produto/', ProdutoList.as_view(), name='listar-produto'),
    path('listar/estoque/', EstoqueList.as_view(), name='listar-estoque'),
    path('listar/entrada-saida-estoque/', EntradaSaidaEstoqueList.as_view(), name='listar-entrada-saida-estoque'),

    path('editar/categoria/<int:pk>', CategoriaUpdate.as_view(), name='editar-categoria'),
    path('editar/fornecedor/<int:pk>', FornecedorUpdate.as_view(), name='editar-fornecedor'),
    path('editar/produto/<int:pk>', ProdutoUpdate.as_view(), name='editar-produto'),
    path('editar/entrada-saida-estoque/<int:pk>', EntradaSaidaEstoqueUpdate.as_view(), name='editar-entrada-saida-estoque'),

    path('deletar/categoria/<int:pk>', CategoriaDelete.as_view(), name='deletar-categoria'),
    path('deletar/fornecedor/<int:pk>', FornecedorDelete.as_view(), name='deletar-fornecedor'),
    path('deletar/produto/<int:pk>', ProdutoDelete.as_view(), name='deletar-produto'),
    path('deletar/entrada-saida-estoque/<int:pk>', EntradaSaidaEstoqueDelete.as_view(), name='deletar-entrada-saida-estoque'),

]
