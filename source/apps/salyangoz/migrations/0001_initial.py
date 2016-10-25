# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('content', models.URLField(max_length=1024, verbose_name='Content')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Time')),
                ('counter', models.IntegerField(default=0, verbose_name='Counter')),
                ('user_name', models.CharField(max_length=100, verbose_name='User Name')),
                ('photo', models.URLField(max_length=1024, verbose_name='Photo')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'verbose_name': 'User',
            },
        ),
    ]
