# Modulos sao arquivos que serem para armazenar funções e variaveis
# para serem utilizadas em diversos programas diferentes, porem em pirmeira instancia
# as funções e variaveis importadas só podem ser utilizadas por meio da
# estrutura 'nome da fonte da importação'.'variavel/função desejada', a não ser
# a função ou variavel seja importada diretamene para seu programa
# por meio da estrutra from 'fonte da importação' import 'função/variavel desejada'
import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

print(sys.version)

from math import sqrt
print("Square root of 16 is", sqrt(16))
