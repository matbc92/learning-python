# return, é uma declaração que permite que as instruções de uma função sejam 
# interrompidas e o output da função seja o argumento de return
def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y
print(maximum(2, 3))
