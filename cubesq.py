from threading import Thread

def cube(num):
    print('Cube of the number is : {} '.format(num**3))

def square(num):
    print('Square of the number is : {}'.format(num**2))

t1 = Thread(target=cube, args=(555,))
t1.start()
t2 = Thread(target=square, args=(555,))
t2.start()
print('\nMain thread Exiting')

