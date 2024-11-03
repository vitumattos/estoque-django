from django import forms
from .models import Produto, Fornecedor


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'fornecedor', 'estoque_minimo',
                  'preco_custo', 'preco_venda', 'imagem', 'ativo', 'observacao']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do Produto'}),
            'estoque_minimo': forms.NumberInput(attrs={'placeholder': '5'}),
            'preco_custo': forms.NumberInput(attrs={'placeholder': 'R$20.00'}),
            'preco_venda': forms.NumberInput(attrs={'placeholder': 'R$40.00'}),
            'ativo': forms.Select(choices=[(True, 'Sim'), (False, 'Não')]),
            'observacao': forms.Textarea(attrs={'placeholder': 'Observações adicionais...', 'style': 'height:100px'}),
        }


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj', 'email', 'telefone', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'cnpj': forms.TextInput(attrs={'placeholder': '00.000.000/0000-00'}),
            'email': forms.EmailInput(attrs={'placeholder': 'empresa@email.com'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(21) 9 9999 9999'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Rua enderço n°xx, Bairro, Cidade, ES'}),
        }
