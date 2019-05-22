from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password', 'avatar')
        extra_kwargs = {'password': {"write_only": True}}


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model
        fields = ('email', 'name', 'password')
        extra_kwargs = {'password': {"write_only": True}}

    def create(self, validated_data):

        user = User(
            email=validated_data['email'],
            name=validated_data['name'])

        user.set_password(validated_data['password'])
        return get_user_model().objects.create_user(user)
