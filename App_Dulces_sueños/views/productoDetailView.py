from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from App_Dulces_sueños.Serializers.productoSerializer import ProductoSerializer
from App_Dulces_sueños.models.producto import Producto

class ProductoDetailView(APIView):

    def delete(self, request, pk, format=None):
        Producto.objects.get(ID=pk).delete()
        return Response ("El Producto ha sido borrado exitosamente", status=status.HTTP_200_OK)


def put(self, request, pk):
    categoria_lis = get_object_or_404(Producto.objects.all(), ID=pk)
    data = request.data.get('Categoria')
    serializer = ProductoSerializer(instance=categoria_lis, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        guardarCategoria = serializer.save()
    return Response({"success": "Article '{}' updated successfully".format(guardarCategoria.Articulo)})