def divide_by_2(dec_number):
    remstack = []
    while dec_number > 0:
        rem = dec_number%2
        remstack.append(rem)
        dec_number = dec_number // 2

    binstring = ""
    #the next statement is simplification of while not len(remstack) ==0:
    while remstack:
        binstring += str(remstack.pop())
    return binstring
print(divide_by_2(13))
