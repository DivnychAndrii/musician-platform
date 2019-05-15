from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('register/', views.register, name='reg'),
    path('logout/', views.logout_view, name='logout'),
]
