"""Tweet Bot, for tweeting random tweet
"""
__date__ = '08/01/2014'
__author__ = '@ismailsunni'

import constants
from db_conn import DBConn
from random import randint
from datetime import datetime
import time
from util import setup_api

# constants
consumer_key = constants.consumer_key
consumer_secret = constants.consumer_secret
access_key = constants.access_key
access_secret = constants.access_secret

STATUS_FILE = 'galaukuadrat.txt'

def create_link(post_id):
    prev_string = 'http://sarapanhati.com/qa/?qa='
    return prev_string + str(post_id)

def get_status(file_path):
    try:
        f = open(file_path, 'r')
        statuses = f.readlines()
        f.close()
    except Exception, e:
        print 'Error', e
        raise e
    num_status = len(statuses)
    rand_number = randint(0, num_status)
    status = statuses[rand_number]
    if status[-1] == '\n':
        status = status[:-1]
    return status

def get_link():
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
    return str(a[rand_number][1]) + ' | Silahkan baca di ' + create_link(a[rand_number][0])

def main():
    local_tz = time.timezone / (60 * 60)
    current_hour = (datetime.now().hour + (7 + local_tz)) % 24  # to GMT +7
    if 0 < current_hour < 5:
        print 'too late to tweet'
        return
    api = setup_api(consumer_key, consumer_secret, access_key, access_secret)

    rand_number = randint(0, 10)
    if rand_number % 7 == 0:
        status = get_link()
    else:
        status = get_status(STATUS_FILE)
    print status
    api.update_status(status)


if __name__ == '__main__':
    main()