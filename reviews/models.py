from random import choices
from django.db import models

from users.models import CustomUser
from users.models import Farmer, Merchant
from products.models import Product


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    review_message = models.CharField(max_length=300, blank=True)
    review_rating = models.IntegerField(
        choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    )
    review_created_at = models.DateField(auto_now_add=True)
    review_merchant_id = models.ForeignKey(
        Merchant, on_delete=models.CASCADE)
    review_product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-review_id"]

    def __str__(self):
        return f"{self.review_product_id} <-- {self.review_merchant_id}"
