from django.urls import path

from orders.views import MerchantSenderOrderView, OrderFarmerUpdateStatusView, OrderView, OrderDetailView, FarmerReceiverOrderView
urlpatterns = [
    path('', OrderView.as_view()),
    path('merchant/', MerchantSenderOrderView.as_view()),
    path('farmer/', FarmerReceiverOrderView.as_view()),
    path('<int:orderId>', OrderDetailView.as_view()),
    path('<int:orderId>/farmer/update', OrderFarmerUpdateStatusView.as_view())
]
