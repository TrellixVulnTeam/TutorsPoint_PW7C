# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 04:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0012_auto_20171012_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Course'),
        ),
    ]
