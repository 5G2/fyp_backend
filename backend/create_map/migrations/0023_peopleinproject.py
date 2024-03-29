# Generated by Django 4.2.1 on 2024-03-17 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('create_map', '0022_alter_task_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleInProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='create_map.project')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
