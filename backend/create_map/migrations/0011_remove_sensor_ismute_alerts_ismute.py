# Generated by Django 4.2.1 on 2023-10-05 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_map', '0010_sensor_ismute'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='isMute',
        ),
        migrations.AddField(
            model_name='alerts',
            name='isMute',
            field=models.BooleanField(null=True),
        ),
    ]