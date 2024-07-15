from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PerfilCreate
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='user/form-login.html'
    ),name='login'),
    path('register/', PerfilCreate.as_view(),name='register')
]
