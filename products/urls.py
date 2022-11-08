from django.urls import path

from products.views import ProductDetailView, ProductFileDetailView, ProductFileView, ProductView,ProductCategoryView

urlpatterns = [
    path('', ProductView.as_view()),
    path('<int:productId>', ProductDetailView.as_view()),
    path('product-category/', ProductCategoryView.as_view()),
    path('product-file/', ProductFileView.as_view()),
    path('product-file/<int:productFileId>', ProductFileDetailView.as_view()),
]
