from rest_framework import status, views
from rest_framework.response import Response
from App_Dulces_sueños.Serializers.productoSerializer import ProductoSerializer
from App_Dulces_sueños.models.producto import Producto

class ProductoView(views.APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(str("El Producto ha sido creado exitosamente"), status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        productos = Producto.objects.all()
        productos_serializers = ProductoSerializer(productos, many=True)
        return Response(productos_serializers.data, status=status.HTTP_200_OK)