import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(host='127.0.0.1',
                                                        database='fin_website',
                                                        # database may not be found which raises an exception
                                                        user='root',
                                                        password='root')
        try:
            # self.conn, connection = mysql.connector.connect(host='127.0.0.1',
            #                           database='fin_website',
            #                           user='root',
            #                           password='root')
            if self.conn.is_connected():
                cursor = self.conn.cursor()
                cursor.execute('create database if not exists fin_website')
        except Error as e:
            print("Error: ", e)

    def create_tables(self):
        cursor = self.conn.cursor()
        article_table = "create table if not exists articles (headline varchar(255), link varchar(255), neg double, " \
                        "neu double, pos double, compound double)"
        cursor.execute(article_table)

        symbols_table = "create table if not exists symbols (symbol varchar(20), link varchar(255))"
        cursor.execute(symbols_table)

        self.close_connection()

    def insert_article(self, article_data):
        print("saving article: %s, %s, %f, %f, %f, %f" % (article_data['link'], article_data['title'], article_data['neg'], article_data['neu'], article_data['pos'], article_data['compound']))
        try:
            self.conn.cursor().execute("insert into articles (headline, link, neg, neu, pos, compound) values ('%s', '%s', '%f', '%f', '%f', '%f')" % (article_data['title'], article_data['link'], article_data['neg'], article_data['neu'], article_data['pos'], article_data['compound'],))
        except Error as e:
            print("Error: ", e)

        self.close_connection()

    def insert_symbol(self, symbol, article_link):
        cursor = self.conn.cursor()
        cursor.execute("insert into symbols (symbol, link) values ('%s', '%s')" % (symbol, article_link,))

        self.close_connection()

    def close_connection(self):
        self.conn.close()
