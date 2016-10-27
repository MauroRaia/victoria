from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Reclamo(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField()
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    descripcion = models.TextField()
<<<<<<< HEAD
    image = models.ImageField(upload_to = 'static/uploads/reclamos/', null=True, blank=True)
=======
>>>>>>> fbcd2c59eab4af3ca64c6e6a0fb9229d50a3726a
    latitud = models.CharField(max_length=200, null=True, blank=True)
    longitud = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "(" + self.nombre + " " + self.apellido + ") " + self.descripcion
