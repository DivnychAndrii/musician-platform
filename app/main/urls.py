from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
                                    TokenObtainPairView,
                                    TokenRefreshView,)
from . import views

router = DefaultRouter()

router.register(r'', views.UserProfileViewSet, basename='User')

urlpatterns = [
    url(r'^token/$', TokenObtainPairView.as_view(), name='auth'),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='auth-refresh'),
] + router.urls