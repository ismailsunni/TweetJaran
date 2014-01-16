"""Unfollow some accounts that not following back :)
"""
__author__ = 'ismailsunni'
__project_name = 'TweetJaran'
__filename = 'unfollow_bot.py'
__date__ = '1/16/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''


from util import setup_api, is_followed_by
import time
import constants
from tweepy import Cursor, TweepError
from datetime import datetime

# constants
consumer_key = constants.consumer_key
consumer_secret = constants.consumer_secret
access_key = constants.access_key
access_secret = constants.access_secret

def need_unfollow(api, user):
    """Check if a user need to be unfollowed
    """
    statuses_count = user.statuses_count
    followers_count = user.followers_count
    friends_count = user.friends_count
    is_followed = is_followed_by(api, target_screen_name=user.screen_name)
    if not is_followed:
        return True



def unfollow(api, user):
    """
    Unfollow a user
    """
    api.destroy_friendship(user.screen_name)


def main():
    unfollow_counter = 0
    keep_follow_counter = 0
    api = setup_api(consumer_key, consumer_secret, access_key, access_secret)
    friends = []
    try:
        # friends = Cursor(api.friends).items()
        i = 0
        for page in Cursor(api.friends).pages():
            print 'page: ', i
            print len(page)
            i += 1
            while len(page) > 0:
                friend = page.pop()
                if need_unfollow(api, friend):
                    print friend.name, ' has been unfollowed'
                    unfollow(api, friend)
                    unfollow_counter += 1
                else:
                    print 'keep following ', friend.name
                    keep_follow_counter += 1
            friends.extend(page)
            time.sleep(60)
    except TweepError, e:
        print e
        d = api.rate_limit_status()
        print d
        for i,j in d['resources']['friends'].iteritems():
            print i, j
            print(datetime.fromtimestamp(int(j['reset'])).strftime('%Y-%m-%d %H:%M:%S'))
    finally:
        print len(friends)
        print 'success to unfollow ', unfollow_counter, ' bad accounts'
        print 'keep following ', keep_follow_counter, ' good accounts'
        print 'total: ', unfollow_counter + keep_follow_counter

if __name__ == '__main__':
    main()