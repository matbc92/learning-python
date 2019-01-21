#programinha pra facilitar meus commmits
import os
if os.system('git add .') == 0:
    print('files added')
else:
    print('failed to add files')
messange = input('Insira o comment:')
# por alguma razão os caracteres de espaço
# resultantes da função input causam problemas
# quando importados para o shell, portanto precisei
# substituir eles por '\ '
if os.system('git commit --m {}'.format(messange.replace(' ','\ '))) == 0:
    print('files commited')
else:
    print('failed to commit files')
os.system('git push')
1
