from django.db import models
from .categoria import Categoria

class Modelo(models.Model):
    ID = models.IntegerField(primary_key=True, verbose_name='ID')
    Categoria_ID = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    Descripcion = models.CharField(max_length=45, verbose_name='Descripcion')

    def __str__(self):
        fila = "ID: "+ str(self.ID) + " " + "Descripcion: " + self.Descripcion
        return fila