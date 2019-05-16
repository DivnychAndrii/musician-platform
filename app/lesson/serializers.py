from rest_framework import serializers
from app.main.models import User
from .models import Lesson


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name')
        read_only_fields = ('id',)
        write_only_fields = ('password',)


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'lesson', 'author')