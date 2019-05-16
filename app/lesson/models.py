from django.db import models
<<<<<<< HEAD
from main.models import User


class Lessons(models.Model):

    tittle = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    video_file = models.FileField(upload_to='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
=======
from app.main.models import User


class Lesson(models.Model):


    tittle = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/")
    videofile = models.FileField(upload_to='')
    author = models.ForeignKey(User, on_delete=models.CASCADE))
>>>>>>> 95f7f198ccf9cd0e3ab59508009f3dddf5005089

    class Meta:
        db_table = 'lessons'

    def __str__(self):
        return self.tittle
