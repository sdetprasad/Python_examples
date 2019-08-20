name = input('Enter your name : ')
mk = float(input('Enter the your Percentage : '))

if mk >= 35 and mk <=50:
    print('{} has passed with {} percentage and secured Second class'.format(name,mk))
elif mk > 50 and mk <= 59:
    print('{} has passed with {} percentage and secured  Higher Second class'.format(name,mk))
elif mk >= 60 and mk <=69:
    print('{} has passed with {} percentage and secured First class'.format(name,mk))
elif mk >= 70 and mk <=99:
    print('{} has passed with {} percentage and secured Distinction class'.format(name,mk))
else:
    print('Invalid value entered')


