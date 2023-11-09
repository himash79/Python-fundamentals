vehicle_arr = ['Toyota','Honda','Mitsubishi','BMW','Audi']
print(vehicle_arr)

common_arr = [1,10,True,'H','Customer name',10.5,['0001','himash.s','XXX']]
print(common_arr)

print('Array init with specific index =============')
a,b,c = [1,2,3]
print(a)
print(b)
print(c)

print('Array init with specific index when no init values =============')
a,b,*c = [1,2,3,4,5]
print(a)
print(b)
print(c)

print('Array combine ============')
combined_arr = vehicle_arr + common_arr
print(combined_arr)

print('Array length =============')
print(len(vehicle_arr))

print('Array check value exist =============')
print('XXX' in vehicle_arr)

print('Array update specific index value =============')
vehicle_arr[1] = 'Volkswagen'
print(vehicle_arr)

print('Array add value for specific index =============')
vehicle_arr.insert(3,'BENZ')
print(vehicle_arr)

print('Array add value for last index =============')
vehicle_arr.append('TATA')
print(vehicle_arr)

print('Array sort ASC =============')
vehicle_arr.sort()
print(vehicle_arr)

print('Array sort ASC 2 =============')
vehicle_arr.sort(reverse=False)
print(vehicle_arr)

print('Array reverse =============')
vehicle_arr.sort(reverse=True)
print(vehicle_arr)

print('Array remove last index value =============')
vehicle_arr.pop()
print(vehicle_arr)

print('Array remove specific value =============')
vehicle_arr.remove('Toyota')
print(vehicle_arr)

print('Array clear all values =============')
vehicle_arr.clear()
print(vehicle_arr)

print('Array delete =============')
del vehicle_arr
print(vehicle_arr)