# Mutual exclusion :
# In computer programming, a mutual exclusion (mutex) is a program object
# that prevents multiple threads from accessing the same shared resource simultaneously.
# A shared resource in this context is a code element with a critical section,
# the part of the code that should not be executed by more than one thread at a time.
# For example, a critical section might update a global variable, modify a table in a
# database or write a file to a network server. In such cases, access to the shared
# resource must be controlled to prevent problems to the data or the program itself.


# Mutex in programming
# A multithreaded program can specifically request a mutex for each shared
# resource from the underlying system. If a thread needs to access the resource,
# it must first verify whether the mutex for that resource is locked. If it is unlocked,
# the thread can execute the code s critical section.
# If it is locked, the system typically queues the thread until the mutex becomes unlocked.
# When this occurs, the thread can execute the critical section,
# while the mutex is again locked to prevent other threads from using the resource.

import threading
import time

mutex = threading.Lock()
def get_data(cnt):
    mutex.acquire()
    try:
        thread_id = threading.get_ident()
        time.sleep(0.5)
        print(f"Count: {cnt} (thread {thread_id})")
    finally:
        mutex.release()

count = 1
max_count = 3
while True:
    thread = threading.Thread(target=get_data, args=(count,))
    thread.start()
    count = count + 1
    if count > max_count:
        break