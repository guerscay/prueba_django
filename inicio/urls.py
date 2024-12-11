# De esta forma voy importando las funcionalidades de las views una por una, pero se puede hacer demasiado largo
# from inicio.views import bienvenida, fecha_y_hora, saludo, mitemplate, mitemplate2, condicional_loop, crear_auto, home, listado_autos

#Esta forma es más práctica
from inicio import views    # sólo tengo qyue agregar views a los urls
from django.urls import path

app_name = 'inicio' # creo esta variable para luego acomodar el tema de los links. Esta variable contiene el nombre de mi aplicacion
                    # y la modificacion se hace sobre el urls.py propio de la aplicación. 

urlpatterns = [
    path('bienvenida', views.bienvenida, name = 'bienvenida'),
    path('', views.home, name = 'home'),
    path('fecha-y-hora/', views.fecha_y_hora,name = 'datetime'),
    path('saludo/<nombre>/<apellido>/', views.saludo, name = 'saludo'), 
    path('mitemplate/', views.mitemplate, name = 'mitemplate'),
    path('mitemplate2/', views.mitemplate2, name = 'mitemplate2'),
    path('condicional_loop/', views.condicional_loop, name = 'condicional_loop'),
    #,path('crear_auto/<str:marca>/<str:modelo>/<int:anio>', crear_auto, name = 'crear_auto') # opcion 1
    path('autos/', views.listado_autos, name='listado_autos')
    ,path('autos/crear', views.crear_auto, name = 'crear_auto')
    ,path('autos/<int:id_auto>', views.ver_auto, name = 'ver_auto')
    ,path('autos/<int:id_auto>/eliminar', views.eliminar_auto, name = 'eliminar_auto')
    ,path('autos/<int:id_auto>/editar', views.editar_auto, name = 'editar_auto')
  
    ]