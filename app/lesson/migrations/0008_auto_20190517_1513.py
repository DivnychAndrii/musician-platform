# Generated by Django 2.2.1 on 2019-05-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0007_auto_20190517_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='pub_date',
            field=models.DateField(),
        ),
    ]