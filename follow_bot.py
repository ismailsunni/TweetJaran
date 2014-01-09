"""Follow bot, to follow some followers from an account
"""
__date__ = '08/01/2014'
__author__ = '@ismailsunni'

import tweepy
import constants
from datetime import timedelta, datetime

# constants
consumer_key = constants.consumer_key
consumer_secret = constants.consumer_secret
access_key = constants.access_key
access_secret = constants.access_secret


def is_up2date(last_date, delta_hour=36):
    """
    Return true if last_date is no more than delta_hour. delta_hour is in hour
    """
    delta_hour = timedelta(hours=delta_hour)
    now = datetime.now()
    if now - last_date < delta_hour:
        return True
    return False


def need_to_follow(user):
    """
    Check if user is needed to be followed based on some criteria
    """
    statuses_count = user.statuses_count
    followers_count = user.followers_count
    friends_count = user.friends_count
    # Fyi : you need to check this condition
    if statuses_count > 10 and not user.protected:
        last_status_time = user.status.created_at
        if is_up2date(last_status_time, 36):
            return True

    if followers_count > friends_count:
        return True
    elif statuses_count > 10000:
        return True
    else:
        return False


def test():
    a = datetime.now()
    print is_up2date(a)


def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    accounts = ['SMASHindonesia',
                'Poconggg',
                'coboyjr',
                'JKT48FC',
                'EtudeHouseIndo']
    for account in accounts:
        print '### From follower of ', account
        try:
            followers = api.followers(account)
            for follower in followers:
                if need_to_follow(follower):
                    print follower.screen_name
                    try:
                        friend = api.create_friendship(follower.screen_name)
                        if friend.screen_name == follower.screen_name:
                            print 'Follow ' + follower.screen_name + ' success'
                        else:
                            print 'Follow ' + follower.screen_name + ' failed'
                    except tweepy.TweepError, e:
                        print e
        except e:
            print e
    print 'fin'

if __name__ == '__main__':
    main()
    # test()