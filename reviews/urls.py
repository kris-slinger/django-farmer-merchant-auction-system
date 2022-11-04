from django.urls import path
from reviews.views import ReviewDetailView, ReviewView
urlpatterns = [
    path('', ReviewView.as_view()),
    path('<int:reviewId>/', ReviewDetailView.as_view())

]
