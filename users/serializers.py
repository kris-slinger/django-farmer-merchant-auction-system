from dataclasses import fields
from rest_framework import serializers
from users.models import CustomUser, Farmer, Merchant



# TODO: use a normal serializer here so as to represent your email as user_email etc
class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['user_id', 'email', 'username',
                  'user_national_id', 'user_phone', 'user_role', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class FarmerSerializer(serializers.ModelSerializer):
    farmer_user_id = CustomUserSerializer()

    class Meta:
        model = Farmer
        fields = ['farmer_id', 'farmer_user_id']


class MerchantSerializer(serializers.ModelSerializer):
    model = Merchant
    fields = ['merchant_id', 'merchant_user_id']
