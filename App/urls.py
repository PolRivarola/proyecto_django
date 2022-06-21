from tokenize import Name
from unicodedata import name
from django.urls import path
from App.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('',inicio, name = 'Inicio'),
    path('busquedaPelicula/',busquedaPelicula, name ='busquedaPelicula'),
    path('buscarPeli/',buscarPelicula, name ='buscarPelicula'),
    path('documental/busquedaDocumental/',busquedaDocumental, name ='busquedaDocumental'),
    path('documental/buscarDocumental/',buscarDocumental, name ='buscarDocumental'),
    path('busquedaSerie/',busquedaSerie, name ='busquedaSerie'),
    path('buscarSerie/',buscarSerie, name ='buscarSerie'),
    path('peli/list/',PelisList.as_view(),name = 'pelisList'),
    path('peli/<pk>',PelisDetail.as_view(),name = 'pelisDetail'),
    path('peli/nuevo/',PelisCreate.as_view(),name = 'pelisCreate'),
    path('peli/edicion/<pk>',PelisUpdate.as_view(),name = 'pelisUpdate'),
    path('peli/eliminar/<pk>',PelisDelete.as_view(),name = 'pelisDelete'),
    path('serie/list/',SeriesList.as_view(),name = 'seriesList'),
    path('serie/<pk>',SeriesDetail.as_view(),name = 'seriesDetail'),
    path('serie/nuevo/',SeriesCreate.as_view(),name = 'seriesCreate'),
    path('serie/edicion/<pk>',SeriesUpdate.as_view(),name = 'seriesUpdate'),
    path('serie/eliminar/<pk>',SeriesDelete.as_view(),name = 'seriesDelete'),
    path('documental/list/',DocumentalesList.as_view(),name = 'documentalesList'),
    path('documental/<pk>',DocumentalesDetail.as_view(),name = 'documentalesDetail'),
    path('documental/nuevo/',DocumentalesCreate.as_view(),name = 'documentalesCreate'),
    path('documental/edicion/<pk>',DocumentalesUpdate.as_view(),name = 'documentalesUpdate'),
    path('documental/eliminar/<pk>',DocumentalesDelete.as_view(),name = 'documentalesDelete'),
    path('user/login',login_request,name='login'),
    path('user/register',register_request,name='register'),
    path('user/logout',LogoutView.as_view(template_name='App/user/logout.html'),name='logout'),
    path('user/editarUser',editarUser,name='editarUser'),
    path('about/',about,name='about'),

]