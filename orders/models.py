from django.db import models

from choices.choices import ORDER_CHOICES
from ..users.models import CustomUser
from ..products.models import Product


class Order(models.Model):
    order_name = models.CharField(max_length=100)
    order_quantity = models.IntegerField()
    order_status = models.CharField(max_length=2, choices=ORDER_CHOICES)
    order_product_total_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True)
    order_creation_date = models.DateField(auto_now_add=True)
    order_expiration_date = models.DateField(blank=True, null=True)
    order_product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_merchant_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

# Create your models here.
