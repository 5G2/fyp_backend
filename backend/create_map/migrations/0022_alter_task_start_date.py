# Generated by Django 4.2.1 on 2024-03-16 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_map', '0021_alter_task_create_at_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
