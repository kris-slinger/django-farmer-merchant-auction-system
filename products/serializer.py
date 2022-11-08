from itertools import product
from rest_framework import serializers
from products.models import ProductCategory, Product, ProductFile
from users.serializers import FarmerSerializer


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['product_category_id', 'product_category_name', 'product_category_description']


class ProductFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFile
        fields = ['product_file_id', 'product_file_name', 'product_file_image']


class ProductSerializer(serializers.ModelSerializer):
    # product_category_id = ProductCategorySerializer()
    # product_product_file_id = ProductFileSerializer()
    # product_farmer_id = FarmerSerializer()
    product_farmer_name = serializers.ReadOnlyField(source="product_farmer_id.farmer_user_id.username")
    product_category_name=serializers.ReadOnlyField(source="product_category_id.product_category_name")
    product_product_file=serializers.ImageField(source="product_product_file_id.product_file_image")
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'product_price', 'product_location', 'product_description',
                  'product_category_name', 'product_product_file',  'product_farmer_name']

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        return product
