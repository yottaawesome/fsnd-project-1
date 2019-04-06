from newsdb import NewsDB

def print_options():
    print('Enter one of the following options:')
    print('1: view most popular articles')
    print('2: view the most popular authors')
    print('3: view the days where failed requests amounted to more than 1% of the requests on that day')
    print('r: review options again')
    print('q: quit')

db = NewsDB()
selection = ''

print('Welcome!')
print_options()

while selection != 'q':
    selection = input('Enter your selection: ')
    
    if selection == '1':
        db.top_articles()
    
    elif selection == '2':
        db.top_authors()
    
    elif selection == '3':
        db.top_error_days()
    
    elif selection == 'r':
        print_options()

    elif selection == 'q':
        print('Bye!')

    else:
        print('Invalid input {}'.format(selection))