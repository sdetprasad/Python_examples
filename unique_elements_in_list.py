'''

Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]

'''

list1 = [1,3,4,55,1,1,2,3,3,4,5,6,5,3,3,55,6,66,6,7]

def unique_list(l):
    unlist = []
    for ele in l:
        if ele not in unlist:
            unlist.append(ele)
            ele += 1
    return unlist

unique = unique_list(list1)

print('Original List : {}'.format(list1))
print('\nList with unique elements : {}'.format(unique))
