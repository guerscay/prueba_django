from inicio.views import bienvenida 
from inicio.views import fecha_y_hora, saludo, mitemplate, mitemplate2, condicional_loop, crear_auto, home
from django.urls import path

app_name = 'inicio' # creo esta variable para luego acomodar el tema de los links. Esta variable contiene el nombre de mi aplicacion
                    # y la modificacion se hace sobre el urls.py propio de la aplicación. 

urlpatterns = [
    path('bienvenida', bienvenida, name = 'bienvenida'),
    path('', home, name = 'home'),
    path('fecha-y-hora/', fecha_y_hora,name = 'datetime'),
    path('saludo/<nombre>/<apellido>/', saludo, name = 'saludo'), 
    path('mitemplate/', mitemplate, name = 'mitemplate'),
    path('mitemplate2/', mitemplate2, name = 'mitemplate2'),
    path('condicional_loop/', condicional_loop, name = 'condicional_loop')
    #,path('crear_auto/<str:marca>/<str:modelo>/<int:anio>', crear_auto, name = 'crear_auto') # opcion 1
    ,path('autos/crear', crear_auto, name = 'crear_auto')
    ]