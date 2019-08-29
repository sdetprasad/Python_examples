class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print('The Addition of a & b is :',self.a + self.b)
    def sub(self):
        print('The subtration of a & b is :',self.a - self.b)
    def mul(self):
        print('the multiplication of a & b is :',self.a * self.b)
    def div(self):
        print('the division of a & b is :',self.a / self.b)





myobj = Calculator(800,50)
myobj.add()
myobj.sub()
myobj.mul()
myobj.div()
