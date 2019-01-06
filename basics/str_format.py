age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
print('{} was {} years old when he wrote this book'.format(name, age))
print('{fish} was {boggart} years old when he wrote this book' .format(fish=name, boggart=age))
print('Why is {0} playing with that python?' .format(name))
print(name + ' is ' + str(age)+ ' years old')
#hoje eu aprendi a usar o format, para incluir como parte de uma string
#o valor de variaveis ja definidas no progrma
#isso pode ser feito de diferentes formas, uma delas numerando o ponto
#de inclusâo do argumento do format com o numero sequencial em que esse argumento dentro
#da função format entre chaves({}) no onto desejado da string
#outra forma de se utilizar a função format é colocando chaves fechadas vazias
#ao longo da string em que se esta trabalhando, instancia das chaves acessará
#um argumento difernete da função em ordem (esta forma não permite multiplas utilizações do mesmo argumento)
#uma terceira maneira que isto pode ser feito é por meio da atribuição de um nome aos argumentos da função,
#assim o nome atribuido é o que deve ser inserido entre chaves ao longo da string(na função format o nome deve preceder o argumento seuido de =)
#uma ultima maneira(expressa abaixo) é uma forma em que a função format está abreviada no f que antecede a string, e uma vez que isso acontece
#quaisquer nomes de variaveis expressos entre chaves resultarão no seu respectivo valor inserido na string
print(f'{name} was {age} years {age} old when he wrote this book')  # notice the 'f' before the string
print(f'Why is {name} playing with that python?')  # notice the 'f' before the string
# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
#é possivel alterar as condições de saída do format, inserindo : ddentro das chaves após o identificador de variavel
