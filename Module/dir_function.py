# a função dir, permite visualizar
# os atributos, funções importadas, variaveis definidas, funções definidas
# no programa atual, utilizando a função sem argumentos,
# ou em um modulo especifico, bem como os atributos de uma função,
# utilizando cada um deles como arumentos respectivamente
# bonus stuff: para re-executar um modulos(assim como quando ele é importado)
# pode se usar a função reload do modulo importlib
import sys
from importlib import reload
import this
def pulalinha():
    print('\n \n')
pulalinha()


import module_using_name

pulalinha()

reload(this)

pulalinha()

reload(module_using_name)

pulalinha()

a = 5
print(dir())
pulalinha()
print(dir(reload))
pulalinha()
print(dir(sys))
pulalinha()
print(dir(pulalinha()))
