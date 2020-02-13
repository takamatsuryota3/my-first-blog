# Generated by Django 2.2.10 on 2020-02-13 14:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.AddField(
            model_name='post',
            name='creates_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
