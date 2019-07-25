def parenthesis_balancing(symbol_string):
    stack=[]
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
           stack.append(symbol)
        else:
            if len(stack) == 0:
                balanced = False
            else:
                stack.pop()
        index += 1
    if balanced and  len(stack) == 0:
        return True
    else:
        return False

print(parenthesis_balancing('(())'))
