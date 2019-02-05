import time
while True:
    print('hello', flush=True)
    time.sleep(0.4)
    test = input('Type')
    if test.lower() == 'help' or test.lower() == 'get me out of here':
        break
