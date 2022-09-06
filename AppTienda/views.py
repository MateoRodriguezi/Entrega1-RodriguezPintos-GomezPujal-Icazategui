from http.client import HTTPResponse
from typing import Dict
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from django.http import HttpResponse
from AppTienda.models import *
from AppTienda.forms import *


from AppTienda.forms import ClientesFormulario

def clientes(request):
    return render (request, 'AppTienda/clientes.html', {'clientes': clientes})


def distribuidores(request):
    distribuidores = Distribuidores.objects.all()
    return render (request, 'AppTienda/distribuidores.html', {'distribuidores': distribuidores})


def inicio(request):
    return render (request, 'AppTienda/inicio.html')


def post_venta(request):
    return render (request, 'AppTienda/postventa.html')

def clientes_formulario(request):
    print('entra a la funcion')
    if request.method == 'POST':
        formulario_1 = ClientesFormulario(request.POST)
        if formulario_1.is_valid():
            data_1 = formulario_1.cleaned_data
            clientes = Clientes (nombre=data_1['nombre'], apellido=data_1['apellido'], email=data_1['email'])
            clientes.save()
            return render(request, 'AppTienda/clientes.html', {"exitoso": True})
    else:
        print('entra aqui')
        formulario_1 = ClientesFormulario()
        return render(request, 'AppTienda/form_clientes.html', {'formulario': formulario_1})

def distribuidores_formulario(request):
    print('entra a la funcion')
    if request.method == 'POST':
        formulario_2 = DistribuidoresFormulario(request.POST)
        if formulario_2.is_valid():
            data_2 = formulario_2.cleaned_data
            distribuidores = Distribuidores (nombre=data_2['nombre'], apellido=data_2['apellido'],direccion=data_2['direccion'] , email=data_2['email'])
            distribuidores.save()
            return render(request, 'AppTienda/distribuidores.html', {"exitoso": True})
    else:
        print('entra aqui')
        formulario_2 = DistribuidoresFormulario()
        return render(request, 'AppTienda/form_distribuidores.html', {'formulario': formulario_2})

def postventa_form(request):
    print('entra a la funcion')
    if request.method == 'POST':
        formulario_3 = PostVentaFormulario(request.POST)
        if formulario_3.is_valid():
            data_3 = formulario_3.cleaned_data
            postventa = PostVenta (nombre=data_3['nombre'], apellido=data_3['apellido'],email=data_3['email'] , fecha=data_3['fecha'], producto=data_3['producto'], descripcion_reclamo=data_3['descripcion_reclamo'] )
            postventa.save()
            return render(request, 'AppTienda/postventa.html', {"exitoso": True})
    else:
        print('entra aqui')
        formulario_3 = PostVentaFormulario()
        return render(request, 'AppTienda/form_postventa.html', {'formulario': formulario_3})

def busqueda_distribuidor(request):
    return render(request,"AppTienda/busqueda_distribuidor.html")

def buscar(request):
    if request.GET["direccion"]:
        direccion = request.GET["direccion"]
        distribuidores = Distribuidores.objects.filter(direccion__icontains=direccion)
        return render(request, 'AppTienda/distribuidores.html', {'distribuidores': distribuidores})
    else:
        return render(request, 'AppTienda/distribuidores.html', {'distribuidores': []})

# Create your views here.