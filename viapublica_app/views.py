from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib import messages
from django.template import RequestContext


# Create your views here.
def index(request):
    formulario_reclamo = ReclamoForm()
    statuses = {'error': request.session.pop('error', None), 'success': request.session.pop('success', None)}
    return render(request, 'views/index.html', {'formulario_reclamo': formulario_reclamo, 'statuses': statuses})

def reclamo_alta(request):
    # PROCESAR EL FORMULARIO
    if request.method == "POST":
        formulario = ReclamoForm(request.POST, request.FILES)
        if formulario.is_valid():
            form = formulario.save(commit=False)
            form.latitud = request.POST['latitud']
            form.logitud = request.POST['longitud']
            form.save()
            # Si todo va bien, muestro la pagina con un formulario nuevo y un mensaje de exito
            request.session['success'] = 'Se ha procesado correctamente su reclamo.'
            formulario_reclamo = ReclamoForm()
        else:
            request.session['error'] = 'Su reclamo no ha podido ser procesado.'
    # Si hubo algun error, muestro la pagina con el mismo formulario que me llego, y un mensaje de error
    return redirect('/viapublica/')

def clasificar(request, pk):
    r = Reclamo.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReclamoForm(request.POST, instance = r)
        if form.is_valid():
            r = form.save(commit=True)
            return redirect('/viapublica/classify')
    else:
        form = ReclamoForm(instance = r)
    return render(request, 'views/clasificar.html', {'form':form})


def vista_reclamos(request):
    reclamos = Reclamo.objects.all()
    return render(request, 'views/vista_reclamos.html', {'reclamos':reclamos})

def classify(request):
    reclamos = Reclamo.objects.filter(seccion__isnull=True)
    return render(request, 'views/classify.html', {'reclamos':reclamos})

def showMap(request, pk):
    s = Seccion.objects.filter(pk=pk)
    r = Reclamo.objects.filter(seccion=s)
    return render(request, 'views/showMap.html', {'s':s, 'r':r})
