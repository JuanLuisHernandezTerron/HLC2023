from django.shortcuts import render
from django.http import HttpResponse
import datetime

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
# Create your views here.
