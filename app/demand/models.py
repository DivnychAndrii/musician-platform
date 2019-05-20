from django.db import models

from main.models import User


class Demand(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    to_creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    content = models.TextField()

    class Meta:
        db_table = 'demand'

