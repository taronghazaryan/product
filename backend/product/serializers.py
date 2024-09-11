from rest_framework import serializers
from rest_framework.response import Response

from rest_framework import status

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
     class Meta:
         model = Product
         fields = ['pk', 'name', 'description', 'price', 'created_at', 'updated_at']

     def validate(self, data):
         name = data['name']
         description = data['description']
         price = data['price']

         if not name:
             return Response({"error": "This field is required"}, status=status.HTTP_400_BAD_REQUEST)
         if not description:
             return Response({"error": "This field is required"}, status=status.HTTP_400_BAD_REQUEST)
         if price <= 0:
             return Response({"error": "The price must be a positive number"}, status=status.HTTP_400_BAD_REQUEST)
         return data

     def create(self, validated_data):
         product = Product.objects.create(
             name=validated_data['name'],
             description=validated_data['description'],
             price=validated_data['price']
         )
         return product


