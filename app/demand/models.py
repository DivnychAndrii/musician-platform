from django.contrib.auth import get_user_model
from django.db import models
from main.models import User


class Demand(models.Model):
    from_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user')
    to_creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    title = models.CharField(max_length=255, default='NoTittle')
    content = models.TextField()

    class Meta:
        db_table = 'demand'

    def __str__(self):
        return f'{self.from_user.name} requested a lesson from {self.to_creator} with title {self.title}'

