"""Retweet some followers/friends' tweets
"""
__author__ = '@ismailsunni'
__project_name = 'TweetJaran'
__filename = 'retweet_bot'
__date__ = '09/01/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

import constants
from util import setup_api, is_good_account

# constants
consumer_key = constants.consumer_key
consumer_secret = constants.consumer_secret
access_key = constants.access_key
access_secret = constants.access_secret

def is_good_status(follower):
    """
    Check if the last status is good
    """
    last_status = follower.status
    tweet_text = last_status.text
    print tweet_text
    if '@' in tweet_text:
        return False
    return False

def retweet(follower):
    pass

def main():
    api = setup_api(consumer_key, consumer_secret, access_key, access_secret)

    # get followers
    followers = api.followers('santapanhaticom')
    print len(followers)
    for follower in followers:
        if is_good_account(follower):
            print follower.name
            retweet(follower)

if __name__ == '__main__':
    main()