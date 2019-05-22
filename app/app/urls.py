from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from app import settings
from main.standart_views import HomePage, signup
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
    path('register/', signup, name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]

# api/auth/id
# api/lessons/id

# docs/profile/id
# docs/lessons/id/likes
