from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.shortcuts import render
from .models import EntradaSaidaEstoque
from django.db.models import Sum, F, Case, When, Max, Count

from django.urls import reverse_lazy


# Create your views here.
class EntradaSaidaCreate(CreateView, ListView):
    model = EntradaSaidaEstoque
    fields = ['quantidade', 'produto', 'ordem']
    template_name = 'estoque/form.html'
    success_url = reverse_lazy('cadastrar-EntradaSaida')


class EntradaSaidaUpdate(UpdateView):
    model = EntradaSaidaEstoque
    fields = ['quantidade', 'produto', 'ordem']
    template_name = 'estoque/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "**UPDATE**"
        return context


class EntradaSaidaDelete(DeleteView):
    model = EntradaSaidaEstoque
    template_name = 'estoque/form-excluir.html'
    success_url = reverse_lazy('cadastrar-EntradaSaida')


class Estoque(ListView):
    model = EntradaSaidaEstoque
    template_name = 'estoque/estoque.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        estoque_dict = {}
        for i in EntradaSaidaEstoque.objects.filter(ordem='Entrada'):
            if i.produto not in estoque_dict:
                estoque_dict[i.produto] = i.quantidade
            else:
                estoque_dict[i.produto] += i.quantidade

        for i in EntradaSaidaEstoque.objects.filter(ordem='Saida'):
            if i.produto not in estoque_dict:
                break
            else:
                estoque_dict[i.produto] -= i.quantidade

        context['estoque_dict'] = estoque_dict
        context['estoque_quantidade'] = estoque_dict.values()
        context['estoque_produtos'] = estoque_dict.keys()
        return context


def Relatorio(request):
    # Todods os Lançamentos
    all_object = EntradaSaidaEstoque.objects.all()

    # Estoque Atual
    estoque_qs = (
        EntradaSaidaEstoque.objects
        .values('produto__nome', 'produto__preco_venda', 'produto__preco_custo', 'produto__estoque_minimo')
        .annotate(
            quantidade=Sum(
                Case(
                    When(ordem='Entrada', then=F('quantidade')),
                    When(ordem='Saida', then=-F('quantidade')),
                    default=0,
                )
            ),
            total_estimado=F('produto__preco_venda')*F('quantidade'),
            total_gasto=F('produto__preco_custo')*F('quantidade'),
        )
        .filter(quantidade__gt=0)
    )
    # Valor TOTAL estoque atual
    estoque_sum = estoque_qs.aggregate(estimado_total=Sum('total_estimado'), gasto_total=Sum('total_gasto'))

    # Produtos com baixo estoque
    alert_estoque_min = estoque_qs.filter(quantidade__lt=F('produto__estoque_minimo'))

    # Produto mais vendido
    produtos_vendidos = (
        EntradaSaidaEstoque.objects
        .filter(ordem='Saida')
        .values('produto__nome')
        .annotate(total_vendido=Sum('quantidade'))
        .order_by('-total_vendido')
    )

    # Obter o produto mais vendido, se existir
    produto_mais_vendido = produtos_vendidos.first() if produtos_vendidos else None

    return render(
        request,
        "estoque/relatorio.html",
        {
            "all_object": all_object,
            "estoque_qs": estoque_qs,
            "estoque_sum": estoque_sum,
            "alert_estoque_min": alert_estoque_min,
            'produto_mais_vendido': produto_mais_vendido,
        }
    )
