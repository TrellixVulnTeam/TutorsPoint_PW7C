# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 07:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0023_auto_20170928_1329'),
    ]

    operations = [
        migrations.DeleteModel(
            name='fileupload',
        ),
    ]
