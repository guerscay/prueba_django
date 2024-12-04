### AQUI SE GUARDAN LOS FORMULARIOS
# mira que se parece a models pero mejor
from django import forms

class CrearAuto(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    anio = forms.IntegerField()