# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_c'),
    ]

    operations = [
        migrations.CreateModel(
            name='java',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('videofile', models.FileField(upload_to='files')),
            ],
        ),
    ]
