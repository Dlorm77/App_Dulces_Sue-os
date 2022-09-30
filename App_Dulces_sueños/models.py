from django.db import models
from .choices import tallas

# Create your models here.

class Categoria(models.Model):
    ID = models.IntegerField(primary_key=True, verbose_name='ID')
    Articulo = models.CharField(max_length=20, verbose_name='Articulo')

    def __str__(self):
        fila = "ID: "+ str(self.ID) + " " + "Articulo: " + self.Articulo
        return fila

class Modelo(models.Model):
    ID = models.IntegerField(primary_key=True, verbose_name='ID')
    Categoria_ID = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    Descripcion = models.CharField(max_length=45, verbose_name='Descripcion')

    def __str__(self):
        fila = "ID: "+ str(self.ID) + " " + "Descripcion: " + self.Descripcion
        return fila

class Producto(models.Model):
    ID = models.IntegerField(primary_key=True, verbose_name='ID')
    Modelo_ID = models.ForeignKey(
        Modelo, on_delete=models.CASCADE)
    Talla = models.CharField(max_length=2, choices=tallas, verbose_name='Talla')
    Precio_Unidad = models.IntegerField(null=True, verbose_name='Precio X Unidad')
    Precio_Mayor = models.IntegerField(null=True, verbose_name='Precio X Mayor')
    Stock = models.IntegerField(null=True, verbose_name='Stock')

    def __str__(self):
        fila = "Modelo_"+ str(self.Modelo_ID) + " " + "Talla: " + self.Talla
        return fila

class Clientes(models.Model):
    ID = models.IntegerField(primary_key=True, verbose_name='ID')
    Nombre = models.CharField(max_length=50, verbose_name='Nombre Completo')
    Celular = models.CharField(max_length=10, verbose_name='Numero de celular')
    Correo = models.CharField(max_length=50, blank=True, null=True, verbose_name='Correo electronico')

class Venta(models.Model):
    ID = models.IntegerField(primary_key=True, verbose_name='ID')
    Producto_ID = models.ForeignKey(
        Producto, on_delete=models.CASCADE)
    Clientes_ID = models.ForeignKey(
        Clientes, on_delete=models.CASCADE)
    Cantidad = models.IntegerField(null=True, verbose_name='Cantidad de productos')
    Valor_total = models.IntegerField(null=True, verbose_name='Valor total de venta')

class Factura(models.Model):
    ID = models.IntegerField(primary_key=True, verbose_name='ID')
    Venta_ID = models.ForeignKey(
        Venta, on_delete=models.CASCADE)
    Fecha = models.DateTimeField(auto_now=True)
    Cantidad = models.IntegerField(null=True, verbose_name='Cantidad')
    Valor_total = models.IntegerField(null=True, verbose_name='Valor total a pagar')


