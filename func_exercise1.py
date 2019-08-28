'''

Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).
'''
l = list(range(31))

def calulate_squares(x):
    sq = []
    for ele in x:
        sq.append(ele**2)

    return sq

print('List of numbers from 1 - 30 : ',l)

sqrs = calulate_squares(l)
print('List of squares of numbers from 1 - 30 :',sqrs)