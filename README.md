TweetJaran
==========

This is Jaran

Requirements:
------------
- tweepy: sudo pip install tweepy
- MySQL-python: sudo pip install MySQL-python

TweetBot
-------
For tweeting content every specific time.

Run as a cronjob. For example, run this script per 30 minutes:
0,30 * * * * ~/dev/python/TweetJaran/gembus.sh

Notes
-----
Check cronjob log: grep CRON /var/log/syslog
