# Abstract class and methods :
# It's user for implement abstraction concept.
# Able to apply pass keyword for there are doesn't have a method implementation.
# It's unable to create object.
# Child class after inherited from  Abstract class that class also so abstract until method overriding.

from abc import ABC, abstractmethod

class Phone(ABC):

    @abstractmethod
    def fetchDetail(self):
        pass

class Samsung(Phone):
    def fetchDetail(self):
        print('details fetched successfully')

obj = Samsung()
obj.fetchDetail()