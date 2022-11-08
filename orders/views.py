from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from orders.models import Order
from orders.models import Merchant
from orders.serializer import OrderSerializer
from permissions.permissions import IsMerchantOrReadOnly
from rest_framework.permissions import IsAuthenticated
class OrderView(APIView):
    permission_classes = [IsAuthenticated, IsMerchantOrReadOnly]
    def get(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            merchant_instance = Merchant.objects.get(merchant_user_id=request.user)
            serializer.save(order_merchant_id=merchant_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(APIView):
    permission_classes = [IsAuthenticated, IsMerchantOrReadOnly]
    def get_object(self, pk):
        try:
            return Order.objects.get(order_id=pk)
        except Order.DoesNotExist:
            raise Http404
    def get(self,request,orderId):
        query = self.get_object(orderId)
        serializer = OrderSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,orderId):
        query=self.get_object(orderId)
        serializer=OrderSerializer(query,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,orderId):
        query=self.get_object(orderId).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

