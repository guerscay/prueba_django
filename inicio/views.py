### Acá vamos a estar trabajando nuestras vstas ###

# Una vista es una función
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from inicio.models import Auto
import random
from inicio.forms import CrearAuto, BuscarAuto, EditarAuto


def home(request):
    #return HttpResponse('<h1> Bienvenidos! </h1>')
    return render (request, 'inicio/home.html', {})

def bienvenida(request):
    #return HttpResponse('<h1> Bienvenidos! </h1>')
    return render (request, 'inicio/bienvenida.html', {})


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
    return render (request, 'inicio/mitemplate.html', {'nombre':'pepe'} ) #request, template, contexto (opcional)


# --------------------------------------------------------------------------------------------
def mitemplate2(request):

# VERSION 2 - NUEVA VERSION MEJORADA
   
    # Cambié el BASE DIR que es algo de python, pero no de DJANGO, entonces necesito usar el loader
    template = loader.get_template('inicio/mitemplate2.html')
    
   # Ya no necesitamos crear un contexto pq estamos trabajando con el loader.get_template
   # directamente en lugar del context tenemos que colocar el diccionario que queremos ver
    template_renderizado2 = template.render({'nombre': 'Gremlina'})
    
    # return render(request, 'mitemplate.html')
    return HttpResponse(template_renderizado2)

def condicional_loop(request):
    
    return render (request, 'inicio/condicional_loop.html',  {
      'nombre':'Ricardo',
      'mis_elementos':[22],
      'numero': 2,
      'numeros': list(range(15))
      }  ) 

# Todo lo que es views y url se debe combinar en un mismo lugar llamado "APLICACIÓN"

#---------------------------------------------------------------------------------------------
# opcion 1
# def crear_auto(request, marca, modelo, anio):
#     # de la terminal interactiva me traigo el codigo
    
#     #auto = Auto(marca = random.choice(['Ford','Fiat','Renault']), modelo = 'wtf', anio = random.choice([2020,2021,2023]))
#     auto = Auto(marca = marca, modelo = modelo, anio = anio)
#     auto.save()
    
#     return render(request, 'inicio/auto_correctamente_creado.html', {'auto':auto})
#_---------------------------------------------------------------------------------------

# Opcion 2 crear auto - post/get sin formulario
# def crear_auto(request):
    
#     ###### VEAMOS QUE EL GET SE PUEDE USAR, PERO NO SE RECOMIENDA  ######
    
#     #Verifica los datos que recibes
#     print('*****************************')
#     print('GET', request.GET)  # Verifica qué datos estás recibiendo
#     print('POST', request.POST)
#     print('******************************')

    # marca = request.GET.get('marca')
    # modelo = request.GET.get('modelo')
    # anio = request.GET.get('anio')

    # # Para evitar el error de los not null
    # if marca and modelo and  anio:
    #    # Si los parámetros son válidos, guarda el auto
    #     auto = Auto(marca=marca, modelo=modelo, anio=anio)
    #     auto.save() 

    # # Renderiza la página de éxito
    # return render(request, 'inicio/crear_auto.html', {})

###### AHORA LO HACEMOS CON EL POST
# def crear_auto(request):
    
#     marca = request.POST.get('marca')
#     modelo = request.POST.get('modelo')
#     anio = request.POST.get('anio')

#     # si la request viene por POST sí lo creo, si viene por GET no
#     if request.method == 'POST':
        
#     # Para evitar el error de los not null
#         if marca and modelo and  anio:
#         # Si los parámetros son válidos, guarda el auto
#             auto = Auto(marca=marca, modelo=modelo, anio=anio)
#             auto.save() 

#     # Renderiza la página de éxito
#     return render(request, 'inicio/crear_auto.html', {})

# -----------------------------------------------------------------------------
# Opción 3 - Formulario (inicio/forms.py)
    #Para esto tengo que hacer el import forms
    
