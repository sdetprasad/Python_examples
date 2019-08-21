'''
Write a python program to check whether given number is prime
'''
a = int(input('Enter any number : '))
for i in range(2,a):
    if (a % i) == 0:
        print('Number is not a prime number')
        break
else:
    print('Number is a prime number')
