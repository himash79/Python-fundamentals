# Tuples :-
# Unable to update specific value
# Provide security more than list
# Available manipulation speed more than list
# Its doesn't include methods more than list
# Able to fetch value using index

vehicle_tuple = ('Toyota','Honda','Mitsubishi','BMW','Audi')
print(vehicle_tuple)

common_tuple = (1,10,True,'H','Customer name',10.5,('0001','himash.s','XXX'))
print(common_tuple)

print('Tuple fetch value using index ============')
print(vehicle_tuple[0])

print('Tuple combine ============')
combined_tuple = vehicle_tuple + common_tuple
print(combined_tuple)

print('Tuple length =============')
print(len(vehicle_tuple))

print('Tuple when have one element should like this otherwise display as int/string =============')
int_tuple = ('Java',)
print(int_tuple)