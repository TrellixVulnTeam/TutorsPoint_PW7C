# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0019_auto_20170927_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='pic',
            field=models.FileField(upload_to=''),
        ),
    ]
