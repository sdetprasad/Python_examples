'''
Write a Python program to convert temperatures to and from celsius, fahrenheit
'''
'''
T(°F) = T(°C) × 9/5 + 32
'''

a = int(input('Enter temperature in Celsius : '))
temp = (a * 1.8) + 32
print('The temperature in Farenheit is : {}'.format(temp))

