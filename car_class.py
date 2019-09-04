# Choose between 4 cars to drive and drive using 6 Gear options. Enjoy Driving!!

class Car:
    
    def __init__(self,a):
        self.a = a

       
    def alto(self):
        print('\nMaruti Alto drive mode')
        print('\nPress 0 to turn on the car')
        t = int(input('Input : '))
        if t == 0:
            print('\nMaruti Alto ON')
        else:
            print('\nInvalid Command')


    def accent(self):
        print('\nHyundai Accent drive mode')
        print('\nPress 0 to turn on the car')
        t = int(input('Input : '))
        if t == 0:
            print('\nHyundai ON')
        else:
            print('\nInvalid Command')

    def swift(self):
        print('\nMaruti Swift drive mode')
        print('\nPress 0 to turn on the car')
        t = int(input('Input : '))
        if t == 0:
            print('\nMaruti Swift')
        else:
            print('\nInvalid Command')

    def Mercedes_Benz(self):
        print('\nMercedes Benz drive mode')
        print('\nPress 0 to turn on the car')
        t = int(input('\nInput : '))
        if t == 0:
            print('\nMercedes Benz ON')
        else:
            print('\nInvalid Command')           

    def drive_modes(self):
        print('\nGears : 1,2,3,4,5,Reverse Mode, 8 to Turn OFF')
        
        while True:
            g = int(input('\nGear Input : '))
            if g == 0:
                print('\nInvalid Gear')
                break
            if g == 1:
                print('\nCar running in Gear 1, Speed 20km/hr')
            elif g == 2:
                print('\nCar running in Gear 2, Speed 40km/hr')
            elif g == 3:
                print('\nCar running in Gear 3, Speed 60km/hr')
            elif g == 4:
                print('\nCar running in Gear 4, Speed 80km/hr')
            elif g == 5:
                print('\nCar running in Gear 5, Speed 100km/hr+')
            elif g == 6:
                print('\nCar running in Reverse Mode')
            elif g == 8:
                print('\nCar OFF')
                break


        
print('Bienvenido! Choose any one cars listed below to drive ')
print('\n1.Maruti Alto\n2.Hyundai Accent\n3.Maruti Swift\n4.Mercedes Benz')

a = int(input('\nEnter Choice : '))
obj = Car(a)
if a == 1:
    obj.alto()
    obj.drive_modes()
elif a == 2:
    obj.accent()
    obj.drive_modes()
elif a == 3:
    obj.swift()
    obj.drive_modes()
elif a == 4:
    obj.Mercedes_Benz()
    obj.drive_modes()

    
else:
    print('Invalid Choice')




