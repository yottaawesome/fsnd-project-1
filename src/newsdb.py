import psycopg2

with open('password') as f:
    password = f.read()
with open('./sql/most-popular-articles.sql') as f:
    top_articles_sql = f.read()
with open('./sql/most-popular-authors.sql') as f:
    top_authors_sql = f.read()
with open('./sql/most-errors-by-day.sql') as f:
    top_error_days_sql = f.read()

class NewsDB:

    def top_articles(self):
        try:

            conn = psycopg2.connect(dbname='news', user='newsuser', password=password)
            cursor = conn.cursor()
            cursor.execute(top_articles_sql)
            results = cursor.fetchall()
            print('')
            print('-------------------------------------------------------------')
            print('The top 3 articles of all time are:')
            for r in results:
                print('{} -- {} views'.format(r[0], r[1]))
            print('-------------------------------------------------------------')
            print('')

        finally:
            conn.close()

    def top_authors(self):
        try:

            conn = psycopg2.connect(dbname='news', user='newsuser', password=password)
            cursor = conn.cursor()
            cursor.execute(top_authors_sql)
            results = cursor.fetchall()
            print('')
            print('-------------------------------------------------------------')
            print('The most popular article authors of all time are:')
            for r in results:
                print('{} -- {} views'.format(r[0], r[1]))
            print('-------------------------------------------------------------')
            print('')

        finally:
            conn.close()

    def top_error_days(self):
        try:

            conn = psycopg2.connect(dbname='news', user='newsuser', password=password)
            cursor = conn.cursor()
            cursor.execute(top_error_days_sql)
            results = cursor.fetchall()
            print('')
            print('-------------------------------------------------------------')
            print('The days where error requests amounted to more than 1% of requests:')
            for r in results:
                print('{} -- {}%'.format(r[0], r[3]))
            print('-------------------------------------------------------------')
            print('')

        finally:
            conn.close()
            