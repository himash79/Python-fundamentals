# Exception handling :
# It's use for indicate proper error for client and code level.
# It's able to use try, execpt, finnaly blocks.

try:
    no01 = int(input('Enter value : '))
    no02 = int(input('Enter value : '))
    print(no01/no02)
except ZeroDivisionError as e:
    print('Invalid input value ', e)
except ValueError as e:
    print('Value should be number ', e)
except Exception as e:
    print('Expectation failed ', e)
finally:
    print('function finished successfully')