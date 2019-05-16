from rest_framework import serializers
from .models import Lessons


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lessons
        fields = ('id', 'tittle', 'video_file', 'pub_date', 'author')

    def create(self, validated_data):
        """Create a new lesson"""

        lessons = Lessons(
            tittle=validated_data['tittle'],
            name=validated_data['name'],
            pub_date=validated_data['pub_d  ate'],
            author=validated_data['author'])
        lessons.save()
        return lessons
