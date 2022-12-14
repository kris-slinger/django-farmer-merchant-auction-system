from itertools import product
from django.db import models
from choices.choices import PRODUCT_CATEGORY_CHOICES
from users.models import Farmer


class ProductCategory(models.Model):
    product_category_id = models.AutoField(primary_key=True)
    product_category_name = models.CharField(
        choices=PRODUCT_CATEGORY_CHOICES, max_length=20)
    product_category_description = models.TextField()

    def __str__(self):
        return f"{self.product_category_name} - {self.product_category_description}"

    class Meta:
        db_table = "ProductCategory"


class ProductFile(models.Model):
    product_file_id = models.AutoField(primary_key=True)
    product_file_name = models.CharField(max_length=200)
    product_file_image = models.ImageField(upload_to="product", blank=True)

    def __str__(self):
        return f"{self.product_file_name}"

    class Meta:
        db_table = "ProductFile"


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=20, decimal_places=2)
    product_location = models.CharField(max_length=100, null=True)
    product_description = models.TextField()
    product_created_at = models.DateField(auto_now_add=True)
    product_category_id = models.OneToOneField(
        ProductCategory, on_delete=models.CASCADE, db_column="product_category_id")
    product_farmer_id = models.ForeignKey(
        Farmer, on_delete=models.CASCADE, db_column="product_farmer_id")

    product_product_file_id = models.OneToOneField(
        ProductFile, on_delete=models.CASCADE, db_column="product_product_file_id")

    class Meta:
        ordering = ['-product_id']
        db_table="Product"

    def __str__(self):
        return f"{self.product_name}-{self.product_farmer_id}"


# Create your models here.
