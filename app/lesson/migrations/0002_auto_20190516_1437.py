# Generated by Django 2.2.1 on 2019-05-16 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='videofile',
            new_name='video_file',
        ),
    ]
