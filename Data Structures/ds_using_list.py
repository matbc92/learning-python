#list é uma estrutura de dados(definida por pares de colchetes)
# que permite se armazenar uma sequencia de objetos com ordem preservada,
# em associação com a estrutura list pode se usar diversas funções especificas
# a listas(cuja estrutura consiste da notação, nome da variavel_dado_a_lista.função)
# dentre eles a função .appen() que inclui no fim da lista os valores aplicados na função
# ja a função .sort() organiza a lista em ordem crescente/alfabetica, dependendo da natureza
# dos objetos, podendo ser invertida com o uso do parametro
# reverse(que por default é definido como false) além disso o parametro
# key que por default é vazio, pode ser preenchido por uma
# função a ser aplicada a cada um dos itens da lista e
# a ordenação da lista é feita baseada no resultado da aplicação
# daquela função

# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist,'\n')

lista_para_ser_ordenada_por_comprimento = ['zé','antigamente','basico','comprido','cinco']
print('lista crua',lista_para_ser_ordenada_por_comprimento, '\n')
lista_para_ser_ordenada_por_comprimento.sort()
print('lista ordenada pelo sort()', lista_para_ser_ordenada_por_comprimento, '\n')
lista_para_ser_ordenada_por_comprimento.sort(key = len)
print('lista ordenada pelo sort(key = len), ou seja ordenada de acordo com o comprimento', lista_para_ser_ordenada_por_comprimento)
