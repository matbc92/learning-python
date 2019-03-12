#dict é uma estrutura definida por um par de colchetes no ao redor de seu conteudo,
# tal estrutura permite associar keys e values(que devem ser definidos seguindo a estrutura key1: value1, key2: value2)
# sendo que keys sao efetivamentes as entradas do dicinoario(uma vez que dict eh abraviação de dictionary)
# e value é o corpo desta entrada, na estrutura dict, keys tem que ser sempre valores imutaveis como strings(aka objetos simples)
# tal restrição nao se aplica a values, todas as keys devem ser unicas.
# itens adicionais podem ser incluidos num dicionario por meio da estrutura nome_do_dicionario[key] = value

# 'ab' is short for 'a'ddress'b'ook

ab = {'Swaroop': 'swaroop@swaroopch.com','Larry': 'larry@wall.org','Matsumoto': 'matz@ruby-lang.org','Spammer': 'spammer@hotmail.com'}

print("Swaroop's address is", ab['Swaroop'])

# Deleting a key-value pair
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])
