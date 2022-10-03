from rest_framework import status, views
from rest_framework.response import Response
from App_Dulces_sueños.Serializers.modeloSerializer import ModeloSerializer
from App_Dulces_sueños.models.modelo import Modelo

class ModeloView(views.APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = ModeloSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(str("el modelo ha sido creada exitosamente"), status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        modelos = Modelo.objects.all()
        modelos_serializers = ModeloSerializer(modelos, many=True)
        return Response(modelos_serializers.data, status=status.HTTP_200_OK)
