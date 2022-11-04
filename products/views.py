from django.shortcuts import render
from rest_framework.views import APIView
from products.models import Product, ProductCategory, ProductFile
from products.serializer import ProductCategorySerializer, ProductFileSerializer, ProductSerializer

from rest_framework.response import Response
from rest_framework import status

# TODO: Figure out who will have permission for this view
class ProductCategory(APIView):
    def get(self, request):
        queryset = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductCategorySerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductFileView(APIView):
    def get(self, request):
        queryset = ProductFile.objects.all()
        serializer = ProductFileSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductFileSerializer(data=request.data)
        if serializer.valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

