from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import IsGetOrAuthenticated
from . import serializers, models


class LessonViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.LessonSerializer
    queryset = models.Lessons.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsGetOrAuthenticated,)
