# Generated by Django 4.2.1 on 2024-03-01 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_first_name_useraccount_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='is_active',
        ),
    ]
