from django import forms

from .models import *

class ReclamoForm(forms.ModelForm):

    class Meta:
        model = Reclamo
        fields = ('nombre',
                  'apellido',
                  'dni',
                  'correo',
                  'telefono',
                  'descripcion',
<<<<<<< HEAD
                  'image',
                  'longitud',
                  'latitud')
        widgets = {
            'latitud': forms.HiddenInput(),
            'longitud': forms.HiddenInput()
        }
=======
                  'longitud')
        widgets = {'latitud': forms.HiddenInput()}
        imagen = forms.ImageField()
>>>>>>> fbcd2c59eab4af3ca64c6e6a0fb9229d50a3726a
