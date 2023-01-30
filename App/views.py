from django.http import HttpResponse
from django.shortcuts import render
from App.models import Documental, Pelicula, Serie
from App.forms import UserEditForm,UserRegistrationForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate

from django.template import loader

# Create your views here.


def inicio(request):
        return render(request,"App/inicio.html")


def busquedaPelicula(request):
    return render(request,"App/peliculas/busquedaPelicula.html")

def busquedaSerie(request):
    return render(request,"App/series/busquedaSerie.html")

def busquedaDocumental(request):
    return render(request,"App/documentales/busquedaDocumental.html")

def buscarPelicula(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        pelis = Pelicula.objects.filter(nombre=nombre) | Pelicula.objects.filter(nombre__startswith=nombre[0]) 
        return render(request,'App/peliculas/resultadosBusqueda.html',{'pelis':pelis, 'nombre':nombre})
    else:
        return render(request,'App/noSeIngreso.html')

def buscarSerie(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        series = Serie.objects.filter(nombre=nombre) | Serie.objects.filter(nombre__startswith=nombre[0]) 
        return render(request,'App/series/resultadosBusquedaSerie.html',{'series':series, 'nombre':nombre})
    else:
        return render(request,'App/noSeIngreso.html')

def buscarDocumental(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        documentales = Documental.objects.filter(nombre=nombre) | Documental.objects.filter(nombre__startswith=nombre[0]) 
        return render(request,'App/documentales/resultadosBusquedaDocumentales.html',{'documentales':documentales, 'nombre':nombre})
    else:
        return render(request,'App/noSeIngreso.html')
##################Peliculas#############################

class PelisList(ListView):
    model = Pelicula
    template_name= 'App/peliculas/pelicula_list.html'
    
class PelisDetail(DetailView):
    model = Pelicula
    template_name= 'App/peliculas/pelicula_detail.html'

class PelisCreate(LoginRequiredMixin,CreateView):
    model = Pelicula
    success_url= reverse_lazy('pelisList')
    fields=  ['nombre','tipo','duracion','autor']
    template_name= 'App/peliculas/pelicula_form.html'

class PelisUpdate(LoginRequiredMixin,UpdateView):
    model = Pelicula
    success_url= reverse_lazy('pelisList')
    fields=  ['nombre','tipo','duracion']
    template_name= 'App/peliculas/pelicula_form.html'

class PelisDelete(LoginRequiredMixin,DeleteView):
    model = Pelicula
    success_url= reverse_lazy('pelisList')
    template_name= 'App/peliculas/pelicula_confirm_delete.html'

##################Series#############################
    
class SeriesList(ListView):
    model = Serie
    template_name= 'App/series/serie_list.html'
    
class SeriesDetail(DetailView):
    model = Serie
    template_name= 'App/series/serie_detail.html'

class SeriesCreate(LoginRequiredMixin,CreateView):
    model = Serie
    success_url= reverse_lazy('seriesList')
    fields=  ['nombre','tipo','capitulos','autor']
    template_name= 'App/series/serie_form.html'

class SeriesUpdate(LoginRequiredMixin,UpdateView):
    model = Serie
    success_url= reverse_lazy('seriesList')
    fields=  ['nombre','tipo','capitulos']
    template_name= 'App/series/serie_form.html'


class SeriesDelete(LoginRequiredMixin,DeleteView):
    model = Serie
    success_url= reverse_lazy('seriesList')
    template_name= 'App/series/serie_confirm_delete.html'

##################Documentales#############################
    
class DocumentalesList(ListView):
    model = Documental
    template_name= 'App/documentales/documental_list.html'
    
class DocumentalesDetail(DetailView):
    model = Documental
    template_name= 'App/documentales/documental_detail.html'

class DocumentalesCreate(LoginRequiredMixin,CreateView):
    model = Documental
    success_url= reverse_lazy('documentalesList')
    fields=  ['nombre','tipo','duracion','autor']
    template_name= 'App/documentales/documental_form.html'

class DocumentalesUpdate(LoginRequiredMixin,UpdateView):
    model = Documental
    success_url= reverse_lazy('documentalesList')
    fields=  ['nombre','tipo','duracion']
    template_name= 'App/documentales/documental_form.html'


class DocumentalesDelete(LoginRequiredMixin,DeleteView):
    model = Documental
    success_url= reverse_lazy('documentalesList')
    template_name= 'App/documentales/documental_confirm_delete.html'

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            user = authenticate(username= usuario,password=clave)
            if user is not None:
                login(request,user)
                return render(request, 'App/inicio.html')

            else:
                return render(request, 'App/inicio.html',{'mensaje':'Datos incorrectos'})
        else:
            return render(request, 'App/inicio.html',{'mensaje':'Error en formulario'})

    else:
        form= AuthenticationForm()
        return render(request,'App/user/login.html',{'form':form})
    
def register_request(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return render(request, 'App/inicio.html',{'mensaje':f'Usuario {username} creado con exito'})
        else:
            return render(request, 'App/inicio.html',{'mensaje':'Error, usuario no creado'})

    else:
        form = UserRegistrationForm()
        return render(request, 'App/user/register.html',{'form':form})

@login_required
def editarUser(request):
    usuario = request.user
    if request.user == 'POST':
        form = UserEditForm(request.POST,instance = usuario)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            
            usuario.save()
            return render(request,'App/inicio.html',{'mensaje':'Cambios exitoso'})
    else:
        form = UserEditForm(instance = usuario)
    return render(request,'App/user/editarUser.html',{'formulario':form,'user':usuario.username})

         
def error_404(request,exception):
    return render(request,'App/404.html')

def about(request):
    return render(request,'App/about.html') 