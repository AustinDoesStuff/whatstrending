import tweepy
import praw
from .models import TwitterTrend, FacebookTrend, RedditTrend


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


def makeNameFriendly(name):
    if name[0] == "#":
        return name[1:]
    else:
        return name.replace(" ", "")


def createTwitterData():
    trends = getTrendingTwitter()
    count = 0
    for trend in trends[0]['trends']:
        name = trend['name']
        link = trend['url']
        friendlyName = makeNameFriendly(name)
        friendlyName = TwitterTrend(name=name, link=link)
        friendlyName.save()
        count += 1
        if count == 10:
            break


def createRedditData():
    reddit = praw.Reddit(user_agent='Whats Trending (by /u/NOB0DYx)',
                         client_id='zVLHSJJwjiqfhg',
                         client_secret="s8HlmR6SDDjCJwO1KLMxEsyTa5U",
                         username='NOB0DYx',
                         password='4643937a',
                         read_only=True)

    for submission in reddit.subreddit('all').hot(limit=10):
        newSubmission = RedditTrend(name=submission.title,
                                    link=submission.url,
                                    user=submission.author)

        newSubmission.save()


def createAllData():
    createTwitterData()
    createRedditData()