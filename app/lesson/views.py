from django.shortcuts import render
<<<<<<< HEAD
from rest_framework import viewsets, status
from . import serializers, models


class LessonViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.LessonSerializer
    queryset = models.Lessons.objects.all()
=======

class ArticleAPIView(APIView):

    def get(self, *args, **kwargs):
        pass
>>>>>>> 95f7f198ccf9cd0e3ab59508009f3dddf5005089
