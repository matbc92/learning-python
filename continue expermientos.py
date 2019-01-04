parametro = True
while parametro:
    coisa = input('continue a frase: coisa...')
    if coisa == 'boa':
        print('é legal mesmo não é?')
    elif coisa == 'ruim':
        print('poxa, ta dificil eim?')
    elif coisa == 'não sei':
        print('poxa pense em algo')
        continue
    elif coisa == 'cansei':
        break
    else:
        print('de fato uma coisa')
    print('vamos outra vez?')
print('tchau')
