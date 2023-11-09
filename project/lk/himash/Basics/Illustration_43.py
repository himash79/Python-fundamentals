# OS module :
# This module provide interact with developer machine data and perform functions.

import os

print('Current working directory ==============================')
print(os.getcwd())

print('Change working directory ==============================')
os.chdir(r'E:\Github\pythonProject\project')
os.chdir('E:/Github/pythonProject/project')
print(os.getcwd())

print('Display files on working directory ==============================')
print(os.listdir())

print('Make working directory ==============================')
os.mkdir('ABC')

print('Rename working directory ==============================')
os.rename('ABC', '123')

print('Remove working directory ==============================')
os.rmdir('123')