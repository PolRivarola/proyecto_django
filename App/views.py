from django.http import HttpResponse
from django.shortcuts import render
from App.forms import DocumentalForm, PelisForm, SeriesForm
from App.models import Documental, Pelicula, Serie
import datetime
from django.template import Template,Context,loader

# Create your views here.

def peliculasFormulario(request):
    if request.method == 'POST':
        
        miFormulario = PelisForm(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
        nombre =info['nombre']
        tipo = info['tipo']
        duracion = info['duracion']
        peli = Pelicula(nombre = nombre , tipo = tipo, duracion = duracion )
        peli.save()
        return render(request,'App/inicio.html')
        

    else:
        miFormulario = PelisForm()
    return render(request,'App/peliculasForm.html', {'miFormulario':miFormulario})

def inicio(self):
    plantilla = loader.get_template("App/inicio.html")
    documento= plantilla.render()
    return HttpResponse(documento)

def documentalesFormulario(request):
    if request.method == 'POST':
        
        miFormulario = DocumentalForm(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
        nombre =info['nombre']
        tipo = info['tipo']
        duracion = info['duracion']
        peli = Documental(nombre = nombre , tipo = tipo, duracion = duracion )
        peli.save()
        return render(request,'App/inicio.html')
        

    else:
        miFormulario = DocumentalForm()
    return render(request,'App/documentalesForm.html', {'miFormulario':miFormulario})

def inicio(self):
    plantilla = loader.get_template("App/inicio.html")
    documento= plantilla.render()
    return HttpResponse(documento)

def seriesFormulario(request):
    if request.method == 'POST':
        
        miFormulario = SeriesForm(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
        nombre =info['nombre']
        tipo = info['tipo']
        capitulos = info['capitulos']
        serie = Serie(nombre = nombre , tipo = tipo, capitulos = capitulos )
        serie.save()
        return render(request,'App/inicio.html')
        

    else:
        miFormulario = SeriesForm()
    return render(request,'App/seriesForm.html', {'miFormulario':miFormulario})

def busquedaPelicula(request):
    return render(request,"App/busquedaPelicula.html")

def busquedaSerie(request):
    return render(request,"App/busquedaSerie.html")

def busquedaDocumental(request):
    return render(request,"App/busquedaDocumental.html")

def buscarPelicula(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        pelis = Pelicula.objects.filter(nombre = nombre)
        return render(request,'App/resultadosBusqueda.html',{'pelis':pelis, 'nombre':nombre})
    else:
        respuesta = "No se ingreso camada"
    return HttpResponse(respuesta)

def buscarSerie(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        series = Serie.objects.filter(nombre = nombre)
        return render(request,'App/resultadosBusquedaSerie.html',{'series':series, 'nombre':nombre})
    else:
        respuesta = "No se ingreso camada"
    return HttpResponse(respuesta)

def buscarDocumental(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        documentales = Documental.objects.filter(nombre = nombre)
        return render(request,'App/resultadosBusquedaDocumentales.html',{'documentales':documentales, 'nombre':nombre})
    else:
        respuesta = "No se ingreso camada"
    return HttpResponse(respuesta)