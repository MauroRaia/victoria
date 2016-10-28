from django import forms

from .models import *

class ReclamoForm(forms.ModelForm):

    class Meta:
        model = Reclamo
        fields = '__all__'
        widgets = {
            'latitud': forms.HiddenInput(),
            'longitud': forms.HiddenInput()
        }
