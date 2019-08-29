a = int(input('Enter the number for which you want to calculate factorial : '))

def factorial(n):
    fact = 1
    while n>0:
        fact *= n
        n -= 1
    return fact

fact = factorial(a)

print('Factorial of the given no is : ',fact)
    