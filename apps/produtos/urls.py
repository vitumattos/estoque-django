from django.urls import path

from .views import CategoriaCreate, FornecedorCreate, ProdutoCreate
from .views import CategoriaUpdate, FornecedorUpdate, ProdutoUpdate
from .views import CategoriaDelete, FornecedorDelete, ProdutoDelete
from .views import CategoriaList, FornecedorList, ProdutoList


urlpatterns = [
    # ======= CREATE ======= #
    path('cadastrar/categoria', CategoriaCreate.as_view(), name='cadastrar-categoria'),
    path('cadastrar/fornecedor', FornecedorCreate.as_view(), name='cadastrar-fornecedor'),
    path('cadastrar/produto', ProdutoCreate.as_view(), name='cadastrar-produto'),

    # ======= UPDATE ======= #
    path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name='editar-categoria'),
    path('editar/fornecedor/<int:pk>/', FornecedorUpdate.as_view(), name='editar-fornecedor'),
    path('editar/produto/<int:pk>/', ProdutoUpdate.as_view(), name='editar-produto'),

    # ======= DELETE ======= #
    path('excluir/categoria/<int:pk>/', CategoriaDelete.as_view(), name='excluir-categoria'),
    path('excluir/fornecedor/<int:pk>/', FornecedorDelete.as_view(), name='excluir-fornecedor'),
    path('excluir/produto/<int:pk>/', ProdutoDelete.as_view(), name='excluir-produto'),

    # ======= LIST ======= #
    path('listar/categoria', CategoriaList.as_view(), name='listar-categoria'),
    path('listar/fornecedor', FornecedorList.as_view(), name='listar-fornecedor'),
    path('listar/produto', ProdutoList.as_view(), name='listar-produto'),
]
