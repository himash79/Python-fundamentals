# Pattern printing :

print('example 01 ==============================')
no01 = 5
for i in range(no01): # declair the rows
    for j in range(i + 1): # declair the columns
        print('* ', end='') # print value, without 'end' value display each row
    print('')

print('example 02 ==============================')
no02 = 5
for i in range(no02):
    for j in range(no02 - i):
        print('* ', end='')
    print('')

print('example 03 ==============================')
no03 = 5
for i in range(no03):
    for j in range(no03 - i - 1):
        print('$ ', end='')
    for k in range(i + 1):
        print('* ', end='')
    for l in range(i + 1):
        print('% ', end='')
    for m in range(no03 - i):
        print('@ ', end='')
    print(' ')

print('example 04 ==============================')
no04 = 5
for i in range(no04):
    for j in range(no04 - i - 1):
        print(' ', end='')
    for k in range(i + 1):
        print('* ', end='')
    print(' ')

print('example 05 ==============================')
rows = 6
columns = 7
for row in range(rows):
    for column in range(columns):
        if row == 0 and column%3 != 0:
            print('* ', end='')
        elif row == 1 and column%3 == 0:
            print('* ', end='')
        elif row - column == 2:
            print('* ', end='')
        elif row + column == 8:
            print('* ', end='')
        else:
            print('  ', end='')
    print()