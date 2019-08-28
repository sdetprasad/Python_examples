'''
Write a Python function to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]

        even.append(ele)
        ele += 1
'''

def even_numbers(x):
    even = []
    for ele in x:
        if ele % 2 == 0:
            even.append(ele)
            ele += 1
    return even
            

l = list(range(101))

a = even_numbers(l)

print('Original list : ',l)

print('\nEven numbers in list : {}'.format(a))
