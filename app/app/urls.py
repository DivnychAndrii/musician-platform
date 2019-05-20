from django.contrib import admin
from django.urls import path, include

from lesson.views import AllLessons
from main.views import HomePage, Register
from rest_framework.documentation import include_docs_urls


urls = [
    path('auth/', include('main.urls')),
    path('lessons/', include('lesson.urls'), name="lessons"),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='docs_urls')),
    path('api/', include(urls)),
    path('', HomePage.as_view(), name='index'),
    path('register/', Register.as_view(), name='register'),
    path('all_lessons/', AllLessons.as_view(), name='all_Lessons'),
]

# api/auth/id
# api/lessons/id

# docs/profile/id
# docs/lessons/id/likes
