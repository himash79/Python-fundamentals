# Multithreading :
# It's can able to perform task execution specific time.
import threading
from time import sleep

def userNameFetch():
    for i in range(100):
        print('User ' + str(i) + ' name fetched')
        sleep(1)

def userPasswordFetch():
    for i in range(100):
        print('User ' + str(i) + ' password fetched')
        sleep(1)

userNameThread = threading.Thread(target=userNameFetch)
userPasswordThread = threading.Thread(target=userPasswordFetch)

userNameThread.start()
sleep(1)
userPasswordThread.start()