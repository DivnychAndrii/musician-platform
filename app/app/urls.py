from django.contrib import admin
from django.urls import path, include
from main import views

urls = [
    path('auth/', include('main.urls')),
    path('lessons/', include('lesson.urls')),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
    path('', views.index, name="index"),
]
