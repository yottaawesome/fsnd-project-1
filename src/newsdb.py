'''Supporting module that connect to the news database.'''
import psycopg2

with open('password') as f:
    _PASSWORD = f.read()
with open('./sql/most-popular-articles.sql') as f:
    _TOP_ARTICLES_SQL = f.read()
with open('./sql/most-popular-authors.sql') as f:
    _TOP_AUTHORS_SQL = f.read()
with open('./sql/most-errors-by-day.sql') as f:
    _TOP_ERRORS_SQL = f.read()

def _exec_sql(sql: str):
    '''Internal to newsdb. Executes the inputted SQL string.'''

    try:
        conn = psycopg2.connect(dbname='news', user='newsuser', password=_PASSWORD)
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    except Exception as ex:
        print('An error occurred connecting to the database.')
        print(ex)
        return None

    finally:
        conn.close()

def _print_results(header, results, print_func):
    '''Internal to newsdb. Formats and prints the results.'''

    if results:
        print('')
        print('-------------------------------------------------------------')
        print('')
        print(header)
        for res in results:
            print_func(res)
        print('')
        print('-------------------------------------------------------------')
        print('')

def top_articles():
    '''Retrieves and prints the top 3 articles of all time.'''

    _print_results(
        'The top 3 articles of all time are:',
        _exec_sql(_TOP_ARTICLES_SQL),
        lambda res: print('{} -- {} views'.format(res[0], res[1])))

def top_authors():
    '''Retrieves the most viewed authors in descending order of views.'''

    _print_results(
        'The most popular article authors of all time are:',
        _exec_sql(_TOP_AUTHORS_SQL),
        lambda res: print('{} -- {} views'.format(res[0], res[1])))

def top_error_days():
    '''Displays the days where error requests are >1% of requests on those day.'''

    _print_results(
        'The days where error requests amounted to more than 1% of requests:',
        _exec_sql(_TOP_ERRORS_SQL),
        lambda res: print('{} -- {}%'.format(res[0], res[1])))
