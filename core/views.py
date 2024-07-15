from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Categoria, Fornecedor, Produto, Estoque, EntradaEstoque, SaidaEstoque

from django.urls import reverse_lazy


# Create your views here.
class IndexView(TemplateView):
    template_name = 'core/index.html'


# ========== CREATE ========== #
class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'forms/form-create.html'
    success_url = reverse_lazy('index')


class FornecedorCreate(CreateView):
    model = Fornecedor
    fields = ['nome', 'cnpj', 'email', 'telefone', 'endereco']
    template_name = 'forms/form-create.html'
    success_url = reverse_lazy('index')


class ProdutoCreate(CreateView):
    model = Produto
    fields = ['nome', 'categoria', 'estoque_minimo', 'descricao',
              'fornecedor', 'preco_custo', 'preco_venda', 'imagem', 'ativo']
    template_name = 'forms/form-create.html'
    success_url = reverse_lazy('index')


class EntradaEstoqueCreate(CreateView):
    model = EntradaEstoque
    fields = ['produto', 'quantidade', 'nota_fiscal']
    template_name = 'forms/form-create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        return url


class SaidaEstoqueCreate(CreateView):
    model = SaidaEstoque
    fields = ['produto', 'quantidade', 'cliente']
    template_name = 'forms/form-create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        return url


# ========== LIST ========== #
class ProdutoList(ListView):
    model = Produto
    template_name = 'forms/listas/produto.html'


class EstoqueList(ListView):
    model = Estoque
    template_name = 'forms/listas/estoque.html'


class MovimentacaoList(ListView):
    model = SaidaEstoque
    template_name = 'forms/listas/movimentacao.html'


# ========== UPDATE ========== #
class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['nome']
    template_name = 'forms/form-update.html'
    success_url = reverse_lazy('index')


class FornecedorUpdate(UpdateView):
    model = Fornecedor
    fields = ['nome', 'cnpj', 'email', 'telefone', 'endereco']
    template_name = 'forms/form-update.html'
    success_url = reverse_lazy('index')


class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ['nome', 'categoria', 'estoque_minimo', 'descricao',
              'fornecedor', 'preco_custo', 'preco_venda', 'imagem', 'ativo']
    template_name = 'forms/form-update.html'
    success_url = reverse_lazy('index')


# ========== DELETE ========== #
class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'forms/form-delete.html'
    success_url = reverse_lazy('index')


class FornecedorDelete(DeleteView):
    model = Fornecedor
    template_name = 'forms/form-delete.html'
    success_url = reverse_lazy('index')


class ProdutoDelete(DeleteView):
    model = Produto
    template_name = 'forms/form-delete.html'
    success_url = reverse_lazy('index')


class EntradaEstoqueDelete(DeleteView):
    model = EntradaEstoque
    template_name = 'forms/form-delete.html'
    success_url = reverse_lazy('index')


class SaidaEstoqueDelete(DeleteView):
    model = SaidaEstoque
    template_name = 'forms/form-delete.html'
    success_url = reverse_lazy('index')
