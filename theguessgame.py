import random

while True:

        no1 = int(input('Enrer a numbe between 1 - 10:'))

        if no1 == 0:
            print('Invalid input')
            break

        no2 = random.randint(1,10)

        if no1 == no2:
            print('Winner Winner Chicken Dinner')
        else:
            print('Better luck next time')
    