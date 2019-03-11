import random

def genereate_one(strlen):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]
    return res
def score(goal, test_string):
    num_same = 0
    for i in range(len(goal)):
        if goal[i] == test_string[i]:
            num_same += 1
    return num_same / len(goal)
string_analyzed = genereate_one(28)
print(score('methinks it is like a weasel', string_analyzed))
print(string_analyzed)


def main():
    goalstring = 'methinks it is like a weasel'
    newstring = genereate_one(28)
    best = 0
    newscore = score(goalstring,newstring)
    while newscore < 1:
        if newscore > best:
            print(newscore, newstring)
            best = newscore
        newstring = genereate_one(28)
        newscore = score(goalstring,newstring)

main()
