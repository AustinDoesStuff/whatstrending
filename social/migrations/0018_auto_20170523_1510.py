# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 20:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0017_auto_20170523_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebooktrend',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 23, 20, 10, 14, 725220, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='twittertrend',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 23, 20, 10, 14, 724421, tzinfo=utc)),
        ),
    ]
