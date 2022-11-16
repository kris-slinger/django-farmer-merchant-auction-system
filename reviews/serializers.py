from rest_framework import serializers
from reviews.models import Review
from users.serializers import FarmerSerializer


class ReviewSerializer(serializers.ModelSerializer):
    review_receiver = serializers.ReadOnlyField(
        source="review_farmer_id.farmer_user_id.username")
    review_sender = serializers.ReadOnlyField(
        source="review_merchant_id.merchant_user_id.username")

    class Meta:
        model = Review
        fields = ['review_id', 'review_message', 'review_rating', 'review_created_at',
                  'review_sender', 'review_receiver', 'review_product_id']
