# Sets :-
# It's not allow duplicates
# It's not allow insertion order
# It's include methods same as list
# It's not allow fetch specific value using index
# It's not allow inner sets of set
# It's not allow combine sets like list and tuple

vehicle_set = {'Toyota','Honda','Mitsubishi','BMW','Audi'}
print(vehicle_set)

common_set = {1,10,True,'H','Customer name',10.5}
print(common_set)

print('Set length =============')
print(len(vehicle_set))

print('Set add element =============')
vehicle_set.add('Volkswagen')
print(vehicle_set)

print('Set add multiple element =============')
vehicle_set.update(['Tata','BENZ'])
print(vehicle_set)

print('Set convert tuple/list =============')
vehicle_tuple = ('Toyota 2','Honda 2','Mitsubishi 2','BMW 2','Audi 2')
updated_vehicle_set = set(vehicle_tuple)
print(updated_vehicle_set)

print('Set fetch intersection in sets =============')
set_01 = {1,4,3,5,7,8}
set_02 = {2,3,4,6,1,5,9}
print(set_01 & set_02)
print(set_01.intersection(set_02))

print('Set fetch union in sets =============')
set_01 = {1,4,3,5,7,8}
set_02 = {2,3,4,6,1,5,9}
print(set_01 | set_02)
print(set_01.union(set_02))


print('Set remove element =============')
vehicle_set.remove('Tata')
print(vehicle_set)

print('Set clear =============')
vehicle_set.clear()
print(vehicle_set)

print('Set delete =============')
del vehicle_set
print(vehicle_set)