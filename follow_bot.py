"""Follow bot, to follow some followers from an account
"""
__date__ = '08/01/2014'
__author__ = '@ismailsunni'

import tweepy
import constants
from datetime import datetime
from util import is_up2date, is_good_account, setup_api, read_list

# constants
consumer_key = constants.consumer_key
consumer_secret = constants.consumer_secret
access_key = constants.access_key
access_secret = constants.access_secret


def test():
    a = datetime.now()
    print is_up2date(a)


def main():
    api = setup_api(consumer_key, consumer_secret, access_key, access_secret)
    file_path = 'famous_accounts.txt'
    accounts = read_list(file_path)
    for account in accounts:
        print '### From follower of ', account
        try:
            followers = api.followers(account)
            for follower in followers:
                if is_good_account(follower):
                    print follower.screen_name
                    try:
                        friend = api.create_friendship(follower.screen_name)
                        if friend.screen_name == follower.screen_name:
                            print 'Follow ' + follower.screen_name + ' success'
                        else:
                            print 'Follow ' + follower.screen_name + ' failed'
                    except tweepy.TweepError, e:
                        print e
        except Exception, e:
            print e
    print 'fin'

if __name__ == '__main__':
    main()
    # test()