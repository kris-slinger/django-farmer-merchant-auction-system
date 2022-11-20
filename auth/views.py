from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from users.serializers import CustomUserSerializer
from auth.serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework import status


class MyTokenObtainPairView(TokenObtainPairView):
    # for simplejwt authentication
    serializer_class = MyTokenObtainPairSerializer


# class registerUser(APIView):
#     permission_classes = [AllowAny]
# 
#     def post(self, request):
#         serializer = CustomUserSerializer(data=request.data)
#         if serializer.is_valid():
#             userExist = CustomUser.objects.filter(
#                 username=serializer.validated_data['username'])
#             if not userExist:
#                 serializer.save()
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response({"msg": "user created"}, status=status.HTTP_200_OK)
