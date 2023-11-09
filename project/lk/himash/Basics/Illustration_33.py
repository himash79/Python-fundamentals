# Iterators :
# It's use for loop/iterate the data in collections.
# It's able to use Set and tuple, list even arrays.

list = {3,4,5,6,7,8}
itr = iter(list)
while True:
    try:
        print(next(itr))
    except Exception:
        break

print('Create own iterator ======================')
class customerItr:
    def __init__(self):
        self.initValue = 2
    def __iter__(self):
        return self
    def __next__(self):
        value = self.initValue
        self.initValue += 2
        return value

cItrObj = customerItr()
itr = iter(cItrObj)
print(next(cItrObj))
print(next(cItrObj))
print(next(cItrObj))