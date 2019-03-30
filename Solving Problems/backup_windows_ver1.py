import os
import time
import shutil
# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
# source = ['"C:\\My Documents"']
# Example on Mac OS X and Linux:
source = 'C:\\Users\\Matheus\\Desktop'
# Notice we have to use double quotes inside a string
# for names with spaces in it.  We could have also used
# a raw string by writing [r'C:\My Documents'].

# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
# target_dir = 'E:\\Backup'
# Example on Mac OS X and Linux:
target_dir = 'C:\\backup_do_desktop'
# Remember to change this to which folder you will be using
# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time# 4. The current day is the name of the subdirectory
# in the main directory.
today = (target_dir + os.sep + time.strftime('%d-%m-%Y'))
# The current time is the name of the zip archive.
now = time.strftime('%H-%M-%S')

# Take a comment from the user to
# create the name of the zip file
comment = input('Enter a comment --> ')
# Check if a comment was entered
if len(comment) == 0:
    target = today + os.sep + now
else:
    target = today + os.sep + now + '_' +\
             comment


# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

shutil.make_archive(target, 'zip', source)