from django.db import models
from app.main.models import User


class Lesson(models.Model):


    tittle = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/")
    videofile = models.FileField(upload_to='')
    author = models.ForeignKey(User, on_delete=models.CASCADE))

    class Meta:
        db_table = 'lessons'

    def __str__(self):
        return self.tittle
