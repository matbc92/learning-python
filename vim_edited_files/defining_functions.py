# coding=utf8
'''Revisando a definição de funções '''
def square(number):
    '''squaring a number, pretty simple stuff really '''
    return number**2
print(square(39))
print(square(square(3)))
def squareroot(n):
    root = n/2          #initial guess will be 1/2 of n
    for k in range(20000):
        root = (1/2)*(root + (n / root))
    return root
print(squareroot(1521))
