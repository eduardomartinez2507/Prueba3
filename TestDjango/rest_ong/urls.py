from django.urls import path
from rest_ong.views import lista_proveedores


urlpatterns = [
    path('lista_proveedores', lista_proveedores, name='lista_proveedores')
]
