# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 15:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0016_auto_20170927_2128'),
    ]

    operations = [
        migrations.DeleteModel(
            name='member1',
        ),
        migrations.RemoveField(
            model_name='member',
            name='pic',
        ),
    ]
