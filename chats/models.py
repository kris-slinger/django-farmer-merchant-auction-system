from django.db import models
from users.models import CustomUser, Farmer, Merchant


class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    chat_message = models.CharField(max_length=300, blank=True)
    chat_merchant_id = models.ForeignKey(
        Merchant, on_delete=models.CASCADE)
    chat_farmer_id = models.ForeignKey(
        Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.chat_farmer_id} - {self.chat_merchant_id}"
# Create your models here.
