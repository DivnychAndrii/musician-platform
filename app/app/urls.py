from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='reg')(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.register, name='reg')(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.index),
    path('register/', views.register, name='reg'),
    path('logout/', views.logout_view, name='logout'),
]
