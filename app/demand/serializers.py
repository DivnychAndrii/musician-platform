from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from demand.models import Demand
from main.models import User


class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)
        write_only_fields = ('id',)


class DemandSerializer(ModelSerializer):

    from_user = UserProfileSerializer()
    to_creator = UserProfileSerializer()

    class Meta:
        model = Demand
        fields = ('id', 'from_user', 'title', 'to_creator', 'content')
        read_only_fields = ('id',)

