# Generated by Django 3.0.2 on 2020-01-28 16:00

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='static/restaurant')),
                ('description', models.TextField()),
                ('working_hours', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None, verbose_name='Working Hour')),
            ],
        ),
    ]
