# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FacebookTrend, TwitterTrend, RedditTrend
from .serializers import FacebookTrendSerializer, TwitterTrendSerializer, RedditTrendSerializer
from .helpers import createAllData


class TwitterJsonView(APIView):

    def get(self, request):
        twittertrends = TwitterTrend.objects.all()
        twitterSerializer = TwitterTrendSerializer(twittertrends, many=True)

        return Response(twitterSerializer.data)


class RedditJsonView(APIView):

    def get(self, request):
        reddittrends = RedditTrend.objects.all()
        redditSerializer = RedditTrendSerializer(reddittrends, many=True)

        return Response(redditSerializer.data)


def index(request):
    createAllData()
    latestTweets = TwitterTrend.objects.order_by('-created')[:10]
    latestReddit = RedditTrend.objects.order_by('-created')[:10]
    context = {'latestTweets': latestTweets, 'latestReddit': latestReddit}
    return render(request, 'social/index.html', context)
