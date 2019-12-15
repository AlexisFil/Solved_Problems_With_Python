'''Objective
Write the current directory and its containing files in a .txt
Using os module
'''

import os
location=os.path.abspath(os.curdir)
target1=f'The current file is located at path: \n {location}\n'
target2 =os.listdir(os.curdir)

with open ('Location_info.txt','w',encoding='utf-8') as f:
    f.write(target1)
    f.write('\nIt contains: \n\n')
    for i in target2:
        f.write(i)
        f.write('\n')

