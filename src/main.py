#!./env/bin/python3
'''The main module.'''

from newsdb import top_articles, top_authors, top_error_days


def print_options():
    '''Prints all available input options.'''

    print('Enter one of the following options:')
    print('1: view most popular articles')
    print('2: view the most popular authors')
    print('3: view the days where failed requests amounted to more than 1% ' \
        'of requests on that day')
    print('r: review options again')
    print('q: quit')


def main():
    '''The core input loop of this script.'''

    selection = None

    print('Welcome!')
    print_options()

    while selection != 'q':
        selection = input('Enter your selection: ')

        if selection == '1':
            top_articles()

        elif selection == '2':
            top_authors()

        elif selection == '3':
            top_error_days()

        elif selection == 'r':
            print_options()

        elif selection == 'q':
            print('Bye!')

        else:
            print('Invalid input {}'.format(selection))

main()
