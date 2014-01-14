__author__ = 'ismailsunni'
__project_name = 'TweetJaran'
__filename = 'stat.py'
__date__ = '1/14/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

import constants
from util import setup_api

# constants
consumer_key = constants.consumer_key
consumer_secret = constants.consumer_secret
access_key = constants.access_key
access_secret = constants.access_secret
stat_file = 'stat.txt'


def main():
    api = setup_api(consumer_key, consumer_secret, access_key, access_secret)
    # f = open(stat_file, 'a')
    number_follower = api.get_user
    print number_follower

if __name__ == '__main__':
    main()