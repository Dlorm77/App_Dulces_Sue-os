from django.contrib import admin

from .models.categoria import Categoria
from .models.modelo import Modelo
from .models.producto import Producto
from .models.venta import Venta
from .models.clientes import Clientes
from .models.factura import Factura

from django.contrib import admin
from .models.user import User
from .models.account import Account


admin.site.register(User)
admin.site.register(Account)


admin.site.register(Categoria)
admin.site.register(Modelo)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Clientes)
admin.site.register(Factura)
# Register your models here.
