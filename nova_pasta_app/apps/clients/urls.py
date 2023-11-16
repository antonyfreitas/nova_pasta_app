# Criar um "urls.py" dentro dos arquivos de configuracao do produto em "apps/clients".
# Nesse local serao declaradas as urls especificas do App clients. Adicionar ao arquivo 
# as linhas a seguir.

from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'clients'

router = routers.DefaultRouter()
router.register('clientes', views.ClientViewSet, basename='clientes')
router.register('clientes_redessociais', views.ClientSocialnetworkViewSet, basename='clientes_redessociais')

urlpatterns = [
    path('', include(router.urls) )
]

