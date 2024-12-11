### AQUI SE GUARDAN LOS FORMULARIOS
# mira que se parece a models pero mejor
from django import forms

class FormularioBaseAuto(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    anio = forms.IntegerField()

class CrearAuto(FormularioBaseAuto):
    ...
    
class EditarAuto(FormularioBaseAuto):
    ...  

class BuscarAuto(forms.Form):
    marca = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Ford, Fiat, Chevrolet...'}))
    modelo = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Uno, K, 206...'}))
    
