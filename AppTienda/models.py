from urllib.parse import MAX_CACHE_SIZE
from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    mail = models.EmailField()

class Distribuidores(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    direccion = models.CharField(max_length=128)
    email = models.EmailField()

class PostVenta(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()
    fecha = models.DateField()
    producto = models.CharField(max_length=128)
    descripcion_reclamo = models.CharField(max_length=400)


# Create your models here.
