#if condiciona o programa a executar um bloco de instruções se certas condições forem atendidas
#  e outro(s) se condições diferentes ocorrerem, as condições diferentes podem ser especificadas
# por meio do comando elif, que efetivamente cria um outro nó de if, ou simplesmente permanecerem
# como qualquer coisa diferente da condição determinada por if
########################################################################
#já o comando while, separa um bloco de texto que será repetido enquanto o parametro determinado,
# seja verdadeiro, ou que um comando de break aconteça, uma vez que o parametro se torna falso,
# o programa retorna ao bloco de texto no qual o while está inserido(isto também é valido para o if),
# a não ser que o comando else seja utilizado, sendo assim as instruções dentro deste comando seram executadas
# antes do programa retornar ao bloco de codigo anterior.
numero = 30
running = True
while running:
    chute = int(input('Tente adivinhar o número secreto: '))

    if chute == 1:
        print('Um? Não acha meio obvio? Tente um número um pouco maior')
    elif chute == 2:
        print('Dois? mas dois é tão obvio, tente um número maior')
    elif chute == 3:
        print('três, mas que numero mais bobo tente um pouquinho maior')
    elif chute < numero:
        print('hmmm... não é esse, tente um numero maior')
    elif chute > numero:
        print('voce passou, tente um numero um pouco menor')
    else:
        print('parabens voce acertou, aqui está seu vale biscoito imaginário')
        running = False
else:
    print('o jogo terminou')
