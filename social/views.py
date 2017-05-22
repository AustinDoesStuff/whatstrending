# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FacebookTrend, TwitterTrend
from .serializers import FacebookTrendSerializer, TwitterTrendSerializer
import tweepy


class JsonView(APIView):

    def get(self, request):
        fbtrends = FacebookTrend.objects.all()
        twittertrends = TwitterTrend.objects.all()
        fbSerializer = FacebookTrendSerializer(fbtrends, many=True)
        twitterSerializer = TwitterTrendSerializer(twittertrends, many=True)

        return Response(fbSerializer.data)


    def post(self):
        pass



