# myapp/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Building
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ['image_url', 'building_name', 'street', 'city', 'area', 'zipcode']