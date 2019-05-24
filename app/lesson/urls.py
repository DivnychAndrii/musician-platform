from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from lesson.standart_views import AllLessons
from . import views

router = DefaultRouter()
like_router = DefaultRouter()

router.register('lessons', views.LessonViewSet, basename='lessons')
like_router.register('likes', views.LikeViewSet, basename='likes')

urlpatterns = [
    path('', include(router.urls)),
    path('lessons/<lesson_id>/', include(like_router.urls)),
]
