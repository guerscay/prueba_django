"""
URL configuration for proyecto_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# aca puedo ver la modificacion automatica que se hizo cuando cambié la carpeta de lugar
# el tema es que me lo trae automaticamente como ..inicio.views (dos carpetas por arriba de inicio) y yo necesito que sea directo
#desde inicio, y por eso queda finalmente: inicio.views (ver aquí abajo)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("inicio.urls"))    # include el nombre de la aplicacion (inicio) y el archivo donde tengo los "links" (urls)
]
