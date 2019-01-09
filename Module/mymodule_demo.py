# uma forma de importar todos os nomes publicos de um modulo
# é utilizando a estrutura from... import porem utilizando
# um asteristico no fim de import, porém nomes iniciados com
# certos caracteres(como underscore) não sao importados desta maneira
import mymodule

mymodule.say_hi()
print('Version', mymodule.__version__)

from mymodule import *

import importlib
import sys
print(vars(importlib))
