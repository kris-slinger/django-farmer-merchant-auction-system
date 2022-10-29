
from rest_framework_simplejwt.views import TokenObtainPairView

from auth.serializers import MyTokenObtainPairSerializer, RegisterSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    # for simplejwt authentication
    serializer_class = MyTokenObtainPairSerializer


def signUp(request):
    pass
