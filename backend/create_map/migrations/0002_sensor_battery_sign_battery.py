# Generated by Django 4.2.1 on 2023-06-09 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='battery',
            field=models.IntegerField(default=100, null=True),
        ),
        migrations.AddField(
            model_name='sign',
            name='battery',
            field=models.IntegerField(default=100, null=True),
        ),
    ]
