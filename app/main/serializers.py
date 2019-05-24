from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password', 'avatar')
        extra_kwargs = {'password': {"write_only": True}}


