from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from app.pagination import ResultSetPagination
from .permissions import IsGetOrAuthenticated
from . import serializers, models


class LessonViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.LessonSerializer
    queryset = models.Lessons.objects.get_queryset().order_by('id')
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsGetOrAuthenticated,)
    pagination_class = ResultSetPagination


class LikesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LikesSerializer
    queryset = models.Like.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsGetOrAuthenticated,)
    pagination_class = ResultSetPagination
