from rest_framework import serializers
from .models import Lessons


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lessons
        fields = ('id', 'tittle', 'video_file', 'pub_date', 'author')

    def create(self, validated_data):
        """Create a new lesson"""

        lesson = Lessons(
            tittle=validated_data['tittle'],
            video_file=validated_data['video_file'],
            pub_date=validated_data['pub_date'],
            author=validated_data['author'])
        lesson.save()
        return lesson
