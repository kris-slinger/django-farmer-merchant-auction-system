from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg

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
            merchant_instance = Merchant.objects.get(
                merchant_user_id=request.user)
            print(merchant_instance)
            serializer.save(review_merchant_id=merchant_instance)

            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewRating(APIView):
    def get(self, request):
        reviewAverage = Review.objects.aggregate(
            rating=Avg('review_rating'))
        if reviewAverage['rating'] == None:
            return Response({'rating': 5}, status=status.HTTP_200_OK)
        return Response({'rating': int(reviewAverage['rating'])}, status=status.HTTP_200_OK)


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


class ReceivedFarmerReviewsView(APIView):
    def get(self, request):
        query = Review.objects.filter(
            review_product_id__product_farmer_id__farmer_user_id=request.user)
        serializer = ReviewSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
