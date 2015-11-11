# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AthlUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('level', models.CharField(max_length=20)),
                ('school', models.CharField(max_length=50)),
                ('coach', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('birthdate', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CoachUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('level', models.CharField(max_length=20)),
                ('school', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('birthdate', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FanUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=30)),
                ('birthdate', models.CharField(max_length=10)),
            ],
        ),
    ]
