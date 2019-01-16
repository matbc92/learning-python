import os
if os.system('git add .') == 0:
    print('files added')
else:
    print('failed to add files')
mensage = input()
if os.system('git commit --m {}'.format(mensage)) == 0:
    print('files commited')
else:
    print('failed to commit files')
