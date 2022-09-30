from django.db import models
from .modelo import Modelo
from ..choices import tallas

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