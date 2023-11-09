# Regular expressions :
# \ signals a special sequence
# [] a set of characters
# . any charactor
# ^ start with
# $ ends with
# * zero or more occurrence
# + one or more occurrence
# {} exactly the specific number of occurrences
# \d 0-9
# \w A-Za-z0-9
# \W not \w
# \s white space
# \S not \s
# {n} exact n occurrence
# {min, max} min-max occurrence
# + 1 or more occurrences
# ? 0 or  occurrences

import re

sentence = 'Hello my world, this is 3000, any issues ?, the number is +94753465516, '

print('FindAll ============================')
regex = re.findall('.\d{11}', sentence)
print(str(regex).replace('+94', '0'))

print('Search ============================')
regex = re.search('issues', sentence)
print(regex)

print('Split ============================')
regex = re.split(',', sentence)
print(regex)

print('Sub ============================')
regex = re.sub('issues', 'problem', sentence)
print(regex)