"""Follow bot, to follow some followers from an account
"""
__date__ = '08/01/2014'
__author__ = '@ismailsunni'

import tweepy
import constants

# constants
consumer_key = constants.consumer_key
consumer_secret = constants.consumer_secret
access_key = constants.access_key
access_secret = constants.access_secret

def need_to_follow(user):
    statuses_count = user.statuses_count
    followers_count = user.followers_count
    friends_count = user.friends_count
    created_at = user.created_at
    # last_status_time = user.status.created_at

    if followers_count > friends_count:
        return True
    else:
        return False


def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    # accounts = ['sarapanhaticom']
    accounts = ['rischanmafrur']
    for account in accounts:
        followers = api.followers(account)
        print followers
        for follower in followers:
            if need_to_follow(follower):
                print follower.screen_name
                try:
                    friend = api.create_friendship(follower.screen_name)
                    if friend.screen_name == follower.screen_name:
                        print 'Follow ' + follower.name + ' success'
                    else:
                        print 'Follow ' + follower.name + ' failed'
                except tweepy.TweepError, e:
                    print e

    print 'benar'

if __name__ == '__main__':
    main()