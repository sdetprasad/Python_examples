'''
Write a Python function to check whether a number is in a given range.
'''

a = int(input('Enter your age : '))

def noinrange(n):
    d = range(1,151)
    if n in d:
        print('\nAge is in the range')
    else:
        print('\nAge not in the given range')

noinrange(a)



