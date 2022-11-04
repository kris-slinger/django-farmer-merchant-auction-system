from django.db import models

from users.models import CustomUser
from users.models import Farmer, Merchant


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    review_rating = models.IntegerField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    review_message = models.CharField(max_length=300, blank=True)
    review_merchant_id = models.ForeignKey(
        Merchant, on_delete=models.CASCADE)
    review_farmer_id = models.ForeignKey(
        Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review_farmer_id} <-- {self.review_merchant_id}"

