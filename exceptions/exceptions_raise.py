# a afirmação raise, permite que voce inclua numa função uma exceção especifica pre determinada sob circunstancias especificas, e no inicio deste codigo há um exemplo de uma uma exceçao sendo criada com o comando def. além disso dentro do bloco de um comano try é possivel atribuir as propriedades de uma exceçao a uma variavel usando o comando except excessaodeinteresse as nomedavariavel
class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # Other work can continue as usual here
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' +
           '{0} long, expected at least {1}')
          .format(ex.length, ex.atleast))

else:
    print('No exception was raised.')

