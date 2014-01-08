"""Tweet Bot, for tweeting random tweet
"""
__date__ = '08/01/2014'
__author__ = '@ismailsunni'


import tweepy
import constants
from db_conn import DBConn
from random import randint

# constant
consumer_key = constants.consumer_key
consumer_secret = constants.consumer_secret
access_key = constants.access_key
access_secret = constants.access_secret



def create_link(id):
    prev_string = 'http://sarapanhati.com/qa/?qa='
    return  prev_string + str(id)

def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # api.update_status('Sedang gundah apa hari ini?')

    data = DBConn()
    post_table = 'qa_posts'
    post_id_column = 'postid'
    title_column = 'title'
    num_post = 10
    # tables = data.read('SHOW TABLES')
    # columns_post = data.read('SHOW COLUMNS FROM ' + post_table)
    # for i in columns_post:
    #     print i
    query = 'SELECT ' + post_id_column + ', ' + title_column + ' FROM ' + post_table + ' WHERE ' + \
            title_column + ' is not null ORDER BY ' + post_id_column + ' DESC LIMIT ' + str(num_post)
    print query
    a = data.read(query)
    print len(a)
    rand_number = randint(0, num_post)

    api.update_status(str(a[rand_number][1]) + ' baca di ' + create_link(a[rand_number][0]))

if __name__ == '__main__':
    main()