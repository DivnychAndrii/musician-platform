# Generated by Django 2.2.1 on 2019-05-25 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0026_auto_20190523_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
