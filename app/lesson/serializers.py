from rest_framework import serializers

from main.models import User
from .models import Lessons, Like


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'name',  'avatar')


class LessonSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer()

    class Meta:
        model = Lessons
        fields = ('id', 'tittle', 'content', 'pub_date', 'author')
        read_only_fields = ('id',)


class LikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('lesson_id', 'user',)
        read_only_fields = ('user', 'lesson_id',)
