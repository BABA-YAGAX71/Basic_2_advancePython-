import os
import pathlib

with open('e:/Ostad/Python_Basic_course/name.txt', 'r') as f:
    content = f.read()
    print(content)


# write in a file

line = ['\n I love python']

with open('e:/Ostad/Python_Basic_course/name.txt', 'a') as f:
    content = f.writelines(line)


if os.path.exists('test.txt'):
    print('File exists')
else:
    print('file not found')

if os.path.exists('e:/Ostad/Python_Basic_course/name.txt'):
    print('File found')
else:
    print('File is not found')     

print(os.path.abspath('e:/Ostad/Python_Basic_course/name.txt'))
print(os.path.getsize('e:/Ostad/Python_Basic_course/name.txt'))

with open('e:/Ostad/Python_Basic_course/name.txt', 'r') as f:
    print(f.read(5))
