from inicio.views import bienvenida 
from inicio.views import fecha_y_hora, saludo, mitemplate, mitemplate2, condicional_loop, crear_auto
from django.urls import path

urlpatterns = [
    path('bienvenida/', bienvenida),
    path('fecha-y-hora/', fecha_y_hora),
    path('saludo/<nombre>/<apellido>/', saludo), 
    path('mitemplate/', mitemplate),
    path('mitemplate2/', mitemplate2),
    path('condicional_loop/', condicional_loop),
     path('crear_auto/', crear_auto)
    ]