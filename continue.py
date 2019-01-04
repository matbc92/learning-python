# continue é uma função que instrui o programa a retornar ao inicio do loop em que ele esta inserido
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')
