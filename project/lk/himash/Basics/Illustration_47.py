# Locks and DeadLock :
# These are the simplest primitive for synchronization in Python.
# There are two states of a lock i.e locked and unlocked. A lock is a class in the
# threading module whose object generated in the unlocked state and has two primary methods
# i.e acquire() and release(). When the acquire() method is called, it locks the execution of
# the Lock and blocks it’s execution until the release() method is called in some other thread
# which sets it to unlock state. Locks help us in efficiently accessing a shared resource in a
# program in order to prevent corruption of data, it follows mutual exclusion as only one thread
# can access a particular resource at a time.

# RLock
# The default Lock doesn’t recognize which thread the lock currently holds.
# If the shared resource is being accessed by any thread then other threads
# trying to access the shared resource will get blocked even if it is
# the same thread that locked the shared resource. The Re-entrant lock or
# RLock is used in these situations to prevent undesired blocking from accessing the
# shared resource. If a shared resource is in RLock then it can be called again safely.
# The RLocked resource can be accessed repeatedly by various threads, though it still works
# correctly when called by different threads.
# Let us look at the below example to understand the use of RLocks:

import threading

# initializing the shared resource
geek = 0

# creating a Lock object
lock = threading.Lock()

# the below thread is accessing the
# shared resource
lock.acquire()
geek = geek + 1

# This thread will be blocked
lock.acquire()
geek = geek + 2
lock.release()

# displaying the value of shared resource
print(geek)

# In the above program, two threads are trying to access the shared resource geek simultaneously,
# here when a thread is currently accessing shared resource geek the other thread will be prevented
# from accessing it. When two or more threads try to access the same resource effectively prevent
# each other from accessing the resource this is known as deadlock due to which the above program
# generates no output. However, the above problem in the program can be solved by using RLock.

# program to illustrate the use of RLocks

# importing the module
import threading

# initializing the shared resource
geek = 0

# creating an RLock object instead
# of Lock object
lock = threading.RLock()

# the below thread is trying to access
# the shared resource
lock.acquire()
geek = geek + 1

# the below thread is trying to access
# the shared resource
lock.acquire()
geek = geek + 2
lock.release()
lock.release()

# displaying the value of shared resource
print(geek)

# Locks vs RLock
# 01) A Lock object can not be acquired again by any thread unless it is
# released by the thread which  is accessing the shared resource.
# 01) An RLock object can be acquired numerous times by any thread.

# 02) A Lock object can be released by any thread.
# 02) An RLock object can only be released by the thread which acquired it.

# 03) A Lock object can be owned by none
# 03) An RLock object can be owned by many threads

# 04) Execution of a Lock object is faster.
# 04) Execution of an RLock object is slower than a Lock object