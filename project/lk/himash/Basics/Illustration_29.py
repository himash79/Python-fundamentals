# Polymorphism :
# It's able to change super class method implementation.
# Same as other language concept.
# Method overloading means one code implement different forms.
# this one doesn't work like other languages, implement same couple of method declaration with different parameters.
# Abstraction means hide the internal process from user.

print('Method overriding example =========================')
class Samsung:
    def getModel(self):
        return 'I phone XS'

class Mobile(Samsung):
    def getModel(self):
        return 'Galaxy S23'

mobileObj = Mobile()
print(mobileObj.getModel())

print('Method overloading example =========================')
class MobilePhone:
    def fetchMobile(self, id = None, brand = None, model = None):
        return 'detail fetched regarding ID : ' + id + ', Brand is : ' + brand + ' and Model is : ' + model

mobilePhones = MobilePhone()
print(mobilePhones.fetchMobile('1', 'Samsung', 'S23'))