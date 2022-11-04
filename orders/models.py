from django.db import models

from choices.choices import ORDER_STATUS_CHOICES
from users.models import Farmer
from products.models import Product


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_name = models.CharField(max_length=100)
    order_quantity = models.IntegerField()
    order_status = models.CharField(max_length=2, choices=ORDER_STATUS_CHOICES)
    order_product_total_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True)
    order_creation_date = models.DateField(auto_now_add=True)
    order_expiration_date = models.DateField(blank=True, null=True)
    order_product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_merchant_id = models.ForeignKey(
        Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_name
# Create your models here.
