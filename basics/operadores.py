# coding=utf-8
# + adiciona dois itens(opratarios, ou operand)
print('3 + 5 =', 3 + 5)
print("'a' + 'b' = " + 'a' + 'b')
# - subtrai dois itens, se o primeiro item estiver omisso, ele é assumido zero
# * multiplica dois numeros, ou repete uma string x vezes
print("'la' * 3 = " + 'la' * 3)
# ** executa uma potenciação
print('3 ** 4 =', 3 ** 4)
# / divide
#// faz uam divisão excluindo o zero
print('7 // 2 = ' + str(7 // 2))
#% divisao modulo, mostra o resto da divisão
print('7 % 2 =', 7 % 2)
#<< é um left shift, ele pega o valor do numero em binario e move os digitos um numero determinado de casas para a esquerda
print('1 << 5 =', 1 << 5)
#>> é um right shift, o mesmo que o left shift só que pro outro lado
print('32 >> 5 =', 32 >> 5)
#& and bit-wise ele compara o valor binario dos dois elementos, resultando num terceiro valor binario
# que exprime 1 em todas as casas que os dois valores anteriores sejam iguais e zero no restante
#####################
#| bit-wise or ele compara o valor binario dos dois elementos, resultando num terceiro valor binario
# que exprime 1 em todas as casas que o valor de pelo menos um dos elementos seja 1 e zero nas outras
#####################
#^ bit-wise xor ele compara o valor binario dos dois elementos, resultando num terceiro valor binario
# que exprime 1 em todas as casas que o valor de somento um dos elementos seja 1 no restante zero
#####################
#~bitwise invert alterna todos os digitos do valor binario de um elemento,
# tal operação conicide com a a operaçao de -(x+1) sendo x o valor a ser invertido
#####################
#< operador de menor do que, resulta um valor True ou False booleano
print('3 < 5 =', 3 < 5)
print('5 < 3 =', 5 < 3)
#>maior que, o oposto de menor que
print('3 > 5 =', 3 > 5)
print('5 > 3 =', 5 > 3)
#<= menor ou igual
#>= maior ou igual
#== operador logico de igualdade, resulta um valor True ou False
print('15 == 51 =', 15 == 51)
print('15 == 15 =', 15 == 15)
#!= operador logico de diferente, ou não igual a
print('15 != 51 =', 15 == 51)
print('15 != 15 =', 15 == 15)
# not, and, e or são os poreadores logicos booleanos como eles funcionam na logica classica,
#Mudando o topico, existem alguns atalhos associados a certos operadores
# para utilizar recursivamente as variaveis em suas proprias definiçoes
a = 2
print('a =', a)
a = a * 3
print('a = a * 3')
print('a =', a)
#Mesma operação, mas dessa vez utilizando o atalho tanto na adição quanto na multiplicação
b = 4
print('b =', b)
b *= 3
print('b *= 3')
print('b =', b)
b += 3
print('b += 3')
print('b =', b)
# a ordem de prioridades das operações é a seguinte
# lambda : Lambda Expression
# if - else : Conditional expression
# or : Boolean OR
# and : Boolean AND
# not x : Boolean NOT
# in, not in, is, is not, <, <=, >, >=, !=, == : Comparisons, including membership tests and identity tests
# | : Bitwise OR
# ^ : Bitwise XOR
# & : Bitwise AND
# <<, >> : Shifts
# +, - : Addition and subtraction
# *, /, //, % : Multiplication, Division, Floor Division and Remainder
# +x, -x, ~x : Positive, Negative, bitwise NOT
# ** : Exponentiation
# x[index], x[index:index], x(arguments...), x.attribute : Subscription, slicing, call, attribute reference
# (expressions...), [expressions...], {key: value...}, {expressions...} : Binding or tuple display, list display, dictionary display, set display
#hello
