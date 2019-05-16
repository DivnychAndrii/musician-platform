from django.shortcuts import render
from rest_framework import viewsets, status
from . import serializers, models


class LessonViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.LessonSerializer
    queryset = models.Lessons.objects.all()
