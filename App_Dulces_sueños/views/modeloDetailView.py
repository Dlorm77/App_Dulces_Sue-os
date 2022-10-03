from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from App_Dulces_sueños.Serializers.modeloSerializer import ModeloSerializer
from App_Dulces_sueños.models.modelo import Modelo

class ModeloDetailView(APIView):

    def delete(self, request, pk, format=None):
        Modelo.objects.get(ID=pk).delete()
        return Response ("El Modelo ha sido borrada exitosamente", status=status.HTTP_200_OK)
