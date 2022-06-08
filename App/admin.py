from django.contrib import admin

from App.models import Documental, Pelicula, Serie

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Serie)
admin.site.register(Documental)