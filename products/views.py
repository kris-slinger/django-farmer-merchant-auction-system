from multiprocessing import context
from django.shortcuts import render
from rest_framework.views import APIView
from products.models import Product, ProductCategory, ProductFile
from products.serializer import ProductCategorySerializer, ProductFileSerializer, ProductSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from permissions.permissions import IsFarmerOrReadOnly
from users.models import Farmer


class ProductCategoryView(APIView):
    permission_classes = [IsAuthenticated, IsFarmerOrReadOnly]

    def get(self, request):
        queryset = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductFileView(APIView):
    permission_classes = [IsAuthenticated, IsFarmerOrReadOnly]

    def get(self, request):
        queryset = ProductFile.objects.all()
        serializer = ProductFileSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductFileDetailView(APIView):
    permission_classes = [IsAuthenticated, IsFarmerOrReadOnly]

    def get_object(self, pk):
        try:
            return ProductFile.objects.get(product_file_id=pk)
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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, productFileId):
        query = self.get_object(productFileId).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductView(APIView):
    permission_classes = [IsAuthenticated, IsFarmerOrReadOnly]

    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.is_valid())
            farmer_instance = Farmer.objects.get(farmer_user_id=request.user)
            serializer.save(product_farmer_id=farmer_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated, IsFarmerOrReadOnly]

    def get_object(self, pk):
        try:
            return Product.objects.get(product_id=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, productId):
        query = self.get_object(productId)
        serializer = ProductSerializer(query, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, productId):
        # print(request.data)
        query = self.get_object(productId)
        serializer = ProductSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, productId):
        query = self.get_object(productId).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FarmerSpecificProductView(APIView):
    def get(self, request):
        query = Product.objects.filter(
            product_farmer_id__farmer_user_id=request.user)
        serializer = ProductSerializer(
            query, many=True, context={'request': request})
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
