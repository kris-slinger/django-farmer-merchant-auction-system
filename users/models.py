from django.db import models
from choices.choices import USER_ROLES


class CustomUser():
    user_name = models.CharField(verbose_name="username", max_length=100)
    user_national_id = models.IntegerField(max_length=10_000_000)
    user_phone = models.CharField(max_length=100)
    user_email = models.EmailField(verbose_name="username")
    user_password = models.CharField(verbose_name="password")
    user_role = models.CharField(max_length=2, choices=USER_ROLES)
# Create your models here.
