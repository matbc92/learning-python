def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = []

    while decNumber > 0:
        rem = decNumber % base
        remstack.append(rem)
        decNumber = decNumber // base

    newString = ""
    while remstack:
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(25,8))
print(baseConverter(26,26))

