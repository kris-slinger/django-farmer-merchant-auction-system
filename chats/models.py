from django.db import models
from users.models import CustomUser, Farmer, Merchant


class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    chat_message = models.CharField(max_length=300, blank=True)
    chat_user_merchant_id = models.ForeignKey(
        Merchant, on_delete=models.CASCADE)
    chat_user_farmer_id = models.ForeignKey(
        Farmer, on_delete=models.CASCADE)
# Create your models here.
