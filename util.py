"""Some utilities functions
"""
__author__ = '@ismailsunni'
__project_name = 'TweetJaran'
__filename = 'util.py'
__date__ = '09/01/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from datetime import datetime, timedelta
from random import randint
import tweepy

# constants
import constants
test_consumer_key = constants.consumer_key
test_consumer_secret = constants.consumer_secret
test_access_key = constants.access_key
test_access_secret = constants.access_secret


def read_list(file_path):
    """Read a file and create a list contain each line
    """
    with open(file_path) as f:
        data = f.read()
    data = data.split('\n')
    retval = []
    for datum in data:
        if datum != '':
            retval.append(datum)
    return retval


def is_followed_by(api, target_screen_name, source_screen_name=None):
    """Return true if the source_screen_name (if None, use current api) is
    followed by the target_screen_name
    """
    # print target_screen_name
    if source_screen_name is None:
        source, _ = api.show_friendship(target_screen_name=target_screen_name)
        return source.followed_by
    else:
        source, _ = api.show_friendship(source_screen_name=source_screen_name,
                                        target_screen_name=target_screen_name)
        return source.followed_by


def is_following(api, target_screen_name, source_screen_name=None):
    """Return true if the source_screen_name (if None, use current api) is
    following the target_screen_name
    """
    if source_screen_name is None:
        source, _ = api.show_friendship(target_screen_name=target_screen_name)
        return source.following
    else:
        source, _ = api.show_friendship(source_screen_name=source_screen_name,
                                        target_screen_name=target_screen_name)
        return source.following


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
    # api.retweet('421542742167007233')
    return api


def pick_random_element(my_list):
    """
    Pick random element from a list of element. Return None if empty list
    """
    if len(my_list) == 0:
        return None
    else:
        random_index = randint(0, len(my_list) - 1)
        return my_list[random_index]

if __name__ == '__main__':
    # a = 'famous_accounts.txt'
    # c = read_list(a)
    # print type(c)
    # for d in c:
    #     print d, '++++++++++'
    test_api = setup_api(test_consumer_key, test_consumer_secret,
                         test_access_key, test_access_secret)
    test_api.update_status('@TVSeriesUpdate telo goreng', '421542742167007233')
