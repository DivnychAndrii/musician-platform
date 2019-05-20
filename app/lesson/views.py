from rest_framework import mixins
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from app.pagination import ResultSetPagination
from lesson import serializers
from lesson.models import Lessons, Like
from lesson.serializers import LikesSerializer
from .permissions import IsGetOrAuthenticated


class LessonViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.LessonSerializer
    queryset = Lessons.objects.get_queryset().order_by('id')
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsGetOrAuthenticated,)
    pagination_class = ResultSetPagination
    # renderer_classes = (JSONRenderer, )


class LikeViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):

    serializer_class = serializers.LikesSerializer
    permission_classes = (IsGetOrAuthenticated,)

    def get_queryset(self):

        return Like.objects.filter(lesson_id=self.kwargs['lesson_id'])

    @action(methods="POST", detail=False)
    def toogle(self, *args, **kwargs):
        lesson = get_object_or_404(Lessons, id=self.kwargs['kwargs_id'])
