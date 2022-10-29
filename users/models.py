from django.db import models
from django.contrib.auth.models import AbstractUser
from choices.choices import USER_ROLES


'''
Django abstract user contains username,email and password fields. 
This is why they have not been included in the Custom user model.
'''


class CustomUser(AbstractUser):
    user_id = models.AutoField(primary_key=True)

    user_national_id = models.IntegerField(default=0)
    user_phone = models.CharField(max_length=100, default=" ")
    user_role = models.CharField(
        max_length=2, choices=USER_ROLES, blank=True)


class Farmer(models.Model):
    farmer_id = models.AutoField(primary_key=True)
    user_farmer_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_farmer_id.username


class Merchant(models.Model):
    farmer_id = models.AutoField(primary_key=True)
    user_merchant_id = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_merchant_id.username
