'''Write a Python program to count the number of characters (character frequency) in a string.
Sample String : codekul.com
Expected Result : {'c': 2, '0': 2, 'd': 1, 'e': 1, 'k': 1, 'u': 1, 'l': 1, 'm': 1}
'''

import collections
a = input('Enter any data : ')
d = collections.defaultdict(int)
for c in a:
    d[c] += 1
for c in sorted(d,key=d.get, reverse=True):
    print("'{}': {}".format(c,d[c]))




