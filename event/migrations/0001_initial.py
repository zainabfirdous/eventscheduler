# Generated by Django 4.1.1 on 2022-09-17 21:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('time', models.TimeField(default=datetime.datetime.now)),
                ('venue', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('email', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d')),
            ],
        ),
    ]
