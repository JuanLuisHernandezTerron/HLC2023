"""mi_proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('adios/', despedida),
    path('edad/<int:edad>/<int:agno>/', calculaEdadActual),
    path('curso_django/', curso_django),
    path('curso_python/', curso_python),
    path('crearArticulo/<str:nombre>/<str:seccion>/<int:precio>',inserccion_bbdd),
    path('Allarticulos',todos_Articulos),
    path('borrarArticulo/<int:id>',del_articulo),
    path('ActualizarArticulo/<int:id>/<str:nombre>/<str:seccion>/<int:precio>',update_articulo)
]
