from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from permissions.permissions import IsMerchantOrReadOnly
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from django.http import Http404

from users.models import Merchant


class ReviewView(APIView):
    permission_classes = [IsAuthenticated, IsMerchantOrReadOnly]
    def get(self, request):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReviewSerializer(
            data=request.data)
        if serializer.is_valid():
            merchant_instance=Merchant.objects.get(merchant_user_id=request.user)
            serializer.save(review_merchant_id=merchant_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailView(APIView):
    def get_object(self, reviewId):
        try:
            return Review.objects.get(review_id=reviewId)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, reviewId):
        query = self.get_object(reviewId)
        print(query)
        serializer = ReviewSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, reviewId):
        query = self.get_object(reviewId)
        serializer = ReviewSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, reviewId):
        query = self.get_object(reviewId).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
