from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register(r'', views.UserProfileViewSet)

urlpatterns = [
    url(r'^token/$', TokenObtainPairView.as_view(), name='auth'),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='auth-refresh'),
] + router.urls
