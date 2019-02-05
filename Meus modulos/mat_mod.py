print('''Este modulo eu vou usar para funções que eu criei que eu acho uteis, ou divertidas''')

def pulalinha(quantas=1):
    ''' Printa um numero qualquer de linhas vazias'''
    print('\n' * quantas, end = ' ')

def limpar_string(texto, pontuação=True, espaço=True, case=True):
    '''Retorna uma copia da string alvo sem pontuação'''
    import string
    if case:
        texto = texto.lower()
    if espaço:
        texto = texto.replace(' ', '')
    if pontuação:
        texto = texto.translate(str.maketrans({key: None for key in string.punctuation}))
    return texto
