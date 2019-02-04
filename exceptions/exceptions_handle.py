# a instrução try é usada para criar um bloco de operações similar a um if, mas, ele é especificamente desenhado para lidar come exceções(falhas na execução de algum comando), então no lugar dos else voce colocaria um except(caso nao seja necessario distinguir entre exceções especificas) ou except nomedoerro, para determinar o comportamento do programa de acordo com cada tipo de erro especifico
try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))
