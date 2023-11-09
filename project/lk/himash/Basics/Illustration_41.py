# Zip function :
# If require the combine multiple list for same list/tuple/set/dictionary able to use this.

userIds = [1,2,3,4]
users = ['perera','amal', 'nimal', 'shanaka']
locations = ['boralla','dehiwala', 'gothatuwa', 'rajagiriya']

print('Zip list ======================')
zipList = list(zip(userIds,users,locations))
zipSet = set(zip(userIds,users,locations))
zipTuple = tuple(zip(userIds,users,locations))
zipDict = dict(zip(userIds,users))
print(zipList)
print(zipSet)
print(zipTuple)
print(zipDict)

print('Unzip list ======================')
unZipList = list(zip(*zipList))
unZipSet = set(zip(*zipSet))
unZipTuple = tuple(zip(*zipTuple))
# unZipDict = dict(zip(*zipDict))
print(unZipList)
print(unZipSet)
print(unZipTuple)
# print(unZipDict)