from django.urls import path
from reviews.views import ReceivedFarmerReviewsView, ReviewDetailView, ReviewRating, ReviewView
urlpatterns = [
    path('', ReviewView.as_view()),
    path('farmer/', ReceivedFarmerReviewsView.as_view()),
    path('<int:reviewId>/', ReviewDetailView.as_view()),
    path('rating/', ReviewRating.as_view())

]
