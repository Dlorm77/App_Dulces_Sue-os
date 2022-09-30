from django.db import models

class Clientes(models.Model):
    ID = models.IntegerField(primary_key=True, verbose_name='ID')
    Nombre = models.CharField(max_length=50, verbose_name='Nombre Completo')
    Celular = models.CharField(max_length=10, verbose_name='Numero de celular')
    Correo = models.CharField(max_length=50, blank=True, null=True, verbose_name='Correo electronico')