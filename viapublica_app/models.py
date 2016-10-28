from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Reclamo(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField()
    correo = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to = 'static/uploads/reclamos/', null=True, blank=True)
    latitud = models.CharField(max_length=200, null=True, blank=True)
    longitud = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "(" + self.nombre + " " + self.apellido + ") " + self.descripcion
