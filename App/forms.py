from django import forms

class PelisForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    tipo = forms.CharField()
    duracion = forms.IntegerField()
    
class SeriesForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    tipo = forms.CharField()
    capitulos = forms.IntegerField()

class DocumentalForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    tipo = forms.CharField()
    duracion = forms.IntegerField()
   
   
    