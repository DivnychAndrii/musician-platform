from django.contrib.auth import get_user_model
from django.db import models
from main.models import User


class Lessons(models.Model):

    tittle = models.CharField(max_length=50)
    pub_date = models.DateField(auto_now=True)
    lesson_file = models.ImageField(upload_to='images/', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'lessons'

    def __str__(self):
        return self.tittle


class Like(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "likes"

    def __str__(self):
        return 'Liked'
