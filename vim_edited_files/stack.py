from pythonds.basic import Stack
m = Stack()
m.push('x')
m.push('y')
m.push('z')
m.push('z')
while not m.isEmpty():
   m.pop()
   m.pop()
def invert_string_using_stacks(string_to_reverse):
    if not isinstance(string_to_reverse, str):
        string_to_reverse = str(string_to_reverse)
    reversor=Stack()
    reversed_string = ''
    reversing_step = []
    for i in string_to_reverse:
        reversor.push(i)
    while not reversor.isEmpty():
        reversing_step.append(reversor.pop())
    reversed_string= ''.join(reversing_step)
    return reversed_string

print(invert_string_using_stacks('acararajadadajararaca'))

