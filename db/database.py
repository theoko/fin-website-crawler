import pyodbc


class Database:
    def __init__(self):
        self.conn = pyodbc.connect('Driver={MySQL ODBC 5.3 Unicode Driver};'
                      'Server=127.0.0.1;'
                      'Database=fin_website;'
                      'Trusted_Connection=yes;')
        self.conn.cursor().execute('create database if not exists fin_website')

    def create_tables(self):
        article_table = "create table if not exists articles (headline varchar(255), link varchar(255), neg double, " \
                        "neu double, pos double, compound double)"
        self.conn.execute(article_table)
        self.conn.commit()

        symbols_table = "create table if not exists symbols (symbol varchar(20), link varchar(255))"
        self.conn.execute(symbols_table)
        self.conn.commit()

        self.close_connection()

    def insert_article(self, article_data):
        self.conn.cursor().execute("insert into products (headline, link, neg, neu, pos, compound) values ('pyodbc', 'awesome library')")
        self.conn.commit()

        self.close_connection()

    def insert_symbol(self, symbol, article_link):
        self.conn.cursor().execute("insert into symbols (symbol, link) values ('test', 'test')")
        self.conn.commit()

        self.close_connection()

    def close_connection(self):
        self.conn.close()
