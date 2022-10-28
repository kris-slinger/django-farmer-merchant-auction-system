from itertools import product
from django.db import models
from choices.choices import CATEGORY_CHOICES, PRODUCT_FILE_TYPE
from ..users.models import CustomUser


class ProductCategory(models.Model):
    product_category = models.CharField(max_length=100)
    product_category_name = models.CharField(
        choices=CATEGORY_CHOICES, max_length=2)


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=20, decimal_places=2)
    product_location = models.CharField(max_length=100, null=True)
    product_description = models.TextField()
    product_category_id = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE)
    product_farmer_user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)


class ProductFiles(models.Model):
    product_file_id = models.IntegerField(primary_key=True)
    product_file_name = models.CharField(max_length=200)
    product_file_image = models.ImageField(to="product")
    product_file_product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE)

# Create your models here.
