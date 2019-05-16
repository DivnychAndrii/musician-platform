from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_api/', include('main.urls')),
    path('lessons_api/', include('lesson.urls')),
    path('', views.index, name="index"),
]
