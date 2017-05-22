import tweepy
import json


#login to twitter

twitterKey = "o5lfqT90lF9eaiXrikXXdw2o0"
twitterSecret = "8HplZfUMPmZ0yHIdtWdLeLy3FWODfyWTuOu6yA55DGEc8dE5YK"
twitterAccessToken = "809565371695034368-WoO437rm0eFuPIRx9LpyE90RTMfU7Dv"
twitterAccessSecret = "QR8GN5yWWcUn7FDvMvrVAX093clDrv1ls41lcoLmvzyj1"

twitterAuth = tweepy.OAuthHandler(twitterKey, twitterSecret)
twitterAuth.set_access_token(twitterAccessToken, twitterAccessSecret)

api = tweepy.API(twitterAuth)


def getTrendingTwitter():
    trends = api.trends_place(23424977)
    return trends


def createTrends():
    trends = getTrendingTwitter()

    for trend in trends[0]['trending']:
        name = trend['name']
        url = trend['url']
