from App_Dulces_sueños.models.clientes import Clientes
from rest_framework import serializers

class ClientesSerializer(serializers.ModelSerializer):     
    class Meta:         
        model = Clientes         
        fields = ['ID', 'Nombre','Celular','Correo']    

    def create(self, validated_data):         
        clientesInstance = Clientes.objects.create(**validated_data)         
        return clientesInstance

    def delete(self, obj):
        Clientes.objects.delete(ID=obj.ID)
        return str("Borrado exitoso")
        
    def update(self, validated_data):
         return super().update(Clientes, validated_data)

    def get(self):
         return Clientes.objects.get()