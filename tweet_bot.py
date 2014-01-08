"""Tweet Bot, for tweeting random tweet
"""
__date__ = '08/01/2014'
__author__ = '@ismailsunni'


import tweepy
import constants

# constant
consumer_key = constants.consumer_key
consumer_secret = constants.consumer_secret
access_key = constants.access_key
access_secret = constants.access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# print api.me().name
# print api.me()
api.update_status('Sedang gundah apa hari ini?')