# Generated by Django 4.2.1 on 2024-03-12 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_useraccount_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='gender',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='phone',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
