# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0007_auto_20170609_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=150)),
            ],
        ),
    ]
