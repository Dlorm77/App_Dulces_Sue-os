from App_Dulces_sueños.models.modelo import Modelo
from rest_framework import serializers

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ['ID', 'Categoria_ID','Descripcion']

    def create(self, validated_data):
        modeloInstance = Modelo.objects.create(**validated_data)
        return modeloInstance
    
    def delete(self, obj):
            Modelo.objects.delete(ID=obj.ID)
            return str("Borrado exitoso")
        
    def update(self, validated_data):
             return super().update(Modelo, validated_data)

    def get(self):
             return Modelo.objects.get()