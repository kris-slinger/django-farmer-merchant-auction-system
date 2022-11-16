from email.policy import default
from django.db import models

from choices.choices import ORDER_STATUS_CHOICES
from users.models import Merchant
from products.models import Product


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_name = models.CharField(max_length=100, null=True)
    order_quantity = models.IntegerField(default=1)
    order_price = models.DecimalField(
        max_digits=8, decimal_places=2)
    order_status = models.CharField(
        max_length=10, choices=ORDER_STATUS_CHOICES, default="pending")
    order_total_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    order_creation_date = models.DateField(auto_now_add=True)
    order_expiration_date = models.DateField(blank=True, null=True)
    order_product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_merchant_id = models.ForeignKey(
        Merchant, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["-order_id"]
    def __str__(self):
        return self.order_name
