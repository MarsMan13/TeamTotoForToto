# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-05 03:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0019_auto_20180905_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member_info',
            name='callnumber',
        ),
    ]