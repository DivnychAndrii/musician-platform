from rest_framework import serializers
from .models import Lessons, Like


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lessons
        fields = ('id', 'tittle', 'lesson_file', 'pub_date', 'author', 'likes')

    def create(self, validated_data):
        """Create a new lesson"""

        lesson = Lessons(
            tittle=validated_data['tittle'],
            lesson_file=validated_data['lesson_file'],
            pub_date=validated_data['pub_date'],
            author=validated_data['author'])
        lesson.save()
        return lesson


class LikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('lesson', 'likes')
