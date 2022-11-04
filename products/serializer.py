from itertools import product
from rest_framework.serializers import ModelSerializer
from products.models import ProductCategory, Product, ProductFile
from users.serializers import FarmerSerializer


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['product_category_name', 'product_category_id',
                  'product_category_description']


class ProductFileSerializer(ModelSerializer):
    class Meta:
        model = ProductFile
        fields = ['product_file_id', 'product_file_name', 'product_file_image']


class ProductSerializer(ModelSerializer):
    class Meta:
        product_category_id = ProductCategorySerializer()
        product_product_file_id = ProductFileSerializer()
        product_farmer_id = FarmerSerializer()
        model = Product
        fields = ['product_name', 'product_price', 'product_location', 'product_description',
                  'product_category_id', 'product_product_file_id', 'product_farmer_id']

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        return product
