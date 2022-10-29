from django.urls import path
from auth.views import MyTokenObtainPairView, signUp
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', signUp, name="sign-up")
]
