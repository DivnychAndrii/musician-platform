from rest_framework import serializers
from .models import Lessons, Like


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lessons
        fields = ('id', 'tittle', 'lesson_file', 'pub_date', 'author', 'likes')
        read_only_fields = ('id',)


class LikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('lesson', 'user')
        read_only_fields = ('user', 'lesson')
