from pyexpat import model
from rest_framework import serializers
from orders.models import Order
from products.serializer import ProductSerializer
from users.serializers import MerchantSerializer


class OrderSerialier(serializers.ModelSerializer):
    # order_product_id = ProductSerializer()
    # order_merchant_id = MerchantSerializer()

    class Meta:
        model = Order
        fields = '__all__'