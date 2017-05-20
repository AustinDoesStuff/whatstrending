from rest_framework import serializers
from .models import TwitterTrend, FacebookTrend


class TwitterTrendSerializer(serializers.ModelSerializer):

    class Meta:
        model = TwitterTrend
        fields = '__all__'

