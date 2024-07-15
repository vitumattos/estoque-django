from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .form import PerfilForm

from .models import Perfil
# Create your views here.


class PerfilCreate(CreateView):
    template_name = "user/form-register.html"
    form_class = PerfilForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='Funcionario')
        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url
