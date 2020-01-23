# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:37:01 2019

@author: Sai Siddhanth
"""
import tweepy
from textblob import TextBlob


consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Hello')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)






