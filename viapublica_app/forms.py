from django import forms

from .models import *

class ReclamoForm(forms.ModelForm):

    class Meta:
        model = Reclamo
        fields = ['nombre', 'apellido', 'dni', 'correo', 'telefono', 'descripcion', 'imagen', 'latitud', 'longitud', 'seccion']
        widgets = {
            'latitud': forms.HiddenInput(),
            'longitud': forms.HiddenInput()
        }
