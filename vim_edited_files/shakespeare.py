import random
random_weird_thing = []
shakesperian_string = []
def sentence_attempt():
    for w in range(28):
        random_weird_thing.append(random.randint(1,27)) 
    for item in random_weird_thing:
        if item==1:
           shakesperian_string.append('q')
        elif item==2:
                   shakesperian_string.append('w')
        elif item==3:
                   shakesperian_string.append('e')
        elif item==4:
                   shakesperian_string.append('r')
        elif item==5:
                   shakesperian_string.append('t')
        elif item==6:
                   shakesperian_string.append('y')
        elif item==7:
                   shakesperian_string.append('u')
        elif item==8:
                   shakesperian_string.append('i')
        elif item==9:
                   shakesperian_string.append('o')
        elif item==10:
                   shakesperian_string.append('p')
        elif item==11:
                   shakesperian_string.append('a')
        elif item==12:
                   shakesperian_string.append('s')
        elif item==13:
                   shakesperian_string.append('d')
        elif item==14:
                   shakesperian_string.append('f')
        elif item==15:
                   shakesperian_string.append('g')
        elif item==16:
                   shakesperian_string.append('h')
        elif item==17:
                   shakesperian_string.append('j')
        elif item==18:
                   shakesperian_string.append('k')
        elif item==19:
                   shakesperian_string.append('l')
        elif item==20:
                   shakesperian_string.append('z')
        elif item==21:
                   shakesperian_string.append('x')
        elif item==22:
                   shakesperian_string.append('c')
        elif item==23:
                   shakesperian_string.append('v')
        elif item==24:
                   shakesperian_string.append('b')
        elif item==25:
                   shakesperian_string.append('n')
        elif item==26:
                   shakesperian_string.append('m')
        else:
            shakesperian_string.append(' ')
    return (''.join(shakesperian_string))
sentence = sentence_attempt()
print(sentence)
