# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 14:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0027_student_teacher'),
    ]

    operations = [
        migrations.DeleteModel(
            name='student',
        ),
        migrations.DeleteModel(
            name='teacher',
        ),
    ]
