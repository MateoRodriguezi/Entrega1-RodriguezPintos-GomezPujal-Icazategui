from unicodedata import name
from django.urls import path
from AppTienda import views

urlpatterns = [
    path('post-venta/', views.postventa_form, name='Formulario Postventa'),
    path('nuevo-cliente/', views.clientes_formulario, name='Formulario Cliente'),
    path('nuevo-distribuidor/', views.distribuidores_formulario, name='Formulario Distribuidores'),
    path('buscar-distribuidor/', views.busqueda_distribuidor, name="Buscar Distribuidor"),
    path('buscar/', views.buscar),
    path('', views.inicio, name='Inicio'),
    path('clientes/', views.clientes, name='Clientes'),
    path('distribuidores/', views.distribuidores, name='Distribuidores'),
    path('postventa/', views.post_venta, name='Post Venta'),
]