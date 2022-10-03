from rest_framework import status, views
from rest_framework.response import Response
from App_Dulces_sueños.Serializers.categoriaSerializer import CategoriaSerializer
from App_Dulces_sueños.models.categoria import Categoria

class CategoriaView(views.APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = CategoriaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(str("La categoria ha sido creada exitosamente"), status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        categorias = Categoria.objects.all()
        categorias_serializers = CategoriaSerializer(categorias, many=True)
        return Response(categorias_serializers.data, status=status.HTTP_200_OK)
