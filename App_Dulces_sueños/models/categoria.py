from django.db import models

class Categoria(models.Model):
    ID = models.IntegerField(primary_key=True, verbose_name='ID')
    Articulo = models.CharField(max_length=20, verbose_name='Articulo')

    def __str__(self):
        fila = "ID: "+ str(self.ID) + " " + "Articulo: " + self.Articulo
        return fila