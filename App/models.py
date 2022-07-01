 
from datetime import date
from django.db import models
from django.forms import DateField, IntegerField


# Create your models here.
class Pelicula(models.Model):
    nombre = models.CharField(max_length=40)
    tipo = models.CharField("Género",max_length=20)
    duracion = models.IntegerField("Duración (minutos)")
    autor = models.CharField(max_length=40)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.nombre + " " + self.tipo + " " + str(self.duracion)+"min" 

class Serie(models.Model):
    nombre = models.CharField(max_length=40)
    tipo = models.CharField("Género",max_length=40)
    capitulos = models.IntegerField()
    autor = models.CharField(max_length=40)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.nombre + " " + self.tipo + " " + str(self.capitulos)+"cap" 

class Documental(models.Model):
    nombre = models.CharField(max_length=40)
    tipo = models.CharField("Género",max_length=40)
    duracion = models.IntegerField("Duración (minutos)")
    autor = models.CharField(max_length=40)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.nombre + " " + self.tipo + " " + str(self.duracion)+"min" 
    

    
    