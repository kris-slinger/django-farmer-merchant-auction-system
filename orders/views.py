from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from orders.models import Order

from orders.serializer import OrderSerialier


class OrderView(APIView):
    def get(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerialier(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerialier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

