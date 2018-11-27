# + adiciona dois itens(opratarios, ou operand)
print('3 + 5 = ' + str(3 + 5))
print("'a' + 'b' = " + 'a' + 'b')
# - subtrai dois itens, se o primeiro item estiver omisso, ele é assumido zero
# * multiplica dois numeros, ou repete uma string x vezes
print("'la' * 3 = " + 'la' * 3)
# ** executa uma potenciação
print('3 ** 4 = ' + str(3 ** 4))
# / divide
#// faz uam divisão excluindo o zero
print('7 // 2 = ' + str(7 // 2))
#% divisao modulo, mostra o resto da divisão
print('7 % 2 = ' + str(7 % 2))
#<< é um left shift, ele pega o valor do numero em binario e move os digitos um numero determinado de casas para a esquerda
print('1 << 5 = ' + str(1 << 5))
#>> é um right shift, o mesmo que o left shift só que pro outro lado
print('32 >> 5 = ' + str(32 >> 5))
#& and bit-wise ele compara o valor binario dos dois elementos, resultando num terceiro valor binario
# que exprime 1 em todas as casas que os dois valores anteriores sejam iguais e zero no restante
#| bit-wise or ele compara o valor binario dos dois elementos, resultando num terceiro valor binario
# que exprime 1 em todas as casas que o valor de pelo menos um dos elementos seja 1 e zero nas outras
#^ bit-wise or ele compara o valor binario dos dois elementos, resultando num terceiro valor binario
# que exprime 1 em todas as casas que o valor de somento um dos elementos seja 1 no restante zero
#~bitwise invert alterna todos os digitos do valor binario de um elemento,
# tal operação conicide com a a operaçao de -(x+1) sendo x o valor a ser invertido
#< operador de menor do que, resulta um valor True ou False booleano
print('3 < 5 = ' + str(3 < 5))
print('5 < 3 = ' + str(5 < 3))
#>maior que, o oposto de menor que
print('3 > 5 = ' + str(3 > 5))
print('5 > 3 = ' + str(5 > 3))
#<= menor ou igual
#>= maior ou igual
#== operador logico de igualdade, resulta um valor True ou False
print('15 == 51 = ' + str(15 == 51))
print('15 == 15 = ' + str(15 == 15))
#!= operador logico de diferente, ou não igual a
print('15 != 51 = ' + str(15 == 51))
print('15 != 15 = ' + str(15 == 15))
