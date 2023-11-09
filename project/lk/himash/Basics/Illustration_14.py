# Dictionary :-
# It's hold pair of values at once. First value call Key and other value is Value.
# It's like a Map in Java.
# It's include methods like List.
# Key should be unique.

vehicles = {1: 'Toyota', 2: 'Honda', 3: 'Mitsubishi', 4: 'BMW', 5: 'Audi'}
print(vehicles)

vehicles_multi = {'vehicles': ['Toyota', 'Honda'], 'laptop': ('Dell', 'Asus'), 3: True}
print(vehicles_multi)

print('Dictionary length =============')
print(len(vehicles))

print('Dictionary print keys only =============')
print(vehicles.keys())

print('Dictionary print values only =============')
print(vehicles.values())

print('Dictionary print all items/regular print =============')
print(vehicles.items())

print('Dictionary add element =============')
vehicles[6] = 'Tata'
print(vehicles)

print('Dictionary update element =============')
vehicles[6] = 'Volkswagen'
print(vehicles)

print('Dictionary remove element =============')
vehicles.pop(6)
print(vehicles)

print('Dictionary clear the all element =============')
vehicles.clear()
print(vehicles)

print('Dictionary delete =============')
del vehicles
print(vehicles)
