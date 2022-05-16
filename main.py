# function that calculates diffecence between two dates in YYYYMMDD format.

'''
#uncomment this section if you want to use shell
import sys
try:
    m = sys.argv[1]
    n = sys.argv[2]
except IndexError:
    print('ERROR - incorect arguments')
    exit()
'''

m = input('enter a date in YYYYMMDD format: ')
n = input('enter another date in YYYYMMDD format: ')

from datetime import date

def date_diff(m,n):

    m = str(m)
    n = str(n)
    
    if not len(m) == 8 or not len(m) == 8:
        print('ERROR - invalid input')

    else:
        try:
            YY1 = int(m[:4])
            YY2 = int(n[:4])
            MM1 = int(m[4:6])
            MM2 = int(n[4:6])
            DD1 = int(m[6:8])
            DD2 = int(n[6:8])

            date1 = date(YY1,MM1,DD1)
            date2 = date(YY2,MM2,DD2)
            diff = date1 - date2
            difference = diff.days
            
            if difference<0:
                difference = difference*(-1)
                print('Difference:',difference,'days')
            else:
                print('Difference:',difference,'days')

        except ValueError:
            print('ERROR - invalid input.')

        except NameError:
            print('ERROR - invalid input.')


date_diff(m,n)
