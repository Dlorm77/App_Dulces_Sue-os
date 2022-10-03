from App_Dulces_sueños.models.producto import Producto
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['ID', 'Modelo_ID','Talla','Precio_Unidad','Precio_Mayor','Stock']

    def create(self, validated_data):
        productoInstance = Producto.objects.create(**validated_data)
        return productoInstance

    def delete(self, obj):
        Producto.objects.delete(ID=obj.ID)
        return str("Borrado exitoso")

    def update(self, validated_data):
        return super().update(Producto, validated_data)

    def get(self):
        return Producto.objects.get()