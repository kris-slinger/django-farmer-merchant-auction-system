from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from django.http import Http404


class ReviewView(APIView):
    def get(self, request):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReviewSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
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
        query = self.get_object(reviewId)
        return Response(status=status.HTTP_204_NO_CONTENT)
