class Bankaccount:

    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        

    def display_details(self):
        print('\nAccount Holder name : {} \nAccount Number : {} \nIFSC Code : {} \nAccount Balance : {}'.format(self.a,self.b,self.c,self.d))

    def deposit(self):
        dep = int(input('Enter amount to be Deposited : '))
        dep1 = self.d + dep
        print('New account balance : {}'.format(dep1))

    def withdraw(self):
        wid = int(input('Enter the amount to withdraw : '))
        wid1 = self.d - wid
        print('New account balance : {} '.format(wid1))

a = input('Enter your Name : ')
b = int(input('Enter Account number : '))
c = input('Enter IFSC Code : ')
d = int(input('Enter Account Balance : '))

myobj = Bankaccount(a,b,c,d)

myobj.display_details()
ch = int(input('\nEnter 1 to deposit money or Enter 2 to withdraw money '))


if ch == 1:
    myobj.deposit()
elif ch == 2:
    myobj.withdraw()
else:
    pass



