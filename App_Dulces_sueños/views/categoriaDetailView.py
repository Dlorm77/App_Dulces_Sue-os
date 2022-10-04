from django.shortcuts import get_object_or_404
from rest_framework import status, views, generics, mixins 
from rest_framework.response import Response
from rest_framework.views import APIView
from App_Dulces_sueños.Serializers.categoriaSerializer import CategoriaSerializer
from App_Dulces_sueños.models.categoria import Categoria

class CategoriaDetailView(APIView):

    def delete(self, request, pk, format=None):
        Categoria.objects.get(ID=pk).delete()
        return Response ("La Categoria ha sido borrada exitosamente", status=status.HTTP_200_OK)


    def put(self, request, pk):
        categoria_lis = get_object_or_404(Categoria.objects.all(), ID=pk)
        data = request.data.get('Categoria')
        serializer = CategoriaSerializer(instance=categoria_lis, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            guardarCategoria = serializer.save()
        return Response({"success": "Article '{}' updated successfully".format(guardarCategoria.Articulo)})


    

        