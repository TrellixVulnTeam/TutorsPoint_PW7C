# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_auto_20171006_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
