from tokenize import Name
from unicodedata import name
from django.urls import path
from App.views import buscarDocumental, buscarPelicula, buscarSerie, busquedaDocumental, busquedaPelicula, busquedaSerie, documentalesFormulario, peliculasFormulario,inicio, seriesFormulario

urlpatterns = [
    path('peliculasForm/',peliculasFormulario, name = 'CargarPelicula' ),
    path('seriesForm/',seriesFormulario, name = 'CargarSerie' ),
    path('documentalesForm/',documentalesFormulario, name = 'CargarDocumental' ),
    path('',inicio, name = 'Inicio'),
    path('busquedaPelicula/',busquedaPelicula, name ='busquedaPelicula'),
    path('buscarPeli/',buscarPelicula, name ='buscarPelicula'),
    path('busquedaDocumental/',busquedaDocumental, name ='busquedaDocumental'),
    path('buscarDocumental/',buscarDocumental, name ='buscarDocumental'),
    path('busquedaSerie/',busquedaSerie, name ='busquedaSerie'),
    path('buscarSerie/',buscarSerie, name ='buscarSerie'),

]