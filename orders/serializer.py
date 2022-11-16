from rest_framework import serializers
from orders.models import Order
from products.serializer import ProductSerializer
from users.serializers import MerchantSerializer


# TODO: calculate order_total_price,order_expiration_date using a signal

class OrderSerializer(serializers.ModelSerializer):
    order_merchant_name = serializers.ReadOnlyField(
        source="order_merchant_id.merchant_user_id.username")
    order_merchant_phone = serializers.ReadOnlyField(
        source="order_merchant_id.merchant_user_id.user_phone")
    order_total_price = serializers.ReadOnlyField()
    order_expiration_date = serializers.ReadOnlyField()
    order_name = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ['order_id', 'order_name', 'order_quantity', 'order_price', 'order_status', 'order_total_price', 'order_total_price',
                  'order_creation_date', 'order_product_id', 'order_expiration_date', 'order_merchant_name', 'order_merchant_phone']