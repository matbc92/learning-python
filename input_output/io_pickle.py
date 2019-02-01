# pickle é um modulo que armazena arquivos de forma semicompilada para que possam ser lidos e alterados pelo programa em qualquer sistema operacionasl, ele difere do modulo marshall prinicipalmente no quesito de que ele faz esse aramazenamento de forma persistente
import pickle

# The name of the file where we will store the object
shoplistfile = 'shoplist.data'
# The list of things to buy
shoplist = ['apple', 'mango', 'carrot']

# Write to the file
f = open(shoplistfile, 'wb')
# Dump the object to a file
pickle.dump(shoplist, f)
f.close()

# Destroy the shoplist variable
del shoplist

# Read back from the storage
f = open(shoplistfile, 'rb')
# Load the object from the file
storedlist = pickle.load(f)
print(storedlist)
f.close()
