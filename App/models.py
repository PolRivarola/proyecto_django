import email
from django.db import models
from django.forms import DateField, IntegerField

# Create your models here.
class Pelicula(models.Model):
    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=20)
    duracion = models.IntegerField()
    def __str__(self) -> str:
        return self.nombre + " " + self.tipo + " " + str(self.duracion)+"min" 

class Serie(models.Model):
    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    capitulos = models.IntegerField()
    def __str__(self) -> str:
        return self.nombre + " " + self.tipo + " " + str(self.capitulos)+"cap" 

class Documental(models.Model):
    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    duracion = models.IntegerField()
    def __str__(self) -> str:
        return self.nombre + " " + self.tipo + " " + str(self.duracion)+"min" 
    

    