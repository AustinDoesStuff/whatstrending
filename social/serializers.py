from rest_framework import serializers
from .models import TwitterTrend, FacebookTrend, RedditTrend


class TwitterTrendSerializer(serializers.ModelSerializer):

    class Meta:
        model = TwitterTrend
        fields = '__all__'


class FacebookTrendSerializer(serializers.ModelSerializer):

    class Meta:
        model = FacebookTrend
        fields = '__all__'


class RedditTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedditTrend
        fields = '__all__'