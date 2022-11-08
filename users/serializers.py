from dataclasses import fields
from rest_framework import serializers
from users.models import CustomUser, Merchant, Farmer
from rest_framework.validators import UniqueValidator

class CustomUserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="id", read_only=True)
    user_email = serializers.EmailField(max_length=254, validators=[UniqueValidator(
        queryset=CustomUser.objects.all())], source="email")
    user_name = serializers.CharField(max_length=200, validators=[UniqueValidator(
        queryset=CustomUser.objects.all())], source="username")
    user_password = serializers.CharField(
        max_length=200, write_only=True, source="password")
    class Meta:
        model = CustomUser
        fields = ['user_id', 'user_email', 'user_name',
                  'user_national_id', 'user_phone', 'user_role', 'user_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class FarmerSerializer(serializers.ModelSerializer):
    # farmer_user_id = CustomUserSerializer()

    class Meta:
        model = Farmer
        fields = '__all__'


class MerchantSerializer(serializers.ModelSerializer):
    # merchant_user_id = CustomUserSerializer()

    class Meta:
        model = Merchant
        fields = ['merchant_id', 'merchant_user_id']

    # def get_accounts_items
