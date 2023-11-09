# OOP, Class and Encapsulation :
# Python include OOP concepts same as other language such as Java, PHP, Javascript, C++.
# It's include encapsulation, inheritance etc.
# private modifier identify __ (double underscore).

class Mobile:
    id = 10
    __name = 'Dasith'

    def getId(self):
        return id

    def getName(self):
        return self.__name

    def fetch(self):
        return self.__getAll()

    def __getAll(self):
        return str(self.id) + ' | ' + self.__name


mobile = Mobile()
print(mobile.id)
print(mobile.getName())
print(mobile.fetch())