from rest_framework import serializers
from reviews.models import Review
from users.serializers import FarmerSerializer


class ReviewSerializer(serializers.ModelSerializer):
    receiver=serializers.ReadOnlyField(source="review_farmer_id.farmer_user_id.username")
    sender=serializers.ReadOnlyField(source="review_merchant_id.merchant_user_id.username")
    class Meta:
        model = Review
        fields = ['review_id','review_message','review_rating','sender','receiver','review_farmer_id']
