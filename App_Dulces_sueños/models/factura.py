from django.db import models
from .venta import Venta

class Factura(models.Model):
    ID = models.IntegerField(primary_key=True, verbose_name='ID')
    Venta_ID = models.ForeignKey(
        Venta, on_delete=models.CASCADE)
    Fecha = models.DateTimeField(auto_now=True)
    Cantidad = models.IntegerField(null=True, verbose_name='Cantidad')
    Valor_total = models.IntegerField(null=True, verbose_name='Valor total a pagar')