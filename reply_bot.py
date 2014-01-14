"""Reply some followers/friends' tweets
"""
__author__ = '@ismailsunni'
__project_name = 'TweetJaran'
__filename = 'retweet_bot'
__date__ = '09/01/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

import constants
from util import (setup_api, is_good_account, read_list, is_followed_by,
                  pick_random_element)

# constants
consumer_key = constants.consumer_key
consumer_secret = constants.consumer_secret
access_key = constants.access_key
access_secret = constants.access_secret


def is_good_status(follower):
    """
    Check if the last status is good
    """
    last_status = follower.status
    tweet_text = last_status.text
    if '@' in tweet_text:
        return False
    return False


def reply(api, tweet_text, target_user, target_tweet=None):
    """
    Reply a target_tweet from a target_user
    """
    full_tweet = '@' + target_user.screen_name + ' ' + tweet_text
    if target_tweet is not None:
        target_tweet_id = target_tweet.id_str
    else:
        target_tweet_id = target_user.status.id_str

    api.update_status(full_tweet, target_tweet_id)


def main():
    api = setup_api(consumer_key, consumer_secret, access_key, access_secret)

    file_path = 'tweets.txt'
    tweet_data = read_list(file_path)
    tweet_text = pick_random_element(tweet_data)
    # get target
    target_accounts = api.friends()
    done = False
    while not done:
        target_account = pick_random_element(target_accounts)
        is_followed = is_followed_by(
            api, target_screen_name=target_account.screen_name)
        if is_good_account(target_account) and not is_followed:
            reply(api, tweet_text, target_account)
            done = True

if __name__ == '__main__':
    main()