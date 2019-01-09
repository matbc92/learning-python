# a propriedade __name__ num modulo é particularmente relevante,
# pois ela diferencia se um modulo está sendo executado
# de forma standalone, ou seja
# o arquivo que contem seu codigo é o arquivo sendo executado,
# neste caso o __name__ do seu modulo é por default definido como
# __main__, caso este modulo seja importado para outro codigo,
# o __name__ do mudlo sera definido pelo nome do arquivo, portano
# esta propriedade pode ser utuilizada no codigo do modulo para diferenciar
# o seu comprotamento entre standalone e importado
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
