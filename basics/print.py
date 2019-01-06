# afunção print normalmente termina com um comando \n, isso pode ser manualmente suprimido
# ao colocar fora da strig a ser printada o comando end='carcter a substituir o \n'
print('a', end='')
print('b', end='')
print('c \n' 'abc')
print('\na', end=' ')
print('b', end=' ')
print('c')
print('\n'r'\ nao funciona dentro de raw strings, que são''\n' r'inciadas por r, antes do comando de string')

r''
