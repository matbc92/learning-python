#  se assinala um objeto a uma variavel, esta variavel vai se referir ao objeto,
#  ou seja, qualquer operação direcionada a variavel sera exercida sobre o objeto,
#  por conta disto se a intenção é copiar os valores de uma lista a uma outra variavel
#  o adequado é utilizar uma função slice encapsulando a sequencia toda ou a função .copy

print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist is just another name pointing to the same object!
mylist = shoplist

# I purchased the first item, so I remove it from the list
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# Notice that both shoplist and mylist both print
# the same list without the 'apple' confirming that
# they point to the same object

print('Copy by making a full slice')
# Make a copy by doing a full slice
mylist = shoplist[:]
# Remove first item
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# Notice that now the two lists are different

conjuntoloko = set([1, 5, 6, 9, 22])
subconjuntoloko = set([9, 22])
print(conjuntoloko.issuperset(subconjuntoloko))
