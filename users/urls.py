from django.urls import path
from .views import CustomUserView, FarmerView

urlpatterns = [
    path('new/', CustomUserView.as_view()),
    path('farmer/', FarmerView.as_view()),
    # path('farmer/new/', FarmerDetailView.as_view())
]
