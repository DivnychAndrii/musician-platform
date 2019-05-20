from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from demand.models import Demand


class DemandSerializer(ModelSerializer):

    creator = get_user_model()

    class Meta:
        model = Demand
        fields = ('id', 'from_user', 'to_creator', 'content')
        read_only_fields = ('id',)
