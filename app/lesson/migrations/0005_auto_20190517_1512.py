# Generated by Django 2.2.1 on 2019-05-17 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0004_auto_20190517_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]
