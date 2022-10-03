from rest_framework import status, views
from rest_framework.response import Response
from App_Dulces_sueños.Serializers.clientesSerializers import ClientesSerializer
from App_Dulces_sueños.models.clientes import Clientes

class ClientesView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = ClientesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(str("El cliente ha sido creada exitosamente"), status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        clients = Clientes.objects.all()
        clientes_serializers = ClientesSerializer(clients, many=True)
        return Response(clientes_serializers.data, status=status.HTTP_200_OK)
