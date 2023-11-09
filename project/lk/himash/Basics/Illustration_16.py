# While & For loop :
# Its use for iterate records


total = 0
i = 1
while i <= 3:
    number = int(input('Enter number : '))
    total = total + number
    i += 1
print('Sum of number : ', total)

print('For loop ===================')
vehicle_arr = ['Toyota', 'Honda', 'Mitsubishi', 'BMW', 'Audi']
for vehicle in vehicle_arr:
    print(vehicle)

print('For loop range function ===================')
for i in range(1, 10):
    print(i)

print('For loop range function odd numbers ===================')
for i in range(1, 11, 2):  # range(start_index, end_index, step_size)
    print(i)

print('For loop range function even numbers ===================')
for i in range(2, 11, 2):
    print(i)

print('For loop with dictionary ===================')
vehicle_dict = {1: 'Toyota', 2: 'Honda', 3: 'Mitsubishi', 4: 'BMW', 5: 'Audi'}
for i in vehicle_dict.items():
    print(i)

print('For loop with dictionary alternative ===================')
for i, j in vehicle_dict.items():
    print(i, j)

print('For loop with dictionary keys ===================')
for i in vehicle_dict.keys():
    print(i)

print('For loop with dictionary values ===================')
for i in vehicle_dict.values():
    print(i)
