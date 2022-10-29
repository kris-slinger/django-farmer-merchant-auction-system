from itertools import product
from django.contrib import admin

from .models import Product, ProductCategory, ProductFile

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductFile)
# Register your models here.
