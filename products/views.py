from django.shortcuts import render
from rest_framework.views import APIView
from products.models import Product, ProductCategory, ProductFile
from products.serializer import ProductCategorySerializer, ProductFileSerializer, ProductSerializer

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
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


class ProductFileDetailView(APIView):
    def get_object(self, pk):
        try:
            ProductFile.objects.get(pk)
        except ProductFile.DoesNotExist:
            raise Http404

    def get(self, request, productFileId):
        query = self.get_object(productFileId)
        serializer = ProductFileSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, productFileId):
        query = self.get_object(productFileId)
        serializer = ProductFileSerializer(query, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, productFileId):
        query = self.get_object(productFileId)
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class ProductDetailView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(product_id=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, productId):
        query = self.get_object(productId)
        print(query)
        serializer = ProductSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, productId):
        query = self.get_object(productId)
        serializer = ProductSerializer(query, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, productId):
        query = self.get_object(productId)
        return Response(status=status.HTTP_204_NO_CONTENT)
