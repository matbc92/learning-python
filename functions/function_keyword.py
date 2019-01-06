# uma vez definidos os parametros de uma função, eles podem ser preenchidos
# com os valores desejados, na posição refenete ao parametro,
# ou pelo nome atribuido pelo parametro, utilizando
# a estrutura (nomedoparametro=valordesejadodoparametro)
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)
