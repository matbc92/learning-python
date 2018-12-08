#if condiciona o programa a executar um bloco de instruções se certas condições forem atendidas e outro(s) se condições diferentes ocorrerem
numero = 30
chute = int(input('Chute um numero: '))

if chute == 1:
    print('Um? Não acha meio obvio? Tente um número um pouco maior')
elif chute == 2:
    print('Dois? mas dois é tão obvio, tente um número maior')
elif chute == 3:
    print('três, mas que numero mais bobo tente um pouquinho maior')
elif chute < numero:
    print('hmmm... não é esse, tente um numero maior')
elif chute == numero:
    print('parabens voce acertou, aqui está seu vale biscoito imaginário')
else:
    print('voce passou, tente um numero um pouco menor')
