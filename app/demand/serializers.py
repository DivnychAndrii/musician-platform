from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from demand.models import Demand
from main.models import User


class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('name',)
        write_only_fields = ('id',)


class DemandSerializer(ModelSerializer):
    from_user = serializers.SlugRelatedField(slug_field='email', queryset=User.objects.all())
    to_creator = serializers.SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Demand
        fields = ('id', 'from_user', 'title', 'to_creator', 'content')
        read_only_fields = ('id',)
