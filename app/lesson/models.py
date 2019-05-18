from django.db import models
from main.models import User, UserManager


class Lessons(models.Model):

    tittle = models.CharField(max_length=50)
    pub_date = models.DateField()
    lesson_file = models.FileField(upload_to='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, through='like', related_name="likes")

    objects = UserManager()

    class Meta:
        db_table = 'lessons'

    def __str__(self):
        return self.tittle


class Like(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_liked = models.BooleanField(default=True)

    objects = UserManager()

    class Meta:
        db_table = "likes"
