# global é uma declaração(statement) que permite de especificar que a variavel utilisada
# dentro da função não é um parametro local, mas sim a variavel com aquele
# nome definida no corpo do codigo
x = 50


def func():
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)


func()
print('Value of x is', x)
