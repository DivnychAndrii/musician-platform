from django.shortcuts import render
from rest_framework import viewsets
from . import serializers, models


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.objects.all()


def index(request):

    return render(request, 'index.html')
