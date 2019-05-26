from rest_framework import serializers

from main.models import User
from .models import Lessons, Like


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)


class LessonSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Lessons
        fields = ('id', 'tittle', 'content', 'pub_date', 'author', 'image')
        read_only_fields = ('id',)


class LikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('lesson_id', 'user',)
        read_only_fields = ('user', 'lesson_id',)
