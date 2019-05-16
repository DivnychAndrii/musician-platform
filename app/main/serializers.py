from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {"write_only": True}}

    def create(self, validated_data):
        """Create a new user"""

        user = models.User(
            email=validated_data['email'],
            name=validated_data['name'])

        user.set_password(validated_data['password'])
        user.save()
        return user


