# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mongoengine import Document, fields


class TwitterTrend(Document):
    name = fields.StringField(max_length=160)
    link = fields.StringField(max_length=500)
    created = fields.DateTimeField()

    def __str__(self):
        return self.name



class FacebookTrend(Document):
    name = fields.StringField(max_length=50)
    link = fields.StringField(max_length=160)
    created = fields.DateTimeField()

    def __str__(self):
        return self.name
