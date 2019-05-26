from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
                                    TokenObtainPairView,
                                    TokenRefreshView,)

from main.views import FileUploadView
from . import views

router = DefaultRouter()

router.register(r'', views.UserProfileViewSet, basename='User')

urlpatterns = [
    path('<int:user_id>/upload_file', FileUploadView.as_view(), name='avatar_upload'),
    url(r'^token/$', TokenObtainPairView.as_view(), name='auth'),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='auth-refresh'),
] + router.urls
