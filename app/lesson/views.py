from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from app.pagination import ResultSetPagination
from lesson.models import Lessons, Like
from lesson.serializers import LessonSerializer, LikesSerializer
from .permissions import IsGetOrAuthenticated


class LessonViewSet(viewsets.ModelViewSet):

    serializer_class = LessonSerializer
    queryset = Lessons.objects.get_queryset().order_by('id')
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsGetOrAuthenticated,)
    pagination_class = ResultSetPagination
    # renderer_classes = (JSONRenderer, )


class LikeViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):

    serializer_class = LikesSerializer
    permission_classes = (IsGetOrAuthenticated,)
    pagination_class = ResultSetPagination

    def get_lesson_or_404(self):
        return get_object_or_404(Lessons, id=self.kwargs['lesson_id'])

    def get_queryset(self):
        lesson = self.get_lesson_or_404()
        return Like.objects.filter(lesson=lesson)

    @action(methods="POST", detail=False)
    def toggle(self, *_args, **_kwargs):
        lesson = get_object_or_404(queryset=Lessons.objects.filter(lesson_id=self.kwargs['lesson_id']))
        like, liked = Like.objects.get_or_create(user=self.request.user, lesson=lesson)

        if not liked:
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(LikesSerializer(like).data, status.HTTP_201_CREATED)



