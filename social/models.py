# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TwitterTrend(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.name



class FacebookTrend(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.name
