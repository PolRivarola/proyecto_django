from django.contrib import admin
from django.urls import path
from App.views import curso,familia
urlpatterns = [
    path('admin/', admin.site.urls),
    path('curso/', curso),
    path('familia/', familia)
]
