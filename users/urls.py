from django.urls import path
from .views import CustomUserView, FarmerView, MerchantView, UserRoleView

urlpatterns = [
    path('', CustomUserView.as_view()),
    path('farmer/', FarmerView.as_view()),
    path('merchant/', MerchantView.as_view()),
    path('role/', UserRoleView.as_view())
]
