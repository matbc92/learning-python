def reverse(text):
    return text[::-1]


def is_palindrome(text=str):
    from mat_mod import limpar_string
    text = limpar_string(text)
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
