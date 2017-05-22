# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FacebookTrend, TwitterTrend
from .serializers import FacebookTrendSerializer, TwitterTrendSerializer
from .helpers import getTrendingTwitter, createTwitterData


class JsonView(APIView):

    def get(self, request):
        fbtrends = FacebookTrend.objects.all()
        twittertrends = TwitterTrend.objects.all()
        fbSerializer = FacebookTrendSerializer(fbtrends, many=True)
        twitterSerializer = TwitterTrendSerializer(twittertrends, many=True)

        return Response(fbSerializer.data)


    def post(self):
        pass


class IndexView(generic.ListView):
    createTwitterData()

    template_name = "social/index.html"
    context_object_name = 'latestTweets'

    def get_queryset(self):
        return TwitterTrend.objects.order_by('-created')[:10]