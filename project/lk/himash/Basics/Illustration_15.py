# Slicing and Negative Indexing :-
# Slicing means divide list/tuple/dictionary
# Slice syntax :- listName[startIndex+1 : lastIndex+1]
# Require the next index value otherwise doesn't display the expected result
# Negative indexing means able to reverse arrange list/tuple/dictionary using negative index
# Able access list values using negative indexes
# It's counting value end of list

vehicle_arr = ['Toyota','Honda','Mitsubishi','BMW','Audi']
print(vehicle_arr)

print('slice =================')
print(vehicle_arr[1:2])

print('slice alternative 02 =================')
print(vehicle_arr[:3])

print('slice alternative 03 =================')
print(vehicle_arr[3:])

print('slice display even records =================')
print(vehicle_arr[1::2])

print('slice display odd records =================')
print(vehicle_arr[::2])

print('negative index select value =================')
print(vehicle_arr[-2])

print('negative index select value =================')
print(vehicle_arr[-2])

print('negative index =================')
print(vehicle_arr[-3:-1])

print('negative index alternative 02 =================')
print(vehicle_arr[:-3])

print('negative index alternative 03 =================')
print(vehicle_arr[-3:])

print('negative index display even records =================')
print(vehicle_arr[-4::2])

print('negative index display odd records =================')
print(vehicle_arr[::2])

print('negative index revese list =================')
print(vehicle_arr[::-1])