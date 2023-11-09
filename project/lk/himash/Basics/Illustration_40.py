# Random library :
# Generate random numbers and patterns

import random

print('random number')
value = random.random()
print(value)

print('random number with range')
value = random.uniform(1, 10)
print(value)

print('random integer number with range')
value = random.randint(1, 10)
print(value)

print('random picker')
users = ['Perera', 'Dias', 'Costa']
randomUser = random.choice(users)
print(randomUser)

print('random multiple picker')
users = ['Perera', 'Dias', 'Costa', 'Bandara']
randomUsers = random.choices(users, k=2)
print(randomUsers)

print('shuffle')
users = ['Perera', 'Dias', 'Costa', 'Bandara']
random.shuffle(users)
print(users)

