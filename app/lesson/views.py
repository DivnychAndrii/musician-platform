from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from app.pagination import ResultSetPagination
from lesson.serializers import LikesSerializer
from .permissions import IsGetOrAuthenticated
from . import serializers, models


class LessonViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.LessonSerializer
    queryset = models.Lessons.objects.get_queryset().order_by('id')
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsGetOrAuthenticated,)
    pagination_class = ResultSetPagination
    # renderer_classes = (JSONRenderer, )

    @action(detail=True, methods=['GET'])
    def likes(self, request, pk=None):
        lesson = self.get_object()
        serializer = LikesSerializer(lesson.likes.all(), many=True)
        return Response(serializer.data)


class AllLessons(View):
    template = 'all_lessons.html'

    def get(self, request):
        all_lessons = models.Lessons.objects.all().order_by('-pub_date')
        paginator = Paginator(all_lessons, 20)
        page = request.GET.get('page')
        context = paginator.get_page(page)

        return render(request, self.template, {"context": context})
