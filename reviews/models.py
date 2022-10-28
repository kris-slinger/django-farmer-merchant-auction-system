from django.db import models

from ..users.models import CustomUser


class Reviews(models.Model):
    review_id = models.CharField(primary_key=True)
    review_rating = models.IntegerField(choices=[0, 1, 2, 3, 4, 5])
    review_message = models.CharField(max_length=300, blank=True)
    review_merchant_user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    review_farmer_user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
# Create your models here.
