"""Database Connection
For handling database connection.
"""

__author__ = '@ismailsunni'
__project_name = 'TweetJaran'
__filename = 'db_conn.py'
__date__ = '08/01/14'
__copyright__ = 'imajimatika@gmail.com'

import MySQLdb
import constants


class DBConn:
    """Class for handling database connection.
    """
    # database variable
    db_host = constants.db_host
    db_user = constants.db_user
    db_password = constants.db_password
    db_name = constants.db_name

    def __init__(self):
        """Init db class
        """
        self.conn = MySQLdb.connect(self.db_host, self.db_user,
                                    self.db_password, self.db_name,
                                    charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def read(self, query):
        """Read database.
        """

        try:
            self.cursor.execute(query)
            retval = self.cursor.fetchall()
            return retval

        except MySQLdb.MySQLError as myExc:
            self.conn.rollback()
            print 'MySQLdb.MySQLError', myExc
            return None

    def insert(self, query):
        """Insert to database.
        """

        try:
            self.cursor.execute(query)
            self.conn.commit()
            return True

        except MySQLdb.MySQLError as myExc:
            print 'MySQLdb.MySQLError', myExc
            self.conn.rollback()
            return False

    def delete(self, query):
        """Delete row(s) in database.
        """

        try:
            self.cursor.execute(query)
            self.conn.commit()
            return True

        except MySQLdb.MySQLError as myExc:
            self.conn.rollback()
            print 'MySQLdb.MySQLError', myExc
            return False

    def update(self, query):
        """Update database.
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
            return True

        except MySQLdb.MySQLError as myExc:
            print 'MySQLdb.MySQLError', myExc
            self.conn.rollback()
            return False

    def insert_tweet(self, my_tweet_id, my_text, my_timestamp,
                     my_user_id, my_user_name, my_categorized,
                     my_sentimented):
        """Insert tweet to database.
        """
        my_query = 'INSERT INTO `tweets` (`tweet_id`, `text`, `time_stamp`, '
        my_query += '`user_id`, `user_name`, `categorized`, `sentimented`)'

        my_query += ' VALUES '

        my_query += '("' + my_tweet_id + '","'
        my_query += MySQLdb.escape_string(my_text) + '","'
        my_query += str(my_timestamp) + '","' + my_user_id + '","'
        my_query += my_user_name + '",' + str(my_categorized) + ','
        my_query += str(my_sentimented) + ')'

        return self.insert(my_query)