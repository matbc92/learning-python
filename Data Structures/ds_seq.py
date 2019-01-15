# listas strings e tuples, são sequencias, uma vez que sequencias sao conjuntos ordenados
# uma vez que eles sao ordenados pode se utilizar uma operação chamada slicing,
# ou seja selecionar apenas alguns itens desta sequencia, para tanto é necessario dizer
# a posição do primeiro e do ultimo item que se quer slecionar e por fim, opcionalmente o step,
# ou seja de quantos em quantos itens serao selecionados

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# Slicing on a string #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:],'\n')

print('shoplist com step 1, ou seja padrão',shoplist[::1],'\n')
print('shoplist com step 2',shoplist[::2],'\n')
print('shoplist com step 3',shoplist[::3], '\n')
print('shoplist com step -1 ou seja em reverso',shoplist[::-1])


