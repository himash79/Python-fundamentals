# Generators :
# When method behavior like iterator then provide generate function.

def fetchResult():
    initValue, endValue = 0, 1
    while True:
        sum = initValue + endValue
        yield initValue
        initValue, endValue = endValue, sum

obj = fetchResult()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
