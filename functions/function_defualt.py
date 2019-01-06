# é possivel atribuir um valor padrão a um parametro, para o
# caso de o usuario não o especificar,
# isto é feito no momento que o parametro é introduzido,
# por meio da inclusão de (=) adjunto do valor pardão desejado
def say(message, times=1):
    print(message * times)

say('Hello')
say('World', 5)
