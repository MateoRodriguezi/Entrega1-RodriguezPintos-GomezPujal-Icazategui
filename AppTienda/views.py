from http.client import HTTPResponse
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from django.http import HttpResponse
from AppTienda.models import*
from AppTienda.forms import*


from AppTienda.forms import ClientesFormulario

def clientes(request):
    return render (request, 'AppTienda/clientes.html')


def distribuidores(request):
    return render (request, 'AppTienda/distribuidores.html')


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
            clientes = Clientes (nombre=data_1['nombre'], apellido=data_1['apellido'], mail=data_1['mail'])
            clientes.save()
            return render(request, 'AppTienda/inicio.html')
    else:
        print('entra aqui')
        formulario_1 = ClientesFormulario()
        return render(request, 'AppTienda/form_clientes.html', {'formulario': formulario_1})


# Create your views here.
