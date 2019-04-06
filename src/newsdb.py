'''Supporting module that connect to the news database'''
import psycopg2

with open('password') as f:
    PASSWORD = f.read()
with open('./sql/most-popular-articles.sql') as f:
    TOP_ARTICLES_SQL = f.read()
with open('./sql/most-popular-authors.sql') as f:
    TOP_AUTHORS_SQL = f.read()
with open('./sql/most-errors-by-day.sql') as f:
    TOP_ERRORS_SQL = f.read()

class NewsDB:
    '''This is a helper class for easily accessing the new DB'''

    @staticmethod
    def top_articles():
        '''Retrieves and prints the top 3 articles of all time'''

        try:
            conn = psycopg2.connect(dbname='news', user='newsuser', password=PASSWORD)
            cursor = conn.cursor()
            cursor.execute(TOP_ARTICLES_SQL)
            results = cursor.fetchall()
            print('')
            print('-------------------------------------------------------------')
            print('The top 3 articles of all time are:')
            for res in results:
                print('{} -- {} views'.format(res[0], res[1]))
            print('-------------------------------------------------------------')
            print('')

        finally:
            conn.close()

    @staticmethod
    def top_authors():
        '''Retrieves the most viewed authors in descending order of views'''

        try:
            conn = psycopg2.connect(dbname='news', user='newsuser', password=PASSWORD)
            cursor = conn.cursor()
            cursor.execute(TOP_AUTHORS_SQL)
            results = cursor.fetchall()
            print('')
            print('-------------------------------------------------------------')
            print('The most popular article authors of all time are:')
            for res in results:
                print('{} -- {} views'.format(res[0], res[1]))
            print('-------------------------------------------------------------')
            print('')

        finally:
            conn.close()

    @staticmethod
    def top_error_days():
        '''Displays the days where error requests are >1% of requests on those day'''

        try:
            conn = psycopg2.connect(dbname='news', user='newsuser', password=PASSWORD)
            cursor = conn.cursor()
            cursor.execute(TOP_ERRORS_SQL)
            results = cursor.fetchall()
            print('')
            print('-------------------------------------------------------------')
            print('The days where error requests amounted to more than 1% of requests:')
            for res in results:
                print('{} -- {}%'.format(res[0], res[3]))
            print('-------------------------------------------------------------')
            print('')

        finally:
            conn.close()
            