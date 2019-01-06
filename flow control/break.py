# break eh um comando que interrome um loop de while ou for, executando na sequencia
#  o restante do codigo do bloco em que loop foi inserido,
#  ou seja caso haja algum else incluso no while/for, ele sera ignorado
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')
