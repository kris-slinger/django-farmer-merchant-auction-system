from rest_framework.views import APIView

from users.models import CustomUser, Farmer, Merchant
from users.serializers import CustomUserSerializer, FarmerSerializer, MerchantSerializer
from rest_framework.response import Response
from rest_framework import status


class CustomUserView(APIView):
    def get(self, request):
        queryset = CustomUser.objects.all()
        serializer = CustomUserSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            customUser = serializer.save()
            if serializer.validated_data['user_role'] == 'Fm':
                Farmer(farmer_user_id=customUser).save()
            elif serializer.validated_data['user_role'] == 'Mt':
                Merchant(merchant_user_id=customUser).save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FarmerView(APIView):
    def get(self, request):
        queryset = Farmer.objects.all()
        serializer = FarmerSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class MerchantView(APIView):
    def get(self, request):
        queryset = Merchant.objects.all()
        serializer = MerchantSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
