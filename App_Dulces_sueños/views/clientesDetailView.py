from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from App_Dulces_sueños.Serializers.clientesSerializers import ClientesSerializer
from App_Dulces_sueños.models.clientes import Clientes

class ClientesDetailView(APIView):

    def delete(self, request, pk, format=None):
        Clientes.objects.get(ID=pk).delete()
        return Response ("El cliente ha sido borrada exitosamente", status=status.HTTP_200_OK)

        