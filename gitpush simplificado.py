import os
if os.system('git add .') == 0:
    print('files added')
else:
    print('failed to add files')
messange = input()
messange.replace(' ', '\ ')
if os.system('git commit --m {}'.format(messange.replace(' ','\ '))) == 0:
    print('files commited')
else:
    print('failed to commit files')
