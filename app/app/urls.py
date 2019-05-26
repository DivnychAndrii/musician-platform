from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from demand.standaart_views import Demand
from lesson.standart_views import AllLessons, OneLesson, CreateLesson
from main.standart_views import HomePage, Register, Login, Profile
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static


urls = [
    path('auth/', include('main.urls')),
    path('', include('lesson.urls'), name="lessons"),
    path('', include('demand.urls'), name='demands'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='docs_urls')),
    path('api/', include(urls)),

    
    path('lessons/', AllLessons.as_view(), name='lessons_list'),
    path('lessons/<int:lesson_id>', OneLesson.as_view(), name='one_lesson'),
    path('lessons/create', CreateLesson.as_view(), name='demand'),
    path('demand/', Demand.as_view(), name='demand'),

    path('', HomePage.as_view(), name='index'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('profile/<int:user_id>/', Profile.as_view(), name='profile'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
