# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 19:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0013_auto_20170523_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebooktrend',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 5, 23, 14, 56, 21, 942675)),
        ),
        migrations.AlterField(
            model_name='twittertrend',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 5, 23, 14, 56, 21, 942675)),
        ),
    ]