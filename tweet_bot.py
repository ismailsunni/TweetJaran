"""Tweet Bot, for tweeting random tweet
"""
__date__ = '08/01/2014'
__author__ = '@ismailsunni'


import tweepy
import constants
from db_conn import DBConn
from random import randint
from datetime import datetime
import time

# constants
consumer_key = constants.consumer_key
consumer_secret = constants.consumer_secret
access_key = constants.access_key
access_secret = constants.access_secret


def create_link(post_id):
    prev_string = 'http://sarapanhati.com/qa/?qa='
    return prev_string + str(post_id)


def main():
    local_tz = time.timezone / (60 * 60)
    current_hour = (datetime.now().hour + (7 + local_tz)) % 24  # to GMT +7
    if 0 < current_hour < 5:
        print 'too late to tweet'
        exit()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    dbconn = DBConn()
    post_table = 'qa_posts'
    post_id_column = 'postid'
    title_column = 'title'
    num_post = 10

    query = 'SELECT ' + post_id_column + ', ' + title_column + ' FROM ' + \
            post_table + ' WHERE ' + title_column + ' is not null ORDER BY ' + \
            post_id_column + ' DESC LIMIT ' + str(num_post)
    a = dbconn.read(query)
    rand_number = randint(0, num_post)

    api.update_status(str(a[rand_number][1]) + ' | Silahkan baca di ' +
                      create_link(a[rand_number][0]))

if __name__ == '__main__':
    main()