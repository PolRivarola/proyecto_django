from django.http import HttpResponse
from django.shortcuts import render
from App.models import Curso,Familiar
import datetime
from django.template import Template,Context,loader

# Create your views here.

def curso(self):
    curso = Curso(nombre='DW', camada = 33002)
    curso.save()
    doc = f"Curso: {curso.nombre} - Camada: {curso.camada}"
    return HttpResponse(doc)

def familia(self):
    papa = Familiar(nombre = 'Pablo', dni = 12345, cumpleanos = datetime.date(1994,3,5))
    mama = Familiar(nombre = 'Flor', dni = 12335, cumpleanos = datetime.date(1996,8,5))
    hermano = Familiar(nombre = 'Mario', dni = 34345, cumpleanos = datetime.date(2010,2,5))
    hermana = Familiar(nombre = 'Maria', dni = 66345, cumpleanos = datetime.date(2020,7,5))
    familia = [papa,mama,hermano,hermana]
    for i in familia:
        i.save()
    diccionario={"fam":familia}
    plantilla = loader.get_template("familia.html")
    
    
    doc = plantilla.render(diccionario)
    
    return HttpResponse(doc)