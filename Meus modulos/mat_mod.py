print('''Este modulo eu vou usar para funções que eu criei que eu acho uteis, ou divertidas''')

def pulalinha(quantas=1):
    ''' Printa um numero qualquer de linhas vazias'''
    print('\n' * quantas, end = ' ')

def limpar_string(texto=str):
    '''Retorna uma copia da string alvo sem pontuação'''
    return texto.replace(' ','').replace('','').replace('!','')\
                         .replace('...','').replace('(','').replace(')','')\
                         .replace('[','').replace(']','').replace(',','')\
                         .replace('?','').replace('—','').replace('\'','')\
                         .replace('"','').replace('/','').replace('\\','')\
                         .replace(':','').replace(';','')
