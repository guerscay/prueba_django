from django.db import models

class Auto(models.Model): #Creo una clase X, pero con herencia models.Model
    marca = models.CharField(max_length = 20)
    modelo = models.CharField(max_length = 20)
    anio = models.IntegerField()