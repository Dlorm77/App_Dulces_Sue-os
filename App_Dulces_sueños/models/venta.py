from django.db import models
from .producto import Producto
from .clientes import Clientes

class Venta(models.Model):
    ID = models.IntegerField(primary_key=True, verbose_name='ID')
    Producto_ID = models.ForeignKey(
        Producto, on_delete=models.CASCADE)
    Clientes_ID = models.ForeignKey(
        Clientes, on_delete=models.CASCADE)
    Cantidad = models.IntegerField(null=True, verbose_name='Cantidad de productos')
    Valor_total = models.IntegerField(null=True, verbose_name='Valor total de venta')