import time
f = open('poem.txt')
for _ in range(5):
    print('.', end='', flush=True)
    time.sleep(0.5)
print(' Pronto!')
f.close
