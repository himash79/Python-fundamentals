# Arrays :
# It's use for store list of data at once but arrays doesn't store multiple type data.
# Character:c, unicode:u, Signed short:h, Unsigned short:H, Signed int:i, Unsigned int:I,Signed long:l
# Unsigned long:L, float:f, Double:d
# above include array data type and it's type code.

from array import *

arr1 = array('i', [1,-2,3,4,5])
print(arr1)

print('Array print using loop =======================')
for i in arr1:
    print(i)

print('Array print index =======================')
print(arr1[2])

print('Array print index range =======================')
print(arr1[1:4])

print('Array print index range reverse =======================')
print(arr1[-1])

print('Array insert value =======================')
arr1.append(2)
print(arr1)

print('Array insert multiple values =======================')
arr1.extend([6,7,8])
print(arr1)

print('Array insert specific values for position =======================')
arr1.insert(4,1)
print(arr1)

print('Array remove last index =======================')
arr1.pop()
print(arr1)

print('Array remove specific index =======================')
arr1.pop(1)
print(arr1)

print('Array remove specific value =======================')
arr1.remove(7)
print(arr1)

print('Array add into new array =======================')
arr2 = array('i', [7,8,9,10])
arr3 = arr1 + arr2
print(arr3)