# Generated by Django 2.2.1 on 2019-05-17 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0009_lessons_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessons',
            name='grade',
        ),
    ]
