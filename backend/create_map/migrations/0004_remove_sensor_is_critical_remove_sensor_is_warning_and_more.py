# Generated by Django 4.2.1 on 2023-08-11 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_map', '0003_alertmessage_floor_rename_name_sign_id_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='is_critical',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='is_warning',
        ),
        migrations.RemoveField(
            model_name='sign',
            name='is_warning',
        ),
        migrations.AddField(
            model_name='sensor',
            name='state',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sign',
            name='state',
            field=models.IntegerField(null=True),
        ),
    ]
