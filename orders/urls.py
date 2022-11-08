from django.urls import path

from orders.views import OrderView, OrderDetailView
urlpatterns = [
    path('', OrderView.as_view()),
    path('<int:orderId>', OrderDetailView.as_view())
]
