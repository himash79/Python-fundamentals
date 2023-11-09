# Multithreading :
# This is a example of tread with classes and methods
import time
from threading import *
from time import *

class GreetingParent(Thread):
    def run(self):
        for i in range(2):
            print('Hello')
            print('Thread 1 name ', current_thread().name)
            sleep(1)

class GreetingChild(Thread):
    def run(self):
        for i in range(2):
            print('my world')
            print('Thread 2 name ', current_thread().name)
            sleep(1)

greet01 = GreetingParent()
greet02 = GreetingChild()

greet01.start()
sleep(0.2)
greet02.start()

greet01.join()
greet02.join()

print('Finished')
