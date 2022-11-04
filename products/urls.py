from django.urls import path
from products.models import ProductCategory

from products.views import ProductDetailView, ProductFileDetailView, ProductFileView, ProductView

urlpatterns = [
    path('', ProductView.as_view()),
    path('<int:productId>', ProductDetailView.as_view()),
    path('productFile/<int:productFileId>', ProductFileDetailView.as_view()),
]
