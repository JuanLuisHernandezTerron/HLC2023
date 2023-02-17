from django.contrib import admin
from blog.models import Articulos, Clientes, Pedidos

# Register your models here.
admin.site.register(Articulos)
admin.site.register(Clientes)
admin.site.register(Pedidos)