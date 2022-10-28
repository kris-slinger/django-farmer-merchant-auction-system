from django.db import models
from users.models import CustomUser


class Chat(models.Model):
    chat_id = models.CharField(primary_key=True)
    chat_message = models.CharField(max_length=300, blank=True)
    chat_merchant_user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    chat_farmer_user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
# Create your models here.
