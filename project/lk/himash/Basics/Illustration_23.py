# Super Keyword, Method Overriding :
# Super keyword use for call/inject parent class variables/methods
# When call the same method name in different class it's getting latest method output.

print('Method overriding example ===============================')


class Parent:
    def method01(self):
        print('Call from method 01 parent class')


class Child(Parent):
    def method01(self):
        print('Call from method 01 from child class')

    def method02(self):
        print('Call from method 02 child class')


obj = Child()
obj.method01()

print('Super Keyword example =============================')


class Parent02:
    def method01(self):
        print('Call from method 01 parent class')


class Child02(Parent02):
    def method02(self):
        self.method01()
        print('Call from method 02 child class')

obj = Child02()
obj.method02()

print('Inheritance example ==================================')
class Calculation:
    count = None
    price = None

    def cal_cons(self, count, price):
        self.count = count
        self. price = price

class Bottle(Calculation):
    def bottleCalculation(self):
        print('Bottles : ', self.price*self.count)

class Laptop(Calculation):
    def laptopCalculation(self):
        print('Laptop : ', self.price*self.count)

bolleObj = Bottle()
bolleObj.cal_cons(4,3)
bolleObj.bottleCalculation()

laptopObj = Laptop()
laptopObj.cal_cons(3,3)
laptopObj.laptopCalculation()
