from django.contrib import admin
from django.urls import path, include
from main import views
from rest_framework.documentation import include_docs_urls

urls = [
    path('auth/', include('main.urls')),
    path('lessons/', include('lesson.urls')),
]
urlpatterns = [
    path('docs/', include_docs_urls(title='docs_urls')),
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
    path('', views.index, name="index"),
]

# api/auth/id
# api/lessons/id

# docs/profile/id
# docs/lessons/id/likes
