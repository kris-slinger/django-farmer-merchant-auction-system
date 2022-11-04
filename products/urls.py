from django.urls import path
from products.models import ProductCategory

from products.views import ProductFileView, ProductView

urlpatterns = [
    path('', ProductView.as_view()),
]
