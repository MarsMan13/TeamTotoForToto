# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-05 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0014_auto_20180905_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_info',
            name='callnumber',
            field=models.IntegerField(default=0),
        ),
    ]
