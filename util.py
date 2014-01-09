"""Some utilities functions
"""
__author__ = '@ismailsunni'
__project_name = 'TweetJaran'
__filename = 'util.py'
__date__ = '09/01/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from datetime import datetime, timedelta
import tweepy

def is_up2date(last_date, delta_hour=36):
    """
    Return true if last_date is no more than delta_hour. delta_hour is in hour
    """
    delta_hour = timedelta(hours=delta_hour)
    now = datetime.now()
    if now - last_date < delta_hour:
        return True
    return False

def is_good_account(user):
    """
    Check if user is good (not bot and active)
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

def setup_api(consumer_key, consumer_secret, access_key, access_secret):
    """
    setup api
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    return api