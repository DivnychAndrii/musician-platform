from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from app import settings
from lesson.standart_views import AllLessons
from main.standart_views import HomePage, Register, Login
from rest_framework.documentation import include_docs_urls


urls = [
    path('auth/', include('main.urls')),
    path('', include('lesson.urls'), name="lessons"),
    path('', include('demand.urls'), name='demands'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='docs_urls')),
    path('api/', include(urls)),
    path('', HomePage.as_view(), name='index'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('lessons/', AllLessons.as_view(), name='lessons_list'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]

