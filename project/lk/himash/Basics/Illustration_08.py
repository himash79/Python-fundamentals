# Inner String manipulation
para_01 = 'friend\'s phone'
print(para_01)
para_02 = "friend's phone"
print(para_02)

# Capilize
print(para_02.capitalize())

# Uppercase
print(para_02.upper())

# lower
print(para_02.lower())

# Utilize string position
print(para_02[1:4])
print(para_02[1:])
print(para_02[:5])

# String replace
print(para_02.replace('phone','bike'))

# String split
print(para_02.split(' '))

# String join
splitValue = para_02.split(' ')
joinValue = ' new '
print(joinValue.join(splitValue))