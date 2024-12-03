### Acá vamos a estar trabajando nuestras vstas ###

# Una vista es una función
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render 
from inicio.models import Auto
import random

def bienvenida(request):
    return HttpResponse('<h1> Bienvenidos! </h1>')

def fecha_y_hora(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f'<h1> Acá se muestra la hora actual </h1>\n {fecha_y_hora}')

def saludo(request, nombre, apellido):  
    # path dinamico
    nombre_formateado = nombre.title
    apellido_formateado = apellido.title
    return HttpResponse(f'<h1> Hola {nombre} {apellido}  ! como te va?  </h1>')

# --------------------------------------------------------------------------------------------
def mitemplate(request):

# VERSION 1 - ORIGINAL 

    # with open('mitemplate.html') as archivo_abierto:
    #     template = Template(archivo_abierto.read())
    
    # contexto = Context({'nombre':'pepe'})
    # template_renderizado = template.render(contexto)
    
    # #return HttpResponse(template_renderizado)
    # return render(request, 'mitemplate.html', {'nombre':'pepe'} ) # el contexto es opcional

# VERSION 3 - LA QUE QUEDA!!!!!
    return render (request, 'mitemplate.html', {'nombre':'pepe'} ) #request, template, contexto (opcional)


# --------------------------------------------------------------------------------------------
def mitemplate2(request):

# VERSION 2 - NUEVA VERSION MEJORADA
   
    # Cambié el BASE DIR que es algo de python, pero no de DJANGO, entonces necesito usar el loader
    template = loader.get_template('mitemplate2.html')
    
   # Ya no necesitamos crear un contexto pq estamos trabajando con el loader.get_template
   # directamente en lugar del context tenemos que colocar el diccionario que queremos ver
    template_renderizado2 = template.render({'nombre': 'Gremlina'})
    
    # return render(request, 'mitemplate.html')
    return HttpResponse(template_renderizado2)

def condicional_loop(request):
    
    return render (request, 'condicional_loop.html',  {
      'nombre':'Ricardo',
      'mis_elementos':[22],
      'numero': 2,
      'numeros': list(range(15))
      }  ) 

# Todo lo que es views y url se debe combinar en un mismo lugar llamado "APLICACIÓN"

#---------------------------------------------------------------------------------------------

def crear_auto(request):
    # de la terminal interactiva me traigo el codigo
    
    auto = Auto(marca = random.choice(['Ford','Fiat','Renault']), modelo = 'wtf', anio = random.choice([2020,2021,2023]))
    auto.save() # siempre hay que decirle que se guarde 
    
    return render(request, 'auto_correctamente_creado.html', {})