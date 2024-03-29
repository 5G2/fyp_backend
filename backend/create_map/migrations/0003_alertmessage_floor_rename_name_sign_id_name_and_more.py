# Generated by Django 4.2.1 on 2023-08-11 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('create_map', '0002_sensor_battery_sign_battery'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20, null=True)),
                ('level', models.IntegerField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='sign',
            old_name='name',
            new_name='id_name',
        ),
        migrations.RenameField(
            model_name='sign',
            old_name='state',
            new_name='left_sign_state',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='name',
        ),
        migrations.AddField(
            model_name='sensor',
            name='connection',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='sensor',
            name='fire_drill_mode',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sensor',
            name='id_name',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='sensor',
            name='is_critical',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sensor',
            name='is_warning',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sign',
            name='is_warning',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sign',
            name='right_sign_state',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20, null=True)),
                ('floor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='create_map.floor')),
            ],
        ),
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(null=True)),
                ('start_time', models.TimeField(null=True)),
                ('message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='create_map.alertmessage')),
                ('sensor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='create_map.sensor')),
            ],
        ),
        migrations.CreateModel(
            name='Alert_Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('state', models.IntegerField(null=True)),
                ('alert', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='create_map.alerts')),
                ('message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='create_map.alertmessage')),
                ('sensor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='create_map.sensor')),
            ],
        ),
        migrations.AddField(
            model_name='sensor',
            name='floor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='create_map.floor'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='create_map.room'),
        ),
        migrations.AddField(
            model_name='sign',
            name='floor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='create_map.floor'),
        ),
        migrations.AddField(
            model_name='sign',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='create_map.room'),
        ),
    ]
