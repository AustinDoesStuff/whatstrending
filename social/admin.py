# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import TwitterTrend, FacebookTrend

admin.site.register(TwitterTrend)
admin.site.register(FacebookTrend)