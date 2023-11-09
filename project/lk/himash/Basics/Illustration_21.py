# Contructors :
# Technically it's use object creation same as other languages.

class Mobile:
    id = int
    brand = str
    model = str
    price = float

    def __init__(self, id, brand, model, price):
        self.id = id
        self.brand = brand
        self.model = model
        self.price = price

    def printObj(self):
        return 'ID : ' + str(self.id) + ' | Brand : ' + str(self.brand) + ' | Model : ' + str(self.model) + ' | Price : ' + str(self.price)


m1 = Mobile(1, 'Samsung', 'Galaxy S21', 4500.00)
m2 = Mobile(2, 'Sony', 'XA1 ultra', 2300.00)

print(m1.printObj())
print(m2.printObj())

