from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProductSerializer
from .models import Product

class ProductApi(APIView):

    def get(self, request):
        products = Product.objects.all().order_by('-created_at')
        serializer = ProductSerializer(products, many=True)
        if products:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Products not found!"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        name = request.data.get('name')
        description = request.data.get('description')
        price = request.data.get('price')

        try:
            if not name or not description or not price:
                return Response({"message": "Please, fill all required fields."}, status=status.HTTP_400_BAD_REQUEST)
            data = {
                'name': name,
                'description': description,
                'price': price
            }
            serializer = ProductSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "product created successfully"}, status=status.HTTP_201_CREATED)
        except:
            return Response({"message": "error!"}, status=status.HTTP_400_BAD_REQUEST)