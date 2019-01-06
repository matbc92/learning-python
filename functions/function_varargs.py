# é possivel numa função criar um parametro com numero de argumentos variavel
# para tanto, pode se iniciar um parametro com *, o que faz com que
# todos os argumentos posicionais daquele ponto em diante sejam agrupados em um tuplo
# com o nome do parametro inciado por *, se inciar o nome do parametro com
# **, todos os parametros nomeados(nao estabelcidos pela função) daquele ponto em diante
# seram agrupados em um dicionario com o nome do parametro inciado pelos **
def total(a=5, *numbers, **phonebook):
    print('a', a)

    #iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)

    #iterate through all the items in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
total(10,1,2,3,Jack=1123,John=2231,Inge=1560)
