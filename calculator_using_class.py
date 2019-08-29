class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print('\nThe Addition of a & b is :',self.a + self.b)
    def sub(self):
        print('\nThe subtration of a & b is :',self.a - self.b)
    def mul(self):
        print('\nthe multiplication of a & b is :',self.a * self.b)
    def div(self):
        print('\nthe division of a & b is :',self.a / self.b)


a = int(input('\nEnter value of a :'))
b = int(input('\nEnter value of b :')) 


myobj = Calculator(a,b)
myobj.add()
myobj.sub()
myobj.mul()
myobj.div()
