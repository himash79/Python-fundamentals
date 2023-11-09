# Continue & Break statement
# Continue provides skip the state of that inside loop
# Break provides stop and return the specific value of that inside loop

print('For loop continue ===================')
vehicle_arr = ['Toyota', 'Honda', 'Mitsubishi', 'BMW', 'Audi']
for vehicle in vehicle_arr:
    if vehicle == 'BMW':
        continue
    print(vehicle)

print('while loop continue ===================')
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)

print('while loop break ===================')
vehicle_arr = ['Toyota', 'Honda', 'Mitsubishi', 'BMW', 'Audi']
for vehicle in vehicle_arr:
    if vehicle == 'BMW':
        break
    print(vehicle)

print('while loop break ===================')
x = 0
while x < 5:
    x += 1
    if x == 3:
        break
    print(x)