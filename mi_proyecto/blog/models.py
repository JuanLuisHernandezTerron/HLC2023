from django.db import models

class Clientes(models.Model):
        nombre = models.CharField(max_length=60,verbose_name='Nombre completo del cliente')
        direccion = models.CharField(max_length=60)
        email = models.CharField(max_length=20)
        telefono = models.CharField(max_length=7)

class Articulos(models.Model):
        nombre = models.CharField(max_length=15)
        seccion = models.CharField(max_length=25)
        precio = models.IntegerField()

        def crear_articulo(nombreArti,seccionArti,precioArti):
                art = Articulos(nombre=nombreArti,seccion=seccionArti,precio=precioArti)
                art.save() #Lo guarda en la base de datos
                return art
        
        def todos_articulos():
                todos = Articulos.objects.all()
                return todos
        
        def borrar_articulos(id_articulo):
                Articulos.objects.get(id=id_articulo).delete() #Lo borra de la base de datos
        
        def actualizar_articulos(id_articulo, p_nombre, p_seccion, p_precio):
                articulo=Articulos.objects.get(id=id_articulo)
                articulo.nombre = p_nombre
                articulo.seccion = p_seccion
                articulo.precio = p_precio
                articulo.save()
                return articulo

        def __str__(self):
                return '{} y su precio es {}'.format(self.nombre,self.precio)
class Pedidos(models.Model):
        numero = models.IntegerField()
        fecha = models.DateField()
        entregado = models.BooleanField()
# Create your models here.
