'''Write a Python program that accepts a string and calculate the number of digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2'''


a = input('Enter data : ')
print(a)
letters = 0
digits = 0
length = len(a)
for b in a:
    if b.isalpha():
        letters += 1
    elif b.isnumeric():
        digits += 1
    else:
        pass
print('Letters and digits are : {} {}'.format(letters,digits))


