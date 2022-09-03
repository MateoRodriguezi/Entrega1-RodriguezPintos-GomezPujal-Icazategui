from unicodedata import name
from django.urls import path
from AppTienda import views

urlpatterns = [
    path('nuevo-cliente/', views.clientes_formulario, name='Formulario Cliente'),
    path('', views.inicio, name='Inicio'),
    path('clientes/', views.clientes, name='Clientes'),
    path('distribuidores/', views.distribuidores, name='Distribuidores'),
    path('postventa/', views.post_venta, name='Post Venta'),
]
