from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
>>>>>>> 95f7f198ccf9cd0e3ab59508009f3dddf5005089
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('user_api/', include('main.urls')),
    path('lessons_api/', include('lesson.urls')),
    path('', views.index, name="index"),
=======
    path('register/', views.register, name='reg')(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.register, name='reg')(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.index),
    path('register/', views.register, name='reg'),
    path('logout/', views.logout_view, name='logout'),
>>>>>>> 95f7f198ccf9cd0e3ab59508009f3dddf5005089
]
