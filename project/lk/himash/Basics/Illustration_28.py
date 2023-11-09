# Decorators
# It's use for if method require method value change without change the method body that methods call decorator methods.

def validate(func):
    def validateValues(userId):
        if userId != 1 and userId != 2:
            return func(userId)
        else:
            return func(0)
    return validateValues


@validate
def fetchUserDetails(userId):
    if userId == 1:
        userName = 'Username 01'
    elif userId == 2:
        userName = 'Username 02'
    else:
        userName = 'Invalid input'
    return userName

print(fetchUserDetails(4))
