cartão ='''Este modulo eu vou usar para funções que eu criei que eu acho uteis, ou divertidas'''

def pulalinha(quantas=1):
    ''' Printa um numero qualquer de linhas vazias'''
    print('\n' * quantas, end = ' ')

def limpar_string(texto, pontuação=True, espaço=True, caixa=True, apostrofe=False):
    '''Retorna uma cópia da string sem ponuações e/ou sem o character espaço e/ou toda em caixa baixa
    por default a função é programada '''
    import string
    if apostrofe:
        texto = texto.repalce('\'', 'xxxxapostrofexxxx')
    if caixa:
        texto = texto.lower()
    if espaço:
        texto = texto.replace(' ', '')
    if pontuação:
        texto = texto.translate(str.maketrans('', '', string.punctuation))
    return texto
