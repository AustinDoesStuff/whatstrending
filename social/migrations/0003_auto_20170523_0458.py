# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 04:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20170520_1353'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FacebookTrend',
        ),
        migrations.DeleteModel(
            name='TwitterTrend',
        ),
    ]
