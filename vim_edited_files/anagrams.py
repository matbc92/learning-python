def anagramSolution1(s1,s2):
    if len(s1) != len(s2):
        stillOK = False

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == s2[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            s2[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

print(anagramSolution1('ovo','oov'))
