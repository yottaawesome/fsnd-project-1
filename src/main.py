import psycopg2

with open('password') as f:
    password = f.read()

conn = psycopg2.connect(dbname='news', user='newsuser', password=password)

conn.close()

print('Welcome!')
print('Enter one of the following options:')
print('1: view most popular articles')
print('2: view the most popular authors')
print('3: view the days where failed requests amounted to more than 1% of the requests on that day')
print('q: quit')

selection = ''
while selection != 'q':
    selection = input('Enter your selection ')
    
    if selection == 1:
        pass
    
    elif selection == 2:
        pass
    
    elif selection == 3:
        pass
    
    elif selection == 'q':
        print('Bye!')

    else:
        print('Invalid input {}'.format(selection))
