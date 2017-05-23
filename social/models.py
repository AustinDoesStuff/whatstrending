# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime


class TwitterTrend(models.Model):
    name = models.CharField(max_length=160)
    link = models.CharField(max_length=500)
    date = str(datetime.datetime.now())
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FacebookTrend(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=160)
    date = str(datetime.datetime.now())
    created = models.DateTimeField(auto_now_add=True, default=timezone.now())

    def __str__(self):
        return self.name
