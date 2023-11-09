# Lambda function :
# It's reduce the code length same as other languages.
# But there are few different syntax availale.

print('Lambda example 01 ================================')
sum = lambda amount, fee: amount + fee
print(sum(100,50))

print('Lambda example 02 ================================')
def calculateAmount(fee):
    return lambda netAmount: netAmount + fee
grossAmount = calculateAmount(50)
print(grossAmount(100))

