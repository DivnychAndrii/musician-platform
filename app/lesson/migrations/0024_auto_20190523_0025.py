# Generated by Django 2.2.1 on 2019-05-22 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0023_auto_20190522_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lesson.Lessons'),
        ),
    ]
