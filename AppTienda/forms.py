from django import forms

class ClientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    apellido = forms.CharField(max_length=128)
    email = forms.EmailField()

class DistribuidoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    apellido = forms.CharField(max_length=128)
    direccion = forms.CharField(max_length=400)
    email = forms.EmailField()

class PostVentaFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    apellido = forms.CharField(max_length=128)
    email = forms.EmailField()
    fecha = forms.DateField()
    producto = forms.CharField(max_length=128)
    descripcion_reclamo = forms.CharField(max_length=400)
    
