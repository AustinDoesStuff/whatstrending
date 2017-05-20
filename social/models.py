# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TwitterTrend(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    """def findOnTwitter(name):
        if name[0] == "#":
            return "https://social.com/hashtag/%s" % name
        else:
            return "https://social.com/search?q=%s" % name"""


class FacebookTrend(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.name

"""def findOnFacebook(name):
    pass"""
