from django.views.generic import TemplateView  # Usado para renderizar um html pronto
from django.views.generic.edit import CreateView  # Usado para criar formulario
from django.views.generic.edit import UpdateView  # Usado para alterar formulario
from django.views.generic.edit import DeleteView  # Usado para deletar formulario
from django.views.generic.list import ListView  # Listar
from .models import Categoria, Fornecedor, Produto
from django.urls import reverse_lazy
from .forms import ProdutoForm, FornecedorForm


# ======= CREATE ======= #
class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'produtos/cadastro/form-cadastro-categoria.html'
    success_url = reverse_lazy('listar-categoria')


class FornecedorCreate(CreateView):
    form_class = FornecedorForm
    template_name = 'produtos/cadastro/form-cadastro-fornecedor.html'
    success_url = reverse_lazy('listar-fornecedor')


class ProdutoCreate(CreateView):
    form_class = ProdutoForm
    template_name = 'produtos/cadastro/form-cadastro-produto.html'
    success_url = reverse_lazy('listar-produto')


# ======= UPDATE ======= #
class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['nome', ]
    template_name = 'produtos/cadastro/form-cadastro-categoria.html'
    success_url = reverse_lazy('listar-categoria')


class FornecedorUpdate(UpdateView):
    model = Fornecedor
    fields = ['nome', 'cnpj', 'email', 'telefone', 'endereco']
    template_name = 'produtos/cadastro/form-cadastro-fornecedor.html'
    success_url = reverse_lazy('listar-fornecedor')


class ProdutoUpdate(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/form-update-produto.html'
    success_url = reverse_lazy('listar-produto')


# ======= DELETE ======= #
class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'produtos/form-excluir.html'
    success_url = reverse_lazy('listar-categoria')


class FornecedorDelete(DeleteView):
    model = Fornecedor
    template_name = 'produtos/form-excluir.html'
    success_url = reverse_lazy('listar-fornecedor')


class ProdutoDelete(DeleteView):
    model = Produto
    template_name = 'produtos/form-excluir.html'
    success_url = reverse_lazy('listar-produto')


# ======= LIST ======= #
class CategoriaList(ListView):
    model = Categoria
    template_name = 'produtos/listar/categoria.html'


class FornecedorList(ListView):
    model = Fornecedor
    template_name = 'produtos/listar/fornecedor.html'


class ProdutoList(ListView):
    model = Produto
    template_name = 'produtos/listar/produto.html'
