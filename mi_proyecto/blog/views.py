from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from blog.models import Articulos


def saludo(request):
    return HttpResponse("Esta la primera página del blog")

def despedida(request):
      return HttpResponse("Esta es la página de despedida")

def damefecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """
    <html>
    <body>
    <h2>
    La fecha y hora actual es: {}
    </h2>
    </body>
    </html>
    """.format(fecha_actual)
    return HttpResponse(documento)

def calculaEdadActual(request, edad, agno):
      periodo = agno - datetime.datetime.now().year 
      nueva_edad = edad + periodo
      documento = """
        <html>
        <body>
        <h2>
        En el año {} tendrás: {}
        </h2>
        </body>
        </html>
        """.format(agno, nueva_edad)

      return HttpResponse(documento)

def saludo(request):
    return render(request, "saludo.html", {"nombre_persona": "Juan", "apellido_persona": "Pérez", "fecha_actual": datetime.datetime.now()})

class Persona(object):
      def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludoPersona(request):
      persona = Persona("Chema", "Durán")
      fecha_actual = datetime.datetime.now()
      return render(request, "saludo.html", {"nombre_persona":persona.nombre, "apellido_persona":persona.apellido, "fecha_actual":fecha_actual})

def saludoTemas(request):
      persona = Persona("Chema", "Durán")
      temas_del_curso = ["Formularios", "Modelos", "Vistas", "Despliegue"]
      fecha_actual = datetime.datetime.now()
      return render(request, "saludo.html", {"nombre_persona":persona.nombre, "apellido_persona":persona.apellido, "fecha_actual":fecha_actual, "temas" : temas_del_curso})

def curso_django(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "curso_django.html", {"fecha_actual":fecha_actual})

def curso_python(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "curso_python.html", {"fecha_actual":fecha_actual})

def inserccion_bbdd(request,nombre,seccion,precio):
    filtrar = Articulos.crear_articulo(nombre,seccion,precio)
    return render(request,"crearArticulo.html",{"articulo":filtrar})

def todos_Articulos(request):
    articulos = Articulos.todos_articulos()
    return render(request,"articulos.html",{"articulos":articulos})

def del_articulo(request,id):
    Articulos.borrar_articulos(id)
    documento = """
        <html>
        <body>
        <h2>
        El id borrado es {}
        </h2>
        </body>
        </html>
        """.format(id)
    return HttpResponse(documento)

def update_articulo(request,id,nombre,seccion,precio):
    articulo=Articulos.actualizar_articulos(id,nombre,seccion,precio)
    return render(request,"crearArticulo.html",{"articulos":articulo})

# Create your views here.
