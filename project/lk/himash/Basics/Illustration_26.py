# Factorial :
# This is the given value multiply given values times.

result = 1
startIndex = 1
factorialValue = int(input('Enter number : '))

for i in range(startIndex, factorialValue + 1):
    result = result * i
print(result)

print('Factorial numbers with recursion')

def factRecur(num):
    if num == 0:
        return 1
    else:
        return num * factRecur(num - 1) # recursion the method till getting output
print(factRecur(4))