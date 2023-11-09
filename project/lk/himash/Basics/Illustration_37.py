# Thread Synchronization
# Set tread priory regarding the process
import threading
from threading import *
from time import *

lock = Lock()

def displayDetails():
    lock.acquire() # one by one process fetched
    for i in range(3):
        print('Details fetched ', threading.current_thread().name)
        sleep(1)
    lock.release() # one by one process finish

thread1 = Thread(target=displayDetails)
thread2 = Thread(target=displayDetails)

thread1.start()
thread2.start()