from rest_framework import serializers
<<<<<<< HEAD
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
=======
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
>>>>>>> 95f7f198ccf9cd0e3ab59508009f3dddf5005089
