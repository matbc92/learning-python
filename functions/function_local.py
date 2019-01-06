# Dentro das instruções de uma função uma variavel pode ser reescrtia,
# porem, este processo não afeta o valor desta variavel fora da função,
# é uma operação extritamente local, para efeito de execussão da função,
# importante, não confundir os parametros internos de uma função com
# variveis em seu exterior
x = 50


def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('x is still', x)
a = 21
func(a)
