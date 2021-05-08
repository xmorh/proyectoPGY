from django.contrib import admin
from django.urls import path, include
from .views import index, banderines, catalogo, clientes, contacto, nosotros, ofertas, registro, scrunchies, usuario

urlpatterns = [
    path("", index, name="index"),
    path("banderines/", banderines, name="banderines"),
    path('catalogo/', catalogo, name='catalogo'),
    path('clientes/', clientes, name='clientes'),
    path('contacto/', contacto, name='contacto'),
    path('nosotros/', nosotros, name='nosotros'),
    path('ofertas/', ofertas, name='ofertas'),
    path('registro/', registro, name='registro'),
    path('scrunchies/', scrunchies, name='scrunchies'),
    path('usuario/', usuario, name='usuario'),
    path('catalogo/', catalogo, name='catalogo'),
]
