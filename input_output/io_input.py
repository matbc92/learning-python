# programa simples com duas funções definidas,
# uma que inverte uma string de texto, usando um operador sobre sequencias
# que inverte a ordem, e uma função que utiliza esta função de
# reversão para testar se a string é palindromica ao comparar
# com o resultado da função que inverte o texto

def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something.replace(' ','').replace('','').replace('!','')\
                         .replace('...','').replace('(','').replace(')','')\
                         .replace('[','').replace(']','').replace(',','')\
                         .replace('?','').replace('—','').replace('\'','')\
                         .replace('"','').replace('/','').replace('\\','')\
                         .replace(':','').replace(';','')):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
