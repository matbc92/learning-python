# programa simples com duas funções definidas,
# uma que inverte uma string de texto, usando um operador sobre sequencias
# que inverte a ordem, e uma função que utiliza esta função de
# reversão para testar se a string é palindromica ao comparar
# com o resultado da função que inverte o texto

def reverse(text):
    return text[::-1]


def is_palindrome(text=str):
    import string
    text = text.replace(' ', '').lower().translate(str.maketrans({key: None for key in string.punctuation}))
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
