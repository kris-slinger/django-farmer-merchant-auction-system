from itertools import product
from rest_framework import serializers
from products.models import ProductCategory, Product, ProductFile
from users.serializers import FarmerSerializer
from drf_extra_fields.fields import Base64ImageField


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['product_category_id', 'product_category_name',
                  'product_category_description']


class ProductFileSerializer(serializers.ModelSerializer):
    product_file_image = Base64ImageField()

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
    product_farmer_phone = serializers.ReadOnlyField(
        source="product_farmer_id.farmer_user_id.user_phone"
    )

    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'product_price', 'product_farmer_phone', 'product_location', 'product_description', 'product_created_at',
                  'product_farmer_name', 'product_category_data', 'product_product_file_data']

    def create(self, validated_data):
        product_category_instance = ProductCategory.objects.create(
            **dict(validated_data.pop('product_category_id')))
        product_file_instance = ProductFile.objects.create(**dict(
            validated_data.pop('product_product_file_id')))
        product = Product.objects.create(**validated_data, product_category_id=product_category_instance,
                                         product_product_file_id=product_file_instance)
        return product

    def update(self, instance, validated_data):
        ProductCategory.objects.filter(product_category_id=instance.product_category_id.product_category_id).update(
            **dict(validated_data.pop("product_category_id"))
        )
        file_instance = ProductFile.objects.create(
            **dict(validated_data.pop('product_product_file_id'))
        )
        ProductFile.objects.get(
            product_file_id=instance.product_product_file_id.product_file_id).delete()

        instance.product_product_file_id = file_instance
        instance.product_name = validated_data.get(
            'product_name', instance.product_name)
        instance.product_price = validated_data.get(
            'product_price', instance.product_price)
        instance.product_location = validated_data.get(
            'product_location', instance.product_location)
        instance.product_description = validated_data.get(
            'product_description', instance.product_description)
        instance.save()
        return instance
