# Generated by Django 2.2.1 on 2019-05-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0020_auto_20190522_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='likes',
            field=models.PositiveIntegerField(),
        ),
    ]