def crear_auto(request):
    
    print('*****************************')
    
    formulario = CrearAuto()
    
    # si la request viene por POST sí lo creo, si viene por GET no
    if request.method == 'POST':
        formulario = CrearAuto(request.POST)   
        if formulario.is_valid():
            
            data = formulario.cleaned_data
            
            auto = Auto(marca=data.get('marca'), modelo=data.get('modelo'), anio=data.get('anio'))
            auto.save() 
            
            return render(request, 'inicio/home.html',{})

    # Renderiza la página de crear auto
    return render(request, 'inicio/crear_auto.html', {'formulario':formulario}) #mi contexto ahora es el formulario

# --------------------------------------------------------------------------------------------

# Opción 1 - Traer todo sin buscar
# def listado_autos(request):
#     listado_autos = Auto.objects.all() # quiero todos los objetos de auto

# Opción 2 - si quiero filtrar el auto que obtengo mediante una busqueda
# def listado_autos(request):
#     buscar_marca = request.GET.get('marca')
#     #buscar_modelo = request.GET.get('modelo')
    
#     if buscar_marca:
#         listado_autos = Auto.objects.filter(marca__icontains = buscar_marca) #filtra que la marca del auto CONTENGA los caracteres que busco
#     else: 
#         listado_autos = Auto.objects.all()


    
    # # Opcion 3 - Usando el GET
    # listado_autos = Auto.objects.filter(marca__icontains = buscar_marca, modelo__icontains = buscar_modelo)
    # return render(request, 'inicio/listado_autos.html', {'listado_autos':listado_autos})
  
    ### Modificacion de chatgpt - me gusta mas ###
    # Obtener los parámetros de búsqueda desde la URL
    # buscar_marca = request.GET.get('marca')
    # buscar_modelo = request.GET.get('modelo')
    
    # # Filtrar según los parámetros proporcionados, si existen
    # if buscar_marca and buscar_modelo:
    #     listado_autos = Auto.objects.filter(marca__icontains=buscar_marca, modelo__icontains=buscar_modelo)
    # elif buscar_marca:  # Si solo se proporciona marca
    #     listado_autos = Auto.objects.filter(marca__icontains=buscar_marca)
    # elif buscar_modelo:  # Si solo se proporciona modelo
    #     listado_autos = Auto.objects.filter(modelo__icontains=buscar_modelo)
    # else:  # Si no se proporciona ningún filtro, traer todos los autos
    #     listado_autos = Auto.objects.all()
    
    # Opcion 4 - UTILIZANDO LOS FORMULARIOS DE DJANGO
    
def listado_autos(request):
    
    formulario_busqueda = BuscarAuto(request.GET or None)

    if formulario_busqueda.is_valid():
        marca_a_buscar = formulario_busqueda.cleaned_data.get('marca', '')
        modelo_a_buscar = formulario_busqueda.cleaned_data.get('modelo', '')
        resultado_autos = Auto.objects.filter(
            marca__icontains=marca_a_buscar, 
            modelo__icontains=modelo_a_buscar
        )
    else:
        resultado_autos = []

    return render(request, 'inicio/listado_autos.html', {
        'listado_autos': resultado_autos, 
        'formulario': formulario_busqueda
    })
    
    # --------------------------------------------------------------------------------------------
    
def ver_auto(request, id_auto):
    
    auto = Auto.objects.get(id = id_auto)
    
    return render(request, 'inicio/ver_auto.html', {'auto': auto})

# ------------------------------------------------
def eliminar_auto(request, id_auto):

    auto = Auto.objects.get(id = id_auto)
    
    auto.delete()
    
    return render(request, 'inicio/eliminar_auto.html', {'auto': auto})

# ------------------------------------------------
def editar_auto(request, id_auto):
    
    auto = Auto.objects.get(id = id_auto)
    
    formulario = EditarAuto(initial= {'marca': auto.marca
                                      , 'modelo': auto.modelo
                                      , 'anio': auto.anio})
    
    if request.method == 'POST':
        formulario = EditarAuto(request.POST)
        if formulario.is_valid():
                        
            auto.marca = formulario.cleaned_data.get('marca')
            auto.modelo = formulario.cleaned_data.get('modelo')
            auto.anio = formulario.cleaned_data.get('anio')
        
            auto.save()
            
            return redirect ('inicio:listado_autos.html')
      
    return render(request, 'inicio/editar_auto.html', {'formulario': formulario, 'auto': auto})