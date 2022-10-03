from App_Dulces_sueños.models.categoria import Categoria
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Categoria
            fields = ['ID', 'Articulo']

        def create(self, validated_data):
            categoriaInstance = Categoria.objects.create(**validated_data)
            return categoriaInstance

        def delete(self, obj):
            Categoria.objects.delete(ID=obj.ID)
            return str("Borrado exitoso")
        
        def update(self, validated_data):
             return super().update(Categoria, validated_data)

        def get(self):
             return Categoria.objects.all()

