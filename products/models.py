from itertools import product
from django.db import models
from choices.choices import PRODUCT_CATEGORY_CHOICES
from users.models import Farmer


class ProductCategory(models.Model):
    product_category_id = models.AutoField(primary_key=True)
    product_category_name = models.CharField(
        choices=PRODUCT_CATEGORY_CHOICES, max_length=2)
    product_category_description = models.TextField()

    def __str__(self):
        return f"{self.product_category_name} - {self.product_category_description}"


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=20, decimal_places=2)
    product_location = models.CharField(max_length=100, null=True)
    product_description = models.TextField()
    product_category_id = models.OneToOneField(
        ProductCategory, on_delete=models.CASCADE)
    product_user_farmer_id = models.ForeignKey(
        Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name}-{self.product_user_farmer_id}"


class ProductFile(models.Model):
    product_file_id = models.AutoField(primary_key=True)
    product_file_name = models.CharField(max_length=200)
    product_file_image = models.ImageField(upload_to="product")
    product_file_product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_file_name}-{self.product_file_product_id}"


# Create your models here.
