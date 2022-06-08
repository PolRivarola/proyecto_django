from tokenize import Name
from unicodedata import name
from django.urls import path
from App.views import documentalesFormulario, peliculasFormulario,inicio, seriesFormulario

urlpatterns = [
    path('peliculasForm/',peliculasFormulario, name = 'CargarPelicula' ),
    path('seriesForm/',seriesFormulario, name = 'CargarSerie' ),
    path('documentalesForm/',documentalesFormulario, name = 'CargarDocumental' ),
    path('',inicio, name = 'Inicio'),

]