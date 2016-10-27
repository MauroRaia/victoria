from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your views here.
def index(request):
    formulario_reclamo = ReclamoForm()
    return render(request, 'views/index.html', {'formulario_reclamo': formulario_reclamo})

def reclamo_alta(request):
    # PROCESAR EL FORMULARIO
    if request.method == "POST":
        formulario = ReclamoForm(request.POST, request.FILES)
        if formulario.is_valid():
            form = formulario.save(commit=False)
            form.latitud = request.POST['latitud']
            form.logitud = request.POST['longitud']
<<<<<<< HEAD
            form.save()
            return render( request,'views/partials/reclamo_alta.html',{})
    return render( request,'views/partials/error.html',{})
=======
	    m.save()
            form.save()
            return render( request,'views/partials/reclamo_alta.html',{})
>>>>>>> fbcd2c59eab4af3ca64c6e6a0fb9229d50a3726a
