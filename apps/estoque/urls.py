from django.urls import path
from .views import EntradaSaidaCreate, EntradaSaidaUpdate, EntradaSaidaDelete, Estoque, Relatorio


urlpatterns = [
    path('cadastrar/EntradaSaida', view=EntradaSaidaCreate.as_view(), name='cadastrar-EntradaSaida'),
    path('editar/EntradaSaida/<int:pk>', view=EntradaSaidaUpdate.as_view(), name='editar-EntradaSaida'),
    path('excluir/EntradaSaida/<int:pk>', view=EntradaSaidaDelete.as_view(), name='excluir-EntradaSaida'),
    path('estoque', view=Estoque.as_view(), name='estoque'),
    path('relatorio', view=Relatorio, name='relatorio'),
]
