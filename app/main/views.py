from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsGetOrAuthenticated
from . import serializers, models


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsGetOrAuthenticated,)


def index(request):

    return render(request, 'index.html')
