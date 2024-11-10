# Generated by Django 4.2.16 on 2024-11-09 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('serviceType', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('ServiceProvider', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=100)),
                ('api1', models.CharField(max_length=100)),
                ('api2', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
            ],
            options={
                'db_table': 'service_table',
            },
        ),
    ]
