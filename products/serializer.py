from itertools import product
from rest_framework import serializers
from products.models import ProductCategory, Product, ProductFile
from users.serializers import FarmerSerializer


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['product_category_id', 'product_category_name',
                  'product_category_description']


class ProductFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFile
        fields = ['product_file_id', 'product_file_name', 'product_file_image']


class ProductSerializer(serializers.ModelSerializer):
    product_category_data = ProductCategorySerializer(
        source="product_category_id")
    product_product_file_data = ProductFileSerializer(
        source="product_product_file_id")
    product_farmer_name = serializers.ReadOnlyField(
        source="product_farmer_id.farmer_user_id.username")
    product_category_name = serializers.ReadOnlyField(
        source="product_category_id.product_category_name")

    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'product_price', 'product_location', 'product_description',
                  'product_category_name', 'product_farmer_name', 'product_category_data', 'product_product_file_data']

    def create(self, validated_data):
        print(validated_data)
        product_file_data = dict(
            validated_data.pop('product_product_file_id'))
        product_category_data = dict(
            validated_data.pop('product_category_id'))
        product_category_instance = ProductCategory.objects.create(
            **product_category_data)
        product_file_instance = ProductFile.objects.create(**product_file_data)
        print(product_file_instance)
        product = Product.objects.create(**validated_data, product_category_id=product_category_instance,
                                         product_product_file_id=product_file_instance)
        return product


# class ProductMainSerializer(serializers.Serializer):
#     product_category_id = ProductCategorySerializer()
#     product_product_file_id = ProductFileSerializer()
#     product_name = serializers.CharField(max_length=200)
#     product_price = serializers.DecimalField(max_digits=20, decimal_places=2)
#     product_location = serializers.CharField(max_length=200)
#     product_description = serializers.CharField()
# 
#     def create(self, validated_data):
#         product_file_data = dict(
#             validated_data.pop('product_product_file_id'))
#         product_category_data = dict(
#             validated_data.pop('product_category_id'))
#         product_category_instance = ProductCategory.objects.create(
#             **product_category_data)
#         product_file_instance = ProductFile.objects.create(**product_file_data)
#         print(product_file_instance)
#         product = Product.objects.create(**validated_data, product_category_id=product_category_instance,
#                                          product_product_file_id=product_file_instance)
#         return product
